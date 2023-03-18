# from https://www.codingthesmartway.com/how-to-use-chatgpt-with-python/

import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)


# This will generate a response to the prompt Hello, how are you today? using the ChatGPT model. The response will be returned as a string in the response variable.

response = completion.choices[0].text
print(response)