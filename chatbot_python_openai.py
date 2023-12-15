#1. instalamos la librería de OPENAI
!pip install openai

#2. Importamos la librería
import openai


#3. Configuramos la API Key generada en la plataforma de OPENAI
openai.api_key = 'TU-API-KEY'

#4. Creamos el campo para ingresar un prompt
mensaje_usuario= input("Ingresa una pregunta para el BOT: ")

#5. Llamar a la API de OpenAI para obtener la respuesta del chatbot
consultar_openai = openai.Completion.create(
    engine="text-davinci-003", # versión del modelo
    prompt=mensaje_usuario,       # el promtp ingresado por el usuario
    max_tokens=1000            # cantidad de palabras en la respuesta
)

#6. Obtener la respuesta del chatbot desde la respuesta de la API
respuesta_bot = consultar_openai.choices[0].text.strip()

#7. Imprime la respuesta del chatbot
print("Respuesta del BOT:", respuesta_bot)
