from flask_socketio import emit
from app.models.incident import Incident
import asyncio
import websockets
import json


connected_clients = set()

async def emit_incident_event(incident_id=None, watchdog=None):
    """웹소켓을 통해 인시던트 이벤트를 전송 (업데이트된 내용만 전송)"""
    try:
        # if incident_id:  # 기존 인시던트 업데이트
        #     # 임의의 인시던트 데이터 생성
        #     incident = {
        #         'id': '1',
        #         'service': 'Service A',
        #         'status': 'Noticed',
        #         'detail': 'This is an example detail for incident.',
        #         'occurred_at': '2025-02-08T12:00:00Z',
        #         'restored_at': ''
        #     }
            
        if incident_id:  # 기존 인시던트 업데이트
            incident = Incident.query.get(incident_id)  # 인시던트를 DB에서 조회

            # 인시던트가 없을 경우 에러 처리
            if not incident:
                print(f"Incident with ID {incident_id} not found.")
                return

            # 웹소켓 데이터 준비
            data = {
                'id': incident.id,
                'service': watchdog if watchdog else incident.service,
                'status': incident.status,
                'detail': incident.detail,
                'occurred_at': incident.occurred_at if incident.occurred_at else "",
                'restored_at': incident.restored_at if incident.restored_at else ""
            }
            event_name = "incident_updated"  # 업데이트된 이벤트

            # 모든 클라이언트에 데이터 전송
            if connected_clients:
                message = json.dumps({'event': event_name, 'data': data})
                await asyncio.gather(*[client.send(message) for client in connected_clients])
                print(f"Sent {event_name} event to FE or Slack: {data}")
        else:
            print("No incident ID provided.")
    except Exception as e:
        print(f"Error sending {event_name} event to frontend: {str(e)}")

