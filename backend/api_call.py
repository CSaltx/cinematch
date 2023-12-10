from openai import OpenAI
# from dotenv import load_dotenv
import os

# Set the API key from the environment variable
# load_dotenv('.env')
# key = os.getenv('API_KEY')
client = OpenAI(api_key='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')

def generate_new_line(message):
    return [{
        "role": "user",
        "content": [{"type": "text", "text": message}]
    }]

def develop_response(script, message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # can be gpt-4 for project submission
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
