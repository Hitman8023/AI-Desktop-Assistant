'''import os
from openai import OpenAI
import google.generativeai as genai

genai.configure(api_key="AIzaSyAKYHmou4ZqI8HFDUB6b_5J0Lqpp-3JR3c")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("essay on holi")
print(response.text)
'''

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["gemini_api"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

response = chat_session.send_message(question)

print(response.text)