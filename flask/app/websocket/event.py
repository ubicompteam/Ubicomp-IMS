import datetime
import socket
import json
from flask_socketio import SocketIO

# 받은 메시지를 처리하는 함수
def extract_status(data: dict):
    return {
        'mobius_ping_status': data.get('mobius', {}).get('ping', {}).get('status', 'False'),
        'mobius_interval_status': data.get('mobius', {}).get('interval', {}).get('status', 'False'),
        'dashboard_status': data.get('dashboard', {}).get('status', 'False'),
        'server_status': data.get('server', {}).get('status', 'False'),
        'test_status': data.get('test', {}).get('status', 'False')  # test_status 수정
    }

# # 소켓 서버에서 데이터를 완전하게 수신하는 함수
# def receive_full_data(conn):
#     buffer = b""
#     while True:
#         chunk = conn.recv(1024)
#         if not chunk:
#             break
#         buffer += chunk
#         print("Received Data (raw):", buffer)  # 로그 출력

#         try:
#             decoded_data = buffer.decode('utf-8', errors='ignore')
#             print("Decoded Data:", decoded_data)

#             # 데이터가 이미 `dict` 형태인지 확인 후 변환
#             if isinstance(decoded_data, dict):
#                 return decoded_data  # 이미 딕셔너리라면 그대로 반환

#             # JSON 문자열이라면 변환
#             data = json.loads(decoded_data)
#             return data
#         except (json.JSONDecodeError, ValueError, SyntaxError) as e:
#             print(f"Invalid data format: {e}. Waiting for more data...")
#             continue  # 계속 데이터 받기

#     return None

# def send_to_websocket(socketio, data):
#     status = extract_status(data)

#     # 상태값 출력
#     print("Sending Status:", status)

#     # 웹소켓 이벤트를 비동기적으로 실행
#     socketio.start_background_task(lambda: socketio.emit('status_update', status))  # 비동기 실행

# def start_socket_server(socketio, host='0.0.0.0', port=5005):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((host, port))  # 서버 주소와 포트 바인딩
#         s.listen()
#         print(f"Socket server started on {host}:{port}")

#         while True:
#             conn, addr = s.accept()
#             with conn:
#                 print(f"Connected by {addr}")

#                 while True:
#                     received_message = receive_full_data(conn)

#                     if received_message and isinstance(received_message, dict):
#                         # ✅ JSON 직렬화 가능하도록 변환
#                         serializable_message = make_json_serializable(received_message)

#                         # 변환된 데이터를 웹소켓으로 전송
#                         send_to_websocket(socketio, serializable_message)
#                     else:
#                         print("Invalid or incomplete data received")
#                         break

# def make_json_serializable(data):
#     """ JSON으로 변환 가능한 형태로 데이터를 변환하는 함수 """
#     if isinstance(data, dict):
#         return {key: make_json_serializable(value) for key, value in data.items()}
#     elif isinstance(data, list):
#         return [make_json_serializable(item) for item in data]
#     elif isinstance(data, bytes):
#         return data.decode('utf-8', errors='ignore')  # ✅ 바이너리를 문자열로 변환
#     elif isinstance(data, datetime.datetime):
#         return data.isoformat()  # ✅ datetime을 문자열로 변환
#     else:
#         return data  # 변환할 필요 없는 값은 그대로 반환
