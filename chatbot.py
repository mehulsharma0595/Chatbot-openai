import openai

openai.api_key = 'enter api key here'

completion = openai.Completion()

start_sequence = '\nChatbot:'
restart_sequence = '\nHuman:'
session_prompt = 'The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\nHuman: Hello, who are you?\nChatbot: I am Chatbot created by OpenAI. How can I help you today?\nHuman:'

def ask(chat_log):
    response = openai.Completion.create(
    # model="babbage:ft-personal-2023-04-17-17-14-47", #text-babbage-001
      model='davinci:ft-personal-2023-04-20-01-12-00',
    #   model='text-babbage-001',
      prompt=chat_log,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      
      stop=["\n"],
    )

    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

while True:
    prompt = input(session_prompt)
    if prompt == 'exit':
        break
    session_prompt += prompt + start_sequence
    completion = ask(session_prompt)
    session_prompt += completion + restart_sequence

print(session_prompt)