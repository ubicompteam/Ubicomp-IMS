from flask import Blueprint, request, jsonify
from app.models.log import Log
from app.models.incident import Incident
from datetime import datetime

log_api = Blueprint('log_api', __name__)


@log_api.route('/logs/recent', methods=['GET'])
def get_recent_logs():
    try:
        limit = request.args.get('limit', 5, type=int)  # 기본 5개
        logs = Log.query.order_by(Log.timestamp.desc()).limit(limit).all()
        return jsonify([log.to_dict() for log in logs]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@log_api.route('/logs/period', methods=['GET'])
def get_logs_by_period():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        if not start_date or not end_date:
            return jsonify({"error": "start_date and end_date are required"}), 400
        
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S')

        print(type(start_date), end_date)

        logs = Log.query.filter(Log.timestamp >= start_date, Log.timestamp <= end_date).all()

        print(logs)

        return jsonify([log.to_dict() for log in logs]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
