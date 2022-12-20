import requests
from common_functions import get_image, get_extension
import argparse


def fetch_spacex_last_launch(launch_param: str):
    response = requests.get(url=f'https://api.spacexdata.com/v5/launches/{launch_param}')
    response.raise_for_status()

    url_images = response.json()['links']['flickr']['original']
    if len(url_images) == 0:
        print('Фоток нет')
        return

    for ind, url_img in enumerate(url_images):
        get_image(url_img, 'image', f'spacex_{ind}', get_extension(url_img))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id) if args.id else fetch_spacex_last_launch('latest')


if __name__ == '__main__':
    main()
