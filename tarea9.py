import os
import telebot

bot=telebot.TeleBot('1856990333:AAEJEwngvN3x9XXWPzz96H4-TYIp8_FEEro')

@bot.message_handler(commands=['centimetros'])

def centimetros(m):
    cid=m.chat.id
    bot.send_photo(cid,open('metrosacentimetro.jpg','rb'))

@bot.message_handler(commands=['metros'])

def metros(m):
    cid=m.chat.id
    bot.send_photo(cid,open('kilometrosametros.jpg','rb'))

@bot.message_handler(commands=['kilometros'])

def kilometro(m):
    cid=m.chat.id
    bot.send_photo(cid,open('millasakilometros.jpg','rb'))

@bot.message_handler(commands=['pulgadas'])

def pulgadas(m):
    cid=m.chat.id
    bot.send_photo(cid,open('piesapulgadas.jpg','rb'))

bot.polling()