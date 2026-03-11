from openai import OpenAI

client=OpenAI(
    api_key="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"
)

completion=client.chat.completions.create(
    model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)
print(completion.choices[0].message.content)