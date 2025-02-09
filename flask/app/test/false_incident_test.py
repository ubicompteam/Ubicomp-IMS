import asyncio
from app import update_status
# 상태를 업데이트하는 비동기 함수
async def test_update_status():
    # 임의로 current_status 설정 (false 값이 포함된 상태)
    global current_status
    current_status = {
        "watchdog_1": False,  # 임의로 False로 설정
        "watchdog_2": True,
        "watchdog_3": False  # 다른 False도 추가
    }

    # 상태 갱신 호출 (False 상태인 watchdog에 대해 handle_incident가 호출될 것)
    await update_status(current_status)

# 비동기 함수 실행
async def main():
    await test_update_status()

# 이벤트 루프에서 실행
asyncio.run(main())