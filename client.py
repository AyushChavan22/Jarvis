from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "who is shah rukh khan?"}
  ]
)

print(completion.choices[0].message.content);
