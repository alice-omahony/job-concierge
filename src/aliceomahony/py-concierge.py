import os
import json
import openai

def apiCall():
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
        temperature=0.2
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
    # message_content = f'I am a {user_input}. What are the important aspects of my job? Give the response as a json list'
    appendToConversation(message_content)
    # Call the OpenAI API with the user input as the prompt
    response = apiCall()

    conversation_history.append(response.choices[0].message)


    skills = json.loads(response.choices[0].message.content)
    for (i, item) in enumerate(skills, start=1):
      print(f'{i})',  item)

    important_skill = int(input("Which skill is most important to you? ")) - 1
    bad_aspect = input("Was there any aspect of the job which you want to avoid in the next position? ")
    message_content = f'What I enjoy most at my current job is {skills[important_skill]}.' \
                      f'The user wants to avoid the following: {bad_aspect}' \
                      f'Based on this can you suggest some other jobs where that would suit the user\'s desires. The response should be in json object containing 2 lists.' \
                      f'Both lists consist json objects containing a title and description' \
                      f'The first list should be jobs in a similar field as the user\'s current job, called similar.' \
                      f'The second list, called different, should contain any jobs that make use of transferable skills but are in a different industry' \
                      f'For each element in the lists, provide a similarity score between the user\'s job and the suggested job. Filter out results with a similarity lower than 0.8'


    appendToConversation(message_content)
    response = apiCall()
    conversation_history.append(response.choices[0].message)


    # for (item) in enumerate(conversation_history):
    #   print(item)
    print(response.choices[0].message.content)
    print('-------------------------------------------\n')


