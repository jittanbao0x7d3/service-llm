import os
import json

from openai import OpenAI

user = """An user's message
{{ message }}
"""

system = """
    You are an AI assistant that help user finding movies. 
    You will help user category the search, whether user 
    want to search for movie or cast with the provided prompt.
    
    You will receive a message from user, then parse it into the structured json
    file like this:
    {
        "collection": string   // can be "movie" or "people",
    }
    
    Here are some example:
    
    INPUT: cast of The God Father
    OUTPUT: 
    {
        "collection": "people",
    }
    
    INPUT: give me some movie about mafia
    OUTPUT: 
    {
        "collection": "movies",
    }
    
    INPUT: the god father
    OUTPUT:
    {
        "collection": "movies",
    }
    
    INPUT: leonardo dicaprio
    OUTPUT: 
    {
        "collection": "people",
    }
"""


def preprocess(prompt: str):
    return user.replace("{{ message }}", prompt), system


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def process(self, prompt: str):
        user_prompt, system_prompt = preprocess(prompt)
        completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_prompt,
                },
                {
                    "role": "system",
                    "content": system_prompt,
                }
            ],
            model="gpt-4o-mini"
        )
        print("Prompt response {}".format(completion.choices[0]))
        return json.loads(completion.choices[0].message.content)
