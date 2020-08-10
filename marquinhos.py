import telepot
import sys
import time
from pprint import pprint
from telepot.loop import MessageLoop
import random
import datetime

bot = telepot.Bot('1379433917:AAHMoDATPtbrL92zipxboTp5n4UtNkSWFA4')

print('hey')
print(bot.getMe())

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	command = command.lower()

#	print ('got command: %s' % command)

	if 'bot' in command.split():
		bot.sendMessage(chat_id, 'boy')

	if 'dinizista' in command.split():
		bot.sendMessage(chat_id, 'eae meno meu me deixa eu nao so nao')

	if 'denizista' in command.split():
		bot.sendMessage(chat_id, 'eae meno meu me deixa eu nao so nao')

	if 'dinizmo' in command.split():
		bot.sendMessage(chat_id, 'paraaaa')

	if 'deniz' in command.split():
		bot.sendMessage(chat_id, 'eae meno meu me deixa eu nao so nao')

	if 'dinizta' in command.split():
		bot.sendMessage(chat_id, 'boy')

	if 'salve' in command.split():
		bot.sendMessage(chat_id, 'salve galera eu so o marquinhos eu nao so um bot')

	if 'marquinhos' in command.split():
		bot.sendMessage(chat_id, 'marquinhos sou eu')

	if 'diniz' in command.split():
		bot.sendMessage(chat_id, 'VAI SE FUDE')

	if 'futebol' in command.split():
		bot.sendMessage(chat_id, 'eu odeio futebol cala boca')

	if 'denis' in command.split():
		bot.sendMessage(chat_id, 'denis dj blz, sem futebol nessa casa')

	if 'pepe' in command.split():
		bot.sendMessage(chat_id, 'pepe so se for mercado')

	if 'dniz' in command.split():
		bot.sendMessage(chat_id, 'fodase esse maluco')

	if 'morumbi' in command.split():
		bot.sendMessage(chat_id, 'nao comeca poha')

	if 'niz' in command.split():
		bot.sendMessage(chat_id, 'para carai')

	if 'tecnico' in command.split():
		bot.sendMessage(chat_id, 'nem vem com futebol maluco')

	if 'fernando' in command.split():
		bot.sendMessage(chat_id, 'se for o do sp pode parar')

	if 'vitao' in command.split():
		bot.sendMessage(chat_id, 'vitao gostoso')

	if 'victao' in command.split():
		bot.sendMessage(chat_id, 'vitao gostoso')

bot.message_loop(handle)

while 1:
	time.sleep(10)
