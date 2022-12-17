import os
from dotenv import load_dotenv
import telegram


def send_message():
    bot = telegram.Bot(token=os.environ['bot_token'])
    bot.send_message(text='Hi', chat_id='@kosmos_img')


def main():
    load_dotenv()
    send_message()


if __name__ == '__main__':
    main()
