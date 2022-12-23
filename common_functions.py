import requests
import os
from urllib import parse


def get_image(url: str, path: str, filename: str, extension='.jpg', params=None):
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    os.makedirs(path, exist_ok=True)

    with open(f'{path}/{filename}{extension}', 'wb') as file:
        file.write(response.content)


def get_extension(url: str):
    parsed_url = parse.urlsplit(url)

    return os.path.splitext(parsed_url.path)[1]
