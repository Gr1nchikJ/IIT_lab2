import telegram

TOKEN = "6029933916:AAHQdPGxZVJYVI8rM6GmeuwzWkC5KQ0575U"

bot = telegram.Bot(TOKEN)

await bot.send_message(chat_id='357626127', text='Hello world')
