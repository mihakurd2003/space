import os
import requests
from common_functions import get_image
import argparse
from dotenv import load_dotenv


def get_earth_images(api_key: str):
    params = {
        'api_key': api_key,
    }
    response = requests.get(url='https://api.nasa.gov/EPIC/api/natural/images', params=params)
    response.raise_for_status()

    for ind, photo_info in enumerate(response.json()):
        year, month, day = photo_info.get('date').split(' ')[0].split('-')
        name = photo_info.get('image')

        url_photo = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{name}.png'
        get_image(url_photo, 'images', f'space_EPIC_{ind}', extension='.png', params=params)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Your token from https://api.nasa.gov/', default=os.environ['token_NASA'])
    args = parser.parse_args()
    get_earth_images(args.key)


if __name__ == '__main__':
    main()
