from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests

load_dotenv()
openai_api_key = os.getenv("openai_api_key")
client = OpenAI(api_key=openai_api_key)
# image model
MODEL="dall-e-3"

# openai에 보내는 response
response = client.images.generate(
    model=MODEL,
    prompt="호그와트 성을 수채화 양식으로 그려줘",
    size="1024x1024", 
    quality="standard",
    n=1, 
)

image_url = response.data[0].url
pass

# 이미지 파일 이름(경로) 저장
filename = "image.jpg"

# 이미지 데이터 요청
response = requests.get(image_url)

# 이미지 파일 저장
with open(filename, 'wb') as f:
  f.write(response.content)

# 이미지 파일 열기
Image.open(filename)