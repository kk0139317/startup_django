import os

from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)