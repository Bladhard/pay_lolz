"""Файл с настройками и конфигами для проекта"""
from dotenv import load_dotenv
import os

load_dotenv()
# LOLZ
LOLZ_API_TOKEN = os.environ.get('LOLZ_API_TOKEN')
LOLZ_USER_ID = os.environ.get('LOLZ_USER_ID')


