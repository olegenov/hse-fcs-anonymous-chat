'''
Файл настроек. Константы и прочие глобальные штуки - сюда.
'''

import os

import dotenv


dotenv.load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("TOKEN")