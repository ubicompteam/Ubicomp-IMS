import json
import socket
import threading
import asyncio
import websockets
from app import create_app
from app.websocket.event import extract_status
from app.utils.incident_utils import handle_incident

# Flask 애플리케이션 생성
app = create_app()
current_status = None
# 상태가 'False'인 watchdog들을 추적
false_watchdogs = {}
status_lock = asyncio.Lock()
websocket_clients = []

def handle_tcp_client(client_socket, addr):
    """TCP 클라이언트 처리"""
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            data = None
            try:
                # TCP 메시지 디코딩
                if isinstance(message, bytes):
                    decoded_message = message.decode('utf-8', errors='ignore').replace("'", '"')
                    print(f"Received TCP message: {decoded_message}")
                    data = json.loads(decoded_message)

                    status = extract_status(data)
                    print(f"Extracted Status : {status}")
                    
                    if status:
                        # 상태 갱신 시 동기화
                        asyncio.run(update_status(status))


                else:
                    print("Received unsupported data format.")
                    client_socket.send("Unsupported data format".encode())
                    continue
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Invalid JSON format received: {e}")
                client_socket.send("Invalid JSON format".encode())
    except Exception as e:
        print(f"Unexpected error with TCP client: {e}")
    finally:
        client_socket.close()

    
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
            



async def emit_watchdog_status(websocket, path=None):
    """웹소켓을 통해 'watchdog_status' 이벤트를 지속적으로 전송"""
    global current_status
    try:
        websocket_clients.append(websocket)
        print(f"New client connected. Total clients: {len(websocket_clients)}")

        while True:  # 상태를 지속적으로 전송
            if current_status is not None:
                await websocket.send(json.dumps({'watchdog_status': current_status}))
                print(f"Sent status update to WebSocket: {current_status}")
            else:
                await websocket.send(json.dumps({'watchdog_status': 'No status available'}))

            await asyncio.sleep(10)

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")
    except Exception as e:
        print(f"Error sending watchdog status: {e}")
    finally:
        websocket_clients.remove(websocket)
        print(f"Client removed. Total clients: {len(websocket_clients)}")


async def start_websocket_server():
    """WebSocket 서버를 시작"""
    server = await websockets.serve(emit_watchdog_status, '0.0.0.0', 5002)
    print("WebSocket server started at ws://127.0.0.1:5002")
    await server.wait_closed()

def start_tcp_server():
    """TCP 서버 시작"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('0.0.0.0', 5005))  # TCP 소켓 서버 포트
        print("Success Connection to TCP Server")
        server.listen(5)
    except Exception as e:
        print(f"Failed to start socket server: {e}")
        return

    while True:
        try:
            client_socket, addr = server.accept()
            # 별도 스레드에서 클라이언트 핸들러 시작
            threading.Thread(target=handle_tcp_client, args=(client_socket, addr), daemon=True).start()
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == '__main__':
    # WebSocket 서버를 비동기적으로 실행
    loop = asyncio.get_event_loop()

    # WebSocket 서버를 실행
    loop.create_task(start_websocket_server())

    # TCP 서버를 별도의 스레드에서 실행
    threading.Thread(target=start_tcp_server, daemon=True).start()
    
    # 이벤트 루프 실행
    loop.run_forever()
    
    asyncio.run(asyncio.sleep(5))
    
    asyncio.run(test_update_status())
