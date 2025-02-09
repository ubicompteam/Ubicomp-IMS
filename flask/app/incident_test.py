# from flask import Flask
# import asyncio
# from app import create_app
# from app.models.incident import Incident
# from app.models.log import Log
# from app.utils.incident_utils import handle_incident



# app = create_app()

# async def test_handle_incident():
#     test_watchdog = "Test1123124124523"

#     # ✅ Flask 애플리케이션 컨텍스트 적용
#     with app.app_context():
#         await handle_incident(test_watchdog)

#         incident = Incident.query.filter_by(service=test_watchdog).order_by(Incident.occurred_at.desc()).first()
#         log = Log.query.filter_by(service=test_watchdog).order_by(Log.id.desc()).first()

#         if incident:
#             print(f"✅ Incident 생성됨: ID={incident.id}, Service={incident.service}, Status={incident.status}, Time={incident.occurred_at}")
#         else:
#             print("❌ Incident 생성 실패")

#         if log:
#             print(f"✅ Log 생성됨: ID={log.id}, Service={log.service}, Status={log.status}, Message={log.message}")
#         else:
#             print("❌ Log 생성 실패")

# if __name__ == "__main__":
#     asyncio.run(test_handle_incident())
import asyncio
import sys
import os
from app import create_app
from flask import app
# print("Python Path:", sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# print("Updated Python Path:", sys.path)

from app.utils.incident_utils import handle_incident 
status_lock = asyncio.Lock()
false_watchdogs = {}

app = create_app()

async def update_status(status):
    """상태 갱신 함수 (비동기적으로 상태 동기화)"""
    global current_status, false_watchdogs
    async with status_lock:  # Lock 획득
        current_status = status
        print(f"Updated status: {current_status}")

        for watchdog, state in status.items():
            if state is False and watchdog not in false_watchdogs:
                # 새로운 False 감지 -> handle_incident 호출
                false_watchdogs[watchdog] = True
                await handle_incident(watchdog)
                print(f"Calling handle_incident for {watchdog}")
            
            elif state is True and watchdog in false_watchdogs:
                # True로 변경되면 다시 감지 가능하도록 제거
                del false_watchdogs[watchdog]

# 임의로 상태를 변경하여 실험
async def test_update_status():
    # 예시로 false 상태를 가지는 watchdog을 설정
    status = {
        "watchdog_12312321": False,
        "watchdog_2": True
    }

    with app.app_context():
        await update_status(status)

    # current_status를 임의로 false로 설정하고 update_status 호출
    global current_status
    current_status = {"watchdog_1": False, "watchdog_2": True}

    # 상태 갱신 함수 실행
    await update_status(status)

# 테스트 실행
if __name__ == "__main__":
    asyncio.run(test_update_status())