import os
import json
import openai

def apiCall():
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

def appendToConversation(message_content):
  conversation_history.append({"role": "user", "content": message_content})


# ---------------------------------------------------------------------------------------------

openai.api_key = "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"
conversation_history = []

while True:
    print("Enter what currently do for work, or \"exit\" to quit the program")
    user_input = input("I am a: ")
    message_content = f'I am a {user_input}. What are the important aspects of my job? Give the response as a json list of keywords'
    appendToConversation(message_content)
    # Call the OpenAI API with the user input as the prompt
    response = apiCall()
    conversation_history.append(response.choices[0].message)


    skills = json.loads(response.choices[0].message.content)
    for (i, item) in enumerate(skills, start=1):
      print(f'{i})',  item)

    important_skill = int(input("Which skill is most important to you? ")) - 1
    unimportant_skill = int(input("Which skill is most least important to you? ")) - 1
    message_content = f'What I enjoy most at my current job is {skills[important_skill]}. I least enjoy {skills[unimportant_skill]}. ' \
                      f'Based on this can you suggest some other jobs where these skills are transferable. The response should be in json list consisting of a title and short description' \
                      f'Also include some suggests for jobs in other fields for which my skill-set may apply'


    appendToConversation(message_content)
    response = apiCall()
    conversation_history.append(response.choices[0].message)


    # for (item) in enumerate(conversation_history):
    #   print(item)
    print(response.choices[0].message.content)
    print('-------------------------------------------\n')


