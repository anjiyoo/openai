from dotenv import load_dotenv
import os
from openai import OpenAI
import base64
import requests

load_dotenv()
openai_api_key = os.getenv("openai_api_key")
client = OpenAI(api_key=openai_api_key)
# gpt4 vision model
MODEL="gpt-4-vision-preview"

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "이 이미지에는 무엇이 들어있나요? 그들 사이에 어떤 차이가 있나요??",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://www.sputnik.kr/article_img/202012/article_1607406182.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://img.khan.co.kr/news/2023/04/13/news-p.v1.20230223.9f705d6692344077891203bd2239cc5f_P1.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
print(response.choices[0])