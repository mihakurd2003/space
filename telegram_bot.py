import os
from dotenv import load_dotenv
import telegram


def send_message():
    bot = telegram.Bot(token=os.environ['bot_token'])

    media = telegram.InputMediaDocument(media=open('images/space_APOD_0.jpg', 'rb'))
    bot.send_media_group(chat_id='@kosmos_img', media=[media])


def main():
    load_dotenv()
    send_message()


if __name__ == '__main__':
    main()
