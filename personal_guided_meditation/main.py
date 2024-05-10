import os

import pathlib
import textwrap

import google.generativeai as genai

from initial_prompt import INITIAL_PROMPT


ai_api_key = os.environ.get('GOOGLE_AI_API')

print(ai_api_key)

genai.configure(api_key=ai_api_key)
model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

SECOND_MSG = """Greetings, esteemed meditation guru. I humbly request your guidance through a profound and transformative mindfulness meditation session, spanning the duration of 10 minutes. With your transcendent wisdom and serenity, I seek to embark on an inward journey, embracing the present moment with unwavering presence and clarity.
During this sacred practice, I implore you to gently lead me through each phase, punctuating your sagacious instructions with intentional pauses, allowing for the full integration of your teachings. To facilitate this harmonious rhythm, I kindly request that you represent the moments of silence between your utterances in the following format: [x seconds of silence], where 'x' denotes the specific number of seconds dedicated to stillness and contemplation.
May your guidance illuminate the path to inner peace, enabling me to cultivate a profound connection with the breath, the body, and the vast expanse of consciousness that resides within. I await your sublime wisdom with an open heart and a receptive mind, ready to immerse myself in the transformative power of mindful presence."""

def main():
    # response = model.generate_content(INITIAL_PROMPT)
    # print(response.text)
    # new_response = model.generate_content("Who are you?")
    # print(new_response.text)
    chat.send_message(INITIAL_PROMPT)
    response = chat.send_message(SECOND_MSG)
    print(response.text)
    



if __name__ == '__main__':
    main()