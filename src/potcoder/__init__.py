# Import modules
import os
import openai
import platform
from dotenv import load_dotenv

load_dotenv()

# Get the value of the environment variable "POTCODER-VERSION"
potcoder_version = os.getenv("POTCODER-VERSION")

# Welcome message
if potcoder_version is not None:
    print("Welcome to PotCoder [v" + potcoder_version +"]")

# Converts strings to binary [Usage: potcoder.conv_str_bin("[Question when running Python code]")]
def conv_str_bin(machine_question):
    user_input = input(machine_question)
    binary_result = ''.join(format(ord(char), '08b') for char in user_input)

    print("Binary Code: " + binary_result)

# potcoder CLI [Usage: potcoder.cli()]
def cli():
    while True:
        usr_cmd = input("potcoder-1.2.2 >> ")

        if "hi" or "hello" in usr_cmd:
            print("potcoder-" + potcoder_version + " [RETURN] >> Thank you :)")
        elif "bye" in usr_cmd:
            print("potcoder-" + potcoder_version + " [RETURN] >> Good bye! :(")
            break
        elif usr_cmd == "info":
            print("potcoder-" + potcoder_version + " [RETURN] >> potcoder [v" + potcoder_version +"]. Made by Thai Minh Nguyen (@thaiminhnguyen1999)")
        elif usr_cmd == "help":
            print("============================================================")
            print("|                   PotCoder CLI V" + potcoder_version + "                    |")
            print("============================================================")
            print("\nCommands:")
            print("info                  See information about PotCoder CLI")
            print("help                  View available commands in PotCoder")
            print("check-ver             Check and update PotCoder version")
            print("exit                  Exit PotCoder CLI")
        elif usr_cmd == "check-ver":
            exec(open('check-ver.py').read())
        else:
            print("potcoder-" + potcoder_version + " [RETURN] >> I don't understand what you are asking me to do :)?")

# ChatGPT built with Python [Usage: potcoder.pygpt([Your API Key], [Model ID], [Question like "Code: "], [Respond of ChatGPT like "GPT: "])]
def pygpt(openai_api_key, openai_model_id, input_ques, respond_stc):
    openai.api_key = openai_api_key
    MODEL_ID = openai_model_id

    def PyGPT_conversation(conversation):
        response = openai.ChatCompletion.create(
            model=MODEL_ID,
            messages=conversation
        )
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return conversation

    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = PyGPT_conversation(conversation)
    print('PyGPT: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

    while True:
        prompt = input(input_ques)
        if prompt=="gptFoundation()":
            print("Foundation: Python v" + platform.python_version() + " with " + MODEL_ID)
        else:
            conversation.append({'role': 'user', 'content': prompt})
            conversation = PyGPT_conversation(conversation)
            print(respond_stc + ' {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
