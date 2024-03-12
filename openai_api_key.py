from dotenv import load_dotenv
import os
from openai import OpenAI

# .env 파일에서 환경 변수를 로드
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러오기
openai_api_key = os.getenv("openai_api_key")

# api key 불러오는지 확인하기
# print(os.getenv("openai_api_key"))

client = OpenAI(api_key=openai_api_key)

MODEL="gpt-3.5-turbo"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)

