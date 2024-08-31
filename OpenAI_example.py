import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "If Sally is 31 and Bill is 17 and Peter is 44, what are their age differences? Please be concise.",
        }
    ],
    model="gpt-4o-mini",
)

print(chat_completion.choices[0].message.content)