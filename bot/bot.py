#!/usr/bin/env python3
import telebot
import os

# Replace with your Telegram Bot API token
BOT_TOKEN = ""

bot = telebot.TeleBot(BOT_TOKEN)

def get_lyrics(song_name: str)->str:
    """
    Fetch lyrics of the given song using Genius API.
    """
    folder_path = "././songs"
    file_name = song_name.replace(" ","_")

    # Combine folder and file to create the full path
    file_path = os.path.join(folder_path, file_name)

    try:
        # Try to open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            return content
    except FileNotFoundError:
        return f"Lyrics not found!"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a song name, and I'll find the lyrics for you 🎶")


@bot.message_handler(func=lambda message: True)
def fetch_lyrics(message):
    song_name = message.text.strip()
    bot.reply_to(message, f"Searching lyrics for: {song_name}...")
    lyrics = get_lyrics(song_name)
    bot.reply_to(message, lyrics)


# Start the bot
print("Bot is running...")
bot.infinity_polling()
