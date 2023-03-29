import whisper
import time
import os
import sys
import openai
from loguru import logger

openai.api_key = os.environ['OPENAI_API_KEY']

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
logger.debug(f"Starting time: {current_time}")

model = whisper.load_model('base')
result = model.transcribe('../data/vovo.wav', fp16=False)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
logger.debug(f"End time: {current_time}")

logger.info(result['text'])

messages = [
        {"role": "system", "content": "You are a helpful assistant."},
]

message = "Give a summary of '%s'" %result['text']
logger.debug(f"The input msg for chatGPT is: {message}")
while message:
    messages.append(
            {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    answer = chat_completion.choices[0].message.content
    logger.info(f"Summary: {answer}")
    
    message = "Come up with questions for '%s'" %result['text']
    messages.append(
            {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    answer = chat_completion.choices[0].message.content
    logger.info(f"Questions: \n {answer}")

    message = False
