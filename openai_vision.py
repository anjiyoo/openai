from dotenv import load_dotenv
import os
from openai import OpenAI

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
        {"type": "text", "text": "이 이미지는 무슨 내용이야?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202302/23/HankyungGametoc/20230223202835516qfzy.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])