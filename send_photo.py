import telegram
from dotenv import load_dotenv
import os
import argparse
import random


def send_photo(path_photo):
    bot = telegram.Bot(token=os.environ['bot_token'])
    bot.send_photo(chat_id='@kosmos_img', photo=open(f'images/{path_photo}', 'rb'))


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    args = parser.parse_args()

    if args.path:
        send_photo(args.path)
        return

    photos = os.listdir('images')
    random.shuffle(photos)
    send_photo(random.choice(photos))


if __name__ == '__main__':
    main()
