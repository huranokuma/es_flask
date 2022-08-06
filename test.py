import asyncio
import websockets
import json 
import concurrent.futures
import os
## .envファイルを読み込む 本番だと必要？？
from dotenv import load_dotenv
load_dotenv()
###

API_URL = "wss://api-inference.huggingface.co/bulk/stream/cpu/huranokuma/es"
API_TOKEN =os.environ['HugApiKey']

async def hello():
    payload = [
            {
                "inputs": "私",
                "parameters": {"max_length": 100},
            }
        ]
    async with websockets.connect(API_URL) as websocket:
        await websocket.send(f"Bearer {API_TOKEN}".encode("utf-8"))
        await websocket.send(json.dumps(payload).encode("utf-8"))
        data = await websocket.recv()
        print(data)


async def func1():
    await asyncio.sleep(1)
    return 12345,321

async def main():
    task1 = asyncio.create_task(func1())
    ret,ter = await task1
    print(ret,ter) # 12345

asyncio.run(main())
