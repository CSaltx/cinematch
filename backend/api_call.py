import os
import time
from openai import OpenAI

# Set the API key from the environment variable
client = OpenAI(api_key='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')

def generate_new_line(message):
    return [{
        "role": "user",
        "content": [{"type": "text", "text": message}]
    }]

def develop_response(script, message):
    response = client.chat.completions.create(
        model="gpt-4", # can be gpt-4 for project submission
        messages=[{
            "role": "system",
            "content": """
            You are a movie and tv show aficionado (recommendation bot). Expect questions related to movies and tv shows.
            You should respond as if you are a prideful, confident movie reviewer that has seen every movie
            and tv show and can confidently recommend movies. When given such questions, respond with answers
            giving your takes on the movies and always take the person's taste into account and ensure that
            you return with at least 3 recommendations. Remember to use markdown as necessary as well when responding.
            """,
        },] + script + generate_new_line(message), max_tokens=500,
    )
    response_text = response.choices[0].message.content
    return response_text
