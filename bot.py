import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import  settings

logging.basicConfig(filename='bot.log', level=logging.INFO)
# Настройки прокси
#PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    #'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
    
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY , use_context=True) #)
   
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))   
    # Командуем боту начать ходить в Telegram за сообщениями
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
   
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()