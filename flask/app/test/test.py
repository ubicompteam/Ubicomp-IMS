from asyncio import sleep
import time
from flask import Flask
from flask_socketio import SocketIO

# Flask 애플리케이션 생성
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def send_test_incident():
    """임의의 인시던트 데이터를 생성하고 웹소켓으로 전송"""
    test_data = {
        "id": "2",
        "service": "test_service",
        "status": "Noticed",
        "detail": "Test failure",
        "occurred_at": "2025-02-06T15:00:00",
        "restored_at": ""
    }

    print(f"📡 Sending test incident: {test_data}")
    socketio.emit("incident_updated", test_data)  # 이벤트 전송

if __name__ == '__main__':
    # 5초 후 테스트 데이터 전송
    def delayed_emit():
        time.sleep(5)
        for i in range (10):
            send_test_incident()
            sleep(5)

    socketio.start_background_task(delayed_emit)  # 백그라운드에서 실행s
    socketio.run(app, debug=True, host='0.0.0.0', port=5003)