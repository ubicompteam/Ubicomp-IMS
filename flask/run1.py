# import datetime
import json
import socket
# import threading

# from numpy import broadcast
# from app import create_app
# from flask_socketio import emit

# from app.api.log_api import log_api
# from app.api.incident_api import update_status
from app.websocket.event import extract_status

# # Flask 애플리케이션 생성
# app, socketio = create_app()

# # 블루프린트 등록
# app.register_blueprint(log_api, url_prefix='/api')
# app.register_blueprint(update_status, url_prefix='/api')

# import json
# import datetime


# client_socket = None
# addr = None
import asyncio
from http import server
from websockets.asyncio.server import serve


async def echo(websocket):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', 5005))  # TCP 소켓 서버 포트
        server.listen(5)
        print("Success to TCP Socket")
    except Exception as e:
        print(f"Failed to start socket server: {e}")
        return
    
    client_socket, addr = server.accept()

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            
            data = None
            try:
                if isinstance(message, bytes):
                    decoded_message = message.decode('utf-8', errors='ignore').replace("'", '"')
                    print(f"Receiving message: {decoded_message}")
                    data = json.loads(decoded_message)
                else:
                    print("Received unsupported data format.")
                    client_socket.send("Unsupported data format".encode())
                    continue  # 다음 루프로 이동

                status = extract_status(data)

                print(f"Extracted Status: {status}")

                await websocket.send(str(status))
                
                async with asyncio.timeout(timeout=10):
                    m = await websocket.recv()

            except (json.JSONDecodeError, TypeError) as e:
                print(f"Invalid JSON format received: {e}")
                client_socket.send("Invalid JSON format".encode())

            client_socket.send("Message received".encode())

        except ConnectionResetError:
            print(f"Connection reset by {addr}")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            break

    client_socket.close()

async def main():
    async with serve(echo, "0.0.0.0", 8766) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

# @socketio.on('watchdog_status')
# def handle_client(a):
#     global client_socket, addr
#     while True:
#         try:
#             message = client_socket.recv(1024)
#             if not message:
#                 break
            
#             data = None
#             try:
#                 # ✅ 메시지가 bytes라면 디코딩 후 JSON 변환
#                 if isinstance(message, bytes):
#                     decoded_message = message.decode('utf-8', errors='ignore').replace("'", '"')
#                     print(f"Receiving message: {decoded_message}")
#                     data = json.loads(decoded_message)
#                 else:
#                     print("Received unsupported data format.")
#                     client_socket.send("Unsupported data format".encode())
#                     continue  # 다음 루프로 이동

#                 status = extract_status(data)

#                 print(f"Extracted Status: {status}")

#                 # 웹소켓을 통해 전송
#                 socketio.emit('watchdog_status', status)

#                 socketio.sleep(0)
#             except (json.JSONDecodeError, TypeError) as e:
#                 print(f"Invalid JSON format received: {e}")
#                 client_socket.send("Invalid JSON format".encode())

#             client_socket.send("Message received".encode())

#         except ConnectionResetError:
#             print(f"Connection reset by {addr}")
#             break
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             break

#     client_socket.close()

# # @socketio.on('watchdog_status')
# # def send_status(status):
# #     emit('watchdog_status',status, broadcast=True)




# def start_socket_server():
#     global client_socket, addr
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         server.bind(('0.0.0.0', 5005))  # TCP 소켓 서버 포트
#         print(" Success Connection to TCP Server")
#         server.listen(5)
#     except Exception as e:
#         print(f"Failed to start socket server: {e}")
#         return

#     while True:
#         try:
#             client_socket, addr = server.accept()
#             # client_handler = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
#             # client_handler.start()
#         except Exception as e:
#             print(f"Error accepting connection: {e}")



# if __name__ == '__main__':
#     # TCP 소켓 서버를 백그라운드에서 실행
#     threading.Thread(target=start_socket_server, daemon=True).start()

    
#     # Flask 애플리케이션 실행 (웹소켓 포함)
#     socketio.run(app, debug=True, host='0.0.0.0', port=5002)

