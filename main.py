import openai
import os
from wonderwords import RandomWord

# Set the OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Gen the adjectives
r = RandomWord()
adjcetive1 = r.word(include_parts_of_speech=["adjectives"])
adjcetive2 = r.word(include_parts_of_speech=["adjectives"])
adjcetive3 = r.word(include_parts_of_speech=["adjectives"])
adjcetive4 = r.word(include_parts_of_speech=["adjectives"])
adjcetive5 = r.word(include_parts_of_speech=["adjectives"])
adjcetive6 = r.word(include_parts_of_speech=["adjectives"])

# Different prompts
promptType1 = "write a " + adjcetive1 + " website with a lot of sample text in html that has a " + adjcetive2 + " and verbose styling and " + adjcetive3 + " buttons, make it " + adjcetive4 + " Add " +  adjcetive5 + " javascript to the buttons to make them more " + adjcetive6 + "."

promptType2 = "code a " + adjcetive1 + " website that has verbose styling with css, make it " + adjcetive2 + " with interactive javascript that is " + adjcetive3 + " and " + adjcetive4 + "."

promptType3 = "write a website, be verbose with the styling." + " Also make it" + adjcetive1 + " with "+ adjcetive2 + " and verbose javascript, and a " + adjcetive3 + " image."

# client decides prompt
print("Choose prompt:")
print("0. see prompts")
print("1. prompt #1")
print("2. prompt #2")
print("3. prompt #3")
print("4. Your own prompt")

# choice loop
choices = True
while choices:
    cliChoice = int(input())

    # corolates the clients input to the prompt
    if cliChoice == 0:
        print(promptType1 + '\n' + promptType2 + '\n' + promptType3)

    elif cliChoice == 1:
        Genprompt = promptType1
        choices = False
    
    elif cliChoice == 2:
        Genprompt = promptType2
        choices = False

    elif cliChoice ==  3:
        Genprompt = promptType3
        choices = False

    elif cliChoice ==  4:
        Genprompt = input()
        choices = False
    else:
        print("Invalid input")

print("Prompt: " + Genprompt)

# Set the prompt
prompt = Genprompt

# Use the OpenAI API to generate a response
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n = 1,
    temperature=0.5,
)

# Print the response
respText = response["choices"][0]["text"]
print(" Answer:" + '\n' + respText)

# Writes the response into a file/overwrites it
fp = open('index.html', 'w')
fp.write(respText)
fp.close()
