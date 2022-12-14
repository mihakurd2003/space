import requests
import os
from dotenv import load_dotenv


def get_earth_image(path: str):
    params = {
        'api_key': os.environ['token_NASA'],
    }
    response = requests.get(url='https://api.nasa.gov/EPIC/api/natural/images', params=params)
    response.raise_for_status()

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

    for ind, photo_info in enumerate(response.json()[:5]):
        year, month, day = photo_info.get('date').split(' ')[0].split('-')
        name = photo_info.get('image')

        url_photo = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{name}.png'
        response_photo = requests.get(url=url_photo, params=params)

        with open(f'{path}/space_{ind}.png', 'wb') as file:
            file.write(response_photo.content)


def main():
    load_dotenv()
    get_earth_image('images')


if __name__ == '__main__':
    main()
