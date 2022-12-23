import os
import requests
import argparse
from common_functions import get_image, get_extension
from dotenv import load_dotenv


def get_images_APOD(api_key: str):
    params = {
        'api_key': api_key,
        'count': 10,
    }
    response = requests.get(url='https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()

    for ind, photo in enumerate(response.json()):
        url_extension = get_extension(photo.get('url'))
        if not url_extension:
            continue

        get_image(photo.get('url'), 'images', f'space_APOD_{ind}', extension=url_extension)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Your token from https://api.nasa.gov/', default=os.environ['token_NASA'])
    args = parser.parse_args()
    get_images_APOD(args.key)


if __name__ == '__main__':
    main()
