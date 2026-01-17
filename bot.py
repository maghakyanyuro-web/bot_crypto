from telebot import TeleBot, types
from dotenv import load_dotenv
import os
from crypto_bot.parser import parse_data

# Load environment variables
load_dotenv()

# Initialize the bot with the token
bot = TeleBot(token=os.getenv("TOKEN"))

# Handle /start command
@bot.message_handler(commands=['start'])
def start_bot(message):
    # Create inline keyboard
    keyboard = types.InlineKeyboardMarkup()

    # Add inline button
    button = types.InlineKeyboardButton(text="Get Crypto Prices", callback_data="Get_Data")
    keyboard.add(button)

    # Send message with inline keyboard
    bot.send_message(message.chat.id, 'Hello, my name is Crypto Broker Bot!', reply_markup=keyboard)

# Handle callback button presses
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Get_Data":
        # Answer the callback query immediately
        bot.answer_callback_query(call.id, text="Fetching the latest prices...")

        # Scrape data (this can take time)
        crypto_list = parse_data()

        # Check if scraping was successful
        if crypto_list:
            bot.send_message(call.message.chat.id, f"Binance BTC - {crypto_list[0]}\nByBit BTC - {crypto_list[1]}\nOKX - {crypto_list[2]}")
        else:
            bot.send_message(call.message.chat.id, "Sorry, I couldn't fetch the data at the moment.")

# Start polling
bot.polling()