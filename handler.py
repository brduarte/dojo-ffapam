from openai import OpenAI
import json


def hello(event, context):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": event['body']

            },
        ]
    )

    return completion.choices[0].message.content
