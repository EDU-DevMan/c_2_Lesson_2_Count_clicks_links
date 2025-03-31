import requests

from decouple import config
from urllib.parse import urlparse


VERSION = '5.199'
GETSHORTLINK = 'utils.getShortLink'
GETLINKSTATS = 'utils.getLinkStats'
INTERVAL = 'forever'


def shorten_link(token, url):
    headers = {"access_token": token,
               "v": VERSION,
               "url": url}
    response = requests.get(f'https://api.vk.ru/method/{GETSHORTLINK}/',
                            params=headers)
    response.raise_for_status

    return f"Короткая ссылка: {response.json()['response']['short_url']}"


def count_clicks(token, link):
    headers = {"access_token": token,
               "key": urlparse(link).path[1:],
               "v": VERSION,
               "interval": INTERVAL}

    response = requests.get(f'https://api.vk.ru/method/{GETLINKSTATS}/',
                            params=headers)
    response.raise_for_status

    for quantity in response.json()['response']['stats']:
        return f"Количество просмотров: {quantity['views']}"


def is_shorten_link(url):
    if urlparse(url).netloc == 'vk.cc':
        return count_clicks(config('TOKEN'), url)

    return shorten_link(config('TOKEN'), url)


def main():
    link = input("Введите ссылку: ")

    try:
        print(is_shorten_link(link))
    except KeyError:
        print("Вы ввели ошибочную ссылку")


if __name__ == "__main__":
    main()
