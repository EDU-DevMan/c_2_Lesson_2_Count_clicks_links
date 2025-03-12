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
    try:
        return response.json()['response']['short_url']
    except KeyError:
        return "Вы ввели ошибочную ссылку!"


def count_clicks(token, link):
    headers = {"access_token": token,
               "key": urlparse(link).path[1:],
               "v": VERSION,
               "interval": INTERVAL}

    response = requests.get(f'https://api.vk.ru/method/{GETLINKSTATS}/',
                            params=headers)
    try:
        for quantity in response.json()['response']['stats']:
            return quantity['views']
    except KeyError:
        return "Вы ввели ошибочную сокращенную ссылку!"


def is_shorten_link(url):
    if urlparse(url).path[1:]:
        return count_clicks(config('TOKEN'), url)
    else:
        return shorten_link(config('TOKEN'), url)


def main():
    link = input("Введите ссылку: ")
    print(is_shorten_link(link))


if __name__ == "__main__":
    main()
