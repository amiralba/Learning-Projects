import time
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application, MessageHandler, filters
import os
from telegram.error import TimedOut
from tweethandler import get_tweets, plot_tweet_graph, proccess_tweet_data


TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
application = Application.builder().token(TELEGRAM_API_KEY).concurrent_updates(True).build()

user_last_request = {}
COOLDOWN_TIME = 5 * 60


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome to Tweet Stats Bot! To get statistics on a user's tweets, send me a Twitter username. "
        "For example, you can send: 'elonmusk' (without the '@').")

async def help(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "To get tweet statistics for a user, simply send their Twitter username (without '@'). "
        "For example, 'elonmusk' works fine!"
    )
    
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))

async def tweets(update: Update, context: CallbackContext):
    username = update.message.text.strip()
    if not username:
        await update.message.reply_text("Please provide a Twitter username.")
        return
    user_id = update.message.from_user.id
    current_time = time.time()

    if user_id in user_last_request:
        time_diff = current_time - user_last_request[user_id]
        if time_diff < COOLDOWN_TIME:
            remaining_time = int(COOLDOWN_TIME - time_diff)
            await update.message.reply_text(f"Please wait {remaining_time} seconds before requesting again.")
            return

    tweet_data = get_tweets(username)
    tweets_per_day, tweets_per_month, tweets_per_year = proccess_tweet_data(tweet_data)
    daily_graph_path, monthly_graph_path, yearly_graph_path = plot_tweet_graph(tweets_per_day, tweets_per_month, tweets_per_year)
    try:
        with open(daily_graph_path, 'rb') as f:
            await update.message.reply_photo(photo=f)
        with open(monthly_graph_path, 'rb') as f:
            await update.message.reply_photo(photo=f)
        with open(yearly_graph_path, 'rb') as f:
            await update.message.reply_photo(photo=f)
    except TimedOut:
        await update.message.reply_text("The request timed out. Please try again later.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tweets))

if __name__ == "__main__":
    application.run_polling()