from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import random

# Función que responde con "Hola Mundo" al comando /hola
async def hola(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola Mundo')

# Función que responde con un número aleatorio al comando /random
async def random_number(update: Update, context: CallbackContext) -> None:
    numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    await update.message.reply_text(f'Número aleatorio: {numero}')

def main():
    # Usa el token que te dio BotFather
    token = "7803540569:AAFJxmtNyls7Y0gxVX6nilAmNTpVE1fQvE8"

    # Crea la aplicación y pasa el token de tu bot
    application = Application.builder().token(token).build()

    # Registra los comandos con sus funciones respectivas
    application.add_handler(CommandHandler('hola', hola))
    application.add_handler(CommandHandler('random', random_number))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())