from openai import OpenAI
from dotenv import dotenv_values
config_token = dotenv_values(".env")
open_ai_key = config_token['OPEN_AI_KEY']
client = OpenAI(api_key=open_ai_key)


def chat_gpt3(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user",
                   "content": f"{prompt}"}],
    )
    return response.choices[0].message.content


def text_to_picture(promt):
    response = client.images.generate(model="dall-e-2", prompt=promt)
    return response.data[0].url
