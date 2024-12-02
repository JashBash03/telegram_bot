from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import random
import dotenv
import os

doteenv.load_dotenv()
api_key = os.getenv("API_KEY")

# Función que responde con "Hola Mundo" al comando /hola
async def hola(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola Mundo')

# Función que responde con un número aleatorio al comando /random
async def random_number(update: Update, context: CallbackContext) -> None:
    numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    await update.message.reply_text(f'Número aleatorio: {numero}')

def main():

    # Crea la aplicación y pasa el token de tu bot
    application = Application.builder().token(api_key).build()

    # Registra los comandos con sus funciones respectivas
    application.add_handler(CommandHandler('hola', hola))
    application.add_handler(CommandHandler('random', random_number))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())