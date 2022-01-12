from telebot.types import BotCommand
import telebot
import pyscreenshot as ImageGrab
import time

TOKEN_API = "TOKEN DO BOT AQUI"

bot = telebot.TeleBot(TOKEN_API)

print()
print("Lembre-se e instalar os requirements! 'pip install -r requirements.txt' ")
print()
print("Ctrl + C para fechar")
print()

def verificar(mensagem):
    return True

def get_print(imagem):
    imagem = ImageGrab.grab()
    imagem.save("Screenshot.png", 'png')
    return imagem

@bot.message_handler(func=get_print,commands = ['print'])
def print(imagem):
    time.sleep(1)
    bot.reply_to(imagem, "Baixe o print /down")
    
   
@bot.message_handler(commands=['down'])
def down(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open('Screenshot.png', 'rb'))


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
     /print Tirar print
/down Baixar print"""
    bot.reply_to(mensagem, texto)

bot.polling()