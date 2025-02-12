import os

import openai
from openai import OpenAI
from dotenv import load_dotenv

from basic_prompts import cbtprompt_v0, robust_v0


load_dotenv()
# Load the API key from .env file
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def main():
    system_prompt = cbtprompt_v0() + robust_v0()
    conversation = [{"role": "developer", "content": system_prompt}]
    print("Talk2Me: Hi, I'm Talk2Me! What's on your mind?")

    while True:
        # Get user input
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Add user message to the conversation
        conversation.append({"role": "user", "content": user_input})

        # Get response from OpenAI API
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )

            # Extract the chatbot's response
            bot_reply = response.choices[0].message.content
            print(f"Talk2Me: {bot_reply}")
            
            # Add chatbot response to the conversation
            conversation.append({"role": "assistant", "content": bot_reply})

        except openai.error.OpenAIError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
