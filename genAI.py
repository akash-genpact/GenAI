import openai

# Set your OpenAI API key
openai.api_key = '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'

response = openai.Completion.create(
    engine='davinci',
    prompt='Once upon a time',
    max_tokens=100
)

generated_text = response.choices[0].text.strip()
print(generated_text)
