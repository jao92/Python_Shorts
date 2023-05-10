import openai

# API HASH
openai.api_key = "YOUR HASH"

# BUCLE
while True:

    #PREGUNTA
    prompt = input("\n💭 Introduce tu pregunta: ")
    if prompt == "salir":
        print("Bye!")
        break
    
    # RESPUESTA
    question = openai.Completion.create(engine="text-davinci-003",
                            prompt = prompt,
                            max_tokens=2048)
    
    print("\n👽 Tu respuesta es: " + question.choices[0].text)
   