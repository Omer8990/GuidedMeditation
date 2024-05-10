import os

import pathlib
import textwrap

import google.generativeai as genai


ai_api_key = os.environ.get('GOOGLE_AI_API')

print(ai_api_key)

genai.configure(api_key=ai_api_key)
model = genai.GenerativeModel('gemini-pro')


def main():
    user_input = input("Please enter your question: ")
    response = model.generate_content(user_input)
    print(response.text)


if __name__ == '__main__':
    main()