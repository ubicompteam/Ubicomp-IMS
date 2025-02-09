from unittest import mock
import asyncio
import websockets

async def mock_client_send(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response

# 모킹된 클라이언트를 통해 서버에 연결하고 응답을 받는 코드
async def test_websocket_with_mocking():
    mock_send = mock.MagicMock(return_value="Message received")
    with mock.patch('websockets.connect', mock_send):
        response = await mock_client_send('ws://localhost:5002', json.dumps({'key': 'value'}))
        assert response == "Message received"
