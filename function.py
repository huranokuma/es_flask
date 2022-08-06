import requests
import time
import asyncio
import os

## .envファイルを読み込む 本番だと必要？？
from dotenv import load_dotenv
load_dotenv()
###

API_KEY = os.environ['HugApiKey']

API_URL = "https://api-inference.huggingface.co/models/huranokuma/es"
headers = {"Authorization": "Bearer "+API_KEY}

async def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

async def catch_sentence(prompt_text,max_length):
  start = time.time()
  output = await query({"inputs": prompt_text,
            "parameters": {
                            "max_length":max_length,
                            "min_length":50, #将来的にはこれらの値も変えることができたほうがいいかもしれないが今は...
                            "top_p":0.95,
                            "top_k":500,
                            "temperature":1.00,
                            },
            "options":{
                "wait_for_model": True,
            }
            })
  elapsed_time =round(time.time()-start,2)
  if output[0]['generated_text']!=None:
    sentence = output[0]['generated_text']
  else:
    sentence='エラーが起きました、やり直してください。'
  
  return sentence,elapsed_time
