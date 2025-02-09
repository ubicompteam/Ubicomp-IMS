import socketio

sio = socketio.Client()

# 서버 연결 이벤트
@sio.on('connect')
def on_connect():
    print("✅ Connected to WebSocket server")

# incident_updated 이벤트 수신
@sio.on('incident_updated')
def on_incident_updated(data):
    print("🚨 Incident Update Received:", data)

# 서버 연결 종료 이벤트
@sio.on('disconnect')
def on_disconnect():
    print("❌ Disconnected from WebSocket server")

# 서버 연결
sio.connect('ws://192.168.1.186:5002')  # 서버 IP & 포트 확인
sio.wait()  # 계속 대기 (이벤트 수신)
