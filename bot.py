import telegram

TOKEN = "6029933916:AAHQdPGxZVJYVI8rM6GmeuwzWkC5KQ0575U"

bot = telegram.Bot(TOKEN)

bot.send_message(chat_id = '357626127', text="Hello world")
