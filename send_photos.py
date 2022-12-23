import subprocess
import os
import argparse
import time
from dotenv import load_dotenv
import telegram


def send_photos(timeout, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)

    while True:
        subprocess.run('python fetch_APOD_images.py '
                       '& python fetch_nasa_images.py'
                       '& python fetch_spacex_images.py', shell=True)
        for path, dirs, files in os.walk('images'):
            root = path.replace('\\', '/')
            for photo in files:
                with open(f'{path}/{photo}', 'rb') as image:
                    bot.send_photo(chat_id=chat_id, photo=image)

        time.sleep(int(timeout) * 3600)


def main():
    load_dotenv()
    bot_token = os.environ['bot_token']
    chat_id = os.environ['chat_id']

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help='publication frequency in hours', default=os.environ['publication_frequency'])
    args = parser.parse_args()
    send_photos(args.timeout, bot_token, chat_id)


if __name__ == '__main__':
    main()
