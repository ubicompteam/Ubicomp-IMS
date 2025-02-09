from app.models.incident import Incident, IncidentStatus
from app.models.log import Log
from app import db
from datetime import datetime, timezone
from app.utils.websocket_utils import emit_incident_event

async def handle_incident(watchdog):
    """False 상태 감지 시 인시던트 및 로그 생성"""
    print(f"Handling incident for: {watchdog}")

    # ✅ 인시던트 생성
    incident = Incident(
        service=watchdog,  
        status=IncidentStatus.NOTICED.value,  # "Noticed" 상태
        detail="",  # 빈 문자열
        occurred_at=datetime.utcnow(),  # 현재 시간 기록
        restored_at=None  # 초기값 없음
    )
    print("Success create Incident")

    # ✅ 로그 생성
    log_message = f"Watchdog {watchdog} has failed."
    log = Log(
        service=watchdog,
        status="Noticed",  # 로그 상태는 "Noticed"
        message="",
        incident=incident  # 관련된 인시던트를 연결
    )
    print("Success create Log")

    try:
        # 트랜잭션 시작
        print("hello1")
        db.session.add(incident)  # 인시던트 추가
        print("hello2")
        db.session.add(log)  # 로그 추가
        print("hello3")
        
        # 커밋 전에 id가 생성되었는지 확인
        db.session.commit()
        
        # 커밋 후에 id가 생성되어 있어야 한다
        if not incident.id:
            raise Exception("Incident ID was not generated.")
    
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")

    # 세션을 여기서 끝내지 않음
    # 커밋 후에 ID 사용
    await emit_incident_event(incident_id=incident.id, watchdog=incident.service)

    print("calling emit_incident_event!!!!!!!")


async def update_incident_and_create_log(incident_id, new_status, new_detail):
    try:
        # 인시던트 조회
        incident = Incident.query.get(incident_id)

        if not incident:
            raise Exception("Incident not found.")
        
        # 상태 및 세부사항 업데이트
        incident.status = new_status
        incident.detail = new_detail
        incident.restored_at = datetime.utcnow()  # 복구 시간 기록

        # 로그 생성
        new_log = Log(
            service=incident.service,
            status=incident.status,
            message=incident.detail,
            incident_id=incident.id
        )

        # DB에 저장
        db.session.add(incident)  # 인시던트 업데이트
        db.session.add(new_log)  # 새로운 로그 추가
        db.session.commit()  # 커밋


        await emit_incident_event(incident.id, incident.service, incident.status, incident.detail)

        
    except Exception as e:
        db.session.rollback()  # 오류 발생 시 롤백
        print(f"Error updating incident and creating log: {str(e)}")
        raise
