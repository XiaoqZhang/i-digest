import os
import time
import openai
import whisper
from loguru import logger

def a2t(audio_path):
    logger.debug(f"Audio2texting")
    openai.api_key = os.environ['OPENAI_API_KEY']

    model = whisper.load_model('base')
    result = model.transcribe(audio_path, fp16=False)['text']

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    message = "Give a summary of '%s'" %result

    while message:
        messages.append(
            {
                "role": "user",
                "content": message
            }
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = chat_completion.choices[0].message.content
        logger.info(f"Summary: {answer}")

        message = "Come up with questions for '%s'" %result
        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = chat_completion.choices[0].message.content
        logger.info(f"Questions: \n {answer}")

        message = False

    return result
