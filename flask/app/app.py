import asyncio
from datetime import datetime
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

import pymysql

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# Flask 애플리케이션 설정
app = Flask(__name__)
CORS(app)
connected_clients = set()


@app.route('/')
def index():
    return "Welcome to the WebSocket Server!"

@app.route("/api/logs/period", methods=["GET"])
def get_logs_by_period():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    db = pymysql.connect(host="192.168.1.186", user="root", password="ubicomp407!", database="IMS")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM log WHERE timestamp BETWEEN %s AND %s ORDER BY timestamp DESC;", (start_date, end_date))
    logs = cursor.fetchall()
    db.close()

    data = []
    for log in logs:
        data.append({
            "id": log[0],
            "timestamp": log[1],
            "incident_id": log[2],
            "service": log[3],
            "status": log[4],
            "message": log[5]
        })

    return make_response(jsonify(data))

async def send_to_clients(updated_incident):
    # 모든 연결된 클라이언트에 메시지 전송
    for client in connected_clients:
        await client.send(str(updated_incident))  

@app.route("/api/incident/period", methods=["GET"])
def get_incidents_by_period():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    db = pymysql.connect(host="192.168.1.186", user="root", password="ubicomp407!", database="IMS")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM incident WHERE occurred_at BETWEEN %s AND %s ORDER BY occurred_at DESC;", (start_date, end_date))
    incidents = cursor.fetchall()
    db.close()

    data = []
    for incident in incidents:
        data.append({
            "id": incident[0],
            "service": incident[1],
            "status": incident[2],
            "details": incident[3],
            "occurred_at": incident[4],
            "resolved_at": incident[5]
        })

    return make_response(jsonify(data))

@app.route('/api/incident/update', methods=['GET'])
def update_status_routes():
    incident_id = request.args.get('incident_id')
    service = request.args.get('service')
    new_status = request.args.get('status')
    new_detail = request.args.get('detail')

    db = pymysql.connect(host="192.168.1.186", user="root", password="ubicomp407!", database="IMS")
    cursor = db.cursor()
    
    if new_status == 'restored':
        cursor.execute("UPDATE incident SET status=%s, detail=%s, restored_at=%s WHERE id=%s", (new_status, new_detail, datetime.now(), incident_id))
        print("Final incident update!!")
    else: 
        cursor.execute("UPDATE incident SET status=%s, detail=%s WHERE id=%s", (new_status, new_detail, incident_id))
        print("incident update!!")
        
    cursor.execute("INSERT INTO log (incident_id, service, status, message, timestamp) VALUES (%s, %s, %s, %s, NOW())", 
        (incident_id, service, new_status, new_detail))

    db.commit()
    db.close()

    # cursor.execute("SELECT id, service, status, detail, occurred_at, restored_at FROM incident WHERE id=%s", (incident_id,))
    # incident_data = cursor.fetchone()

    # db.close()

    # if incident_data:
    #     updated_incident = {
    #         'incident_id': incident_data[0],
    #         'status': incident_data[1],
    #         'detail': incident_data[2],
    #         'service': incident_data[3]
    #     }

    #     # 업데이트된 인시던트 정보를 연결된 모든 클라이언트에 전송
    #     asyncio.run(send_to_clients(updated_incident))


    return make_response(jsonify({"message": "Incident updated"}))

if __name__ == '__main__':
    app.run(host='192.168.1.186', port=5000, debug=True)

