from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= [
        {"role": "system", "content": "You are virtual assistant named Alexa skilled in general task like Google cloud"},
        {"role": "user", "content": "Explain love"}
    ]
)
print(completion.choices[0].message.content)