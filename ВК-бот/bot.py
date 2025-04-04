from vkbottle.bot import Bot

from constants import API
from data import MyDict
from translator import My_Translator

bot = Bot(API)
bot.labeler.vbml_ignore_case = True

USERS = MyDict()
Translator = My_Translator()
