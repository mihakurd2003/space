import telegram
from dotenv import load_dotenv
import os
import argparse
import random


def send_photo(path_photo, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)
    with open(f'images/{path_photo}', 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image)


def main():
    load_dotenv()
    bot_token = os.environ['bot_token']
    chat_id = os.environ['chat_id']
    photos = os.listdir('images')
    random.shuffle(photos)

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='The path to the file', default=random.choice(photos))
    args = parser.parse_args()

    send_photo(args.path, bot_token, chat_id)


if __name__ == '__main__':
    main()
