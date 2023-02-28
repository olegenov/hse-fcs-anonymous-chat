'''
В этом файле находится всё для работы самого бота 
и его взаимодействия с пользователем.
'''

import telebot as tb

from settings import Settings

bot = tb.TeleBot(Settings.BOT_TOKEN)