from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 파일에서 환경 변수를 로드
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러오기
openai_api_key = os.getenv("openai_api_key")

# api key
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)