import logging
import requests  
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Crea un log de los fallos y excepciones
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

url = "http://api.weatherapi.com/v1/forecast.json?key=894dd5dcbf7d410da13234020230704&q=q=Lomas de Zamora&days=2&aqi=no&alerts=no"

response = requests.get(url) # Realizamos el llamado a la api 

data = response.json() # Parseamos la data recibida a formato JSON

grados_c_ahora = data["current"]["temp_c"] # Accedemos a la temperatura actual

grados_c_ahora = str(grados_c_ahora) # Casteamos para poder concatenar

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Buenas!! La temperatura actualmente es de " + grados_c_ahora)


# Crea el bot
application = ApplicationBuilder().token('6124422376:AAGvV95nIq_JUyf_3mFVRPjiSa6Hyz8Td7w').build()
    
# Escucha el comando /start en el chat
start_handler = CommandHandler('start', start) 
application.add_handler(start_handler)

# Corre el codigo hasta que hagas control c
application.run_polling()


# https://www.weatherapi.com/api-explorer.aspx#forecast PRUEBA DE API





