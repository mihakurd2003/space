import subprocess
import os
import argparse
import time
from dotenv import load_dotenv
import telegram


def send_photos(timeout):
    bot = telegram.Bot(token=os.environ['bot_token'])

    while True:
        subprocess.run('python fetch_APOD_images.py '
                       '& python fetch_nasa_images.py'
                       '& python fetch_spacex_images.py', shell=True)
        for path, dirs, files in os.walk('images'):
            root = path.replace('\\', '/')
            for photo in files:
                bot.send_photo(chat_id='@kosmos_img', photo=open(f'{path}/{photo}', 'rb'))

        time.sleep(int(timeout) * 3600)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout')
    args = parser.parse_args()
    send_photos(args.timeout) if args.timeout else send_photos(os.environ['publication_frequency'])


if __name__ == '__main__':
    main()
