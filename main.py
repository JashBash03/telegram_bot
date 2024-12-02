from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import random
import dotenv
import os
import subprocess

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")

# Función que responde con "Hola Mundo" al comando /hola
async def hola(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola Mundo')

# Función que responde con un número aleatorio al comando /random
async def random_number(update: Update, context: CallbackContext) -> None:
    numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    await update.message.reply_text(f'Número aleatorio: {numero}')

# Función que responde con un saludo personalizado al comando /saludo <nombre>
async def saludo(update: Update, context: CallbackContext) -> None:
    if context.args:  # Si hay argumentos después del comando
        nombre = " ".join(context.args)  # Une los argumentos en un solo string
        await update.message.reply_text(f'¡Hola {nombre}!')
    else:
        await update.message.reply_text('Por favor, ingresa un nombre después del comando. Ejemplo: /saludo Juan')

async def ping(update: Update, context: CallbackContext) -> None:
    if context.args:  # Si hay un dominio después del comando
        dominio = context.args[0]
        try:
            # Ejecuta el comando ping para obtener los primeros 4 paquetes
            result = subprocess.run(
                ['ping', '-c', '4', dominio], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            # Filtra la salida para mostrar solo los paquetes enviados
            paquetes = result.stdout.splitlines()
            await update.message.reply_text("\n".join(paquetes))
        except Exception as e:
            await update.message.reply_text(f"Error al hacer ping a {dominio}: {str(e)}")
    else:
        await update.message.reply_text("Por favor, ingresa un dominio después del comando. Ejemplo: /ping google.com")

def main():

    # Crea la aplicación y pasa el token de tu bot
    application = Application.builder().token(api_key).build()

    # Registra los comandos con sus funciones respectivas
    application.add_handler(CommandHandler('hola', hola))
    application.add_handler(CommandHandler('random', random_number))
    application.add_handler(CommandHandler('saludo', saludo))
    application.add_handler(CommandHandler('ping', ping))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())