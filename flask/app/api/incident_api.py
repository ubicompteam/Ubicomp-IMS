from datetime import datetime
from flask import Blueprint, request, jsonify
from app.models.incident import Incident
# from app.utils.incident_utils import update_incident_and_create_log



def create_update_status_blueprint():
    update_status = Blueprint('update_status', __name__)
    
    @update_status.route('/incident/update', methods=['POST'])
    def update_status_routes(incident_id):
        try:
            # 클라이언트로부터 받은 데이터
            incident_id = request.json.get('incident_id')
            new_status = request.json.get('status')
            new_detail = request.json.get('detail')

            from app.utils.incident_utils import update_incident_and_create_log
            
            if not new_status or not new_detail:
                return jsonify({"error": "Invalid data"}), 400

            # 요청받은 인시던트 ID와 상태, 세부 내용으로 업데이트 처리
            update_incident_and_create_log(incident_id, new_status, new_detail)
            
            return jsonify({
                "message": "Incident status updated and log created successfully"
            }), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        
        
    @update_status.route('/incident/all', methods=['GET'])
    def get_all_incidents():
        """모든 인시던트를 최신순으로 조회"""
        try:
            incidents = Incident.query.order_by(Incident.occurred_at.desc()).all()
            
            incident_list = [{
                "id": inc.id,
                "service": inc.service,
                "status": inc.status,
                "detail": inc.detail,
                "occurred_at": inc.occurred_at,
                "restored_at": inc.restored_at
            } for inc in incidents]

            return jsonify({"incidents": incident_list}), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    
    @update_status.route('/incident/period', methods=['GET'])
    def get_period_incidents():
        try:
            # 요청에서 start_date, end_date 가져오기
            start_date_str = request.args.get('start_date')
            end_date_str = request.args.get('end_date')

            # 날짜 형식이 올바른지 확인 후 변환 (잘못된 입력 예외 처리)
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S') if start_date_str else None
                end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S') if end_date_str else None
            except ValueError:
                return jsonify({"error": "Invalid date format. Use YYYY-MM-DDTHH:MM:SS"}), 400

            # 기간 필터 적용하여 데이터 조회
            query = Incident.query
            if start_date:
                query = query.filter(Incident.occurred_at >= start_date)
            if end_date:
                query = query.filter(Incident.occurred_at <= end_date)

            # 최신순 정렬 후 조회
            incidents = query.order_by(Incident.occurred_at.desc()).all()

            # JSON 응답 생성
            incident_list = [{
                "id": inc.id,
                "service": inc.service,
                "status": inc.status,
                "detail": inc.detail,
                "occurred_at": inc.occurred_at.isoformat() if inc.occurred_at else None,
                "restored_at": inc.restored_at.isoformat() if inc.restored_at else None
            } for inc in incidents]

            return jsonify({"incidents": incident_list}), 200

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return update_status