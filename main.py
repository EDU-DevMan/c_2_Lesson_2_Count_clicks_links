import os
import requests
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv


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
    response.raise_for_status()

    return response.json()


def count_clicks(token, link):
    headers = {"access_token": token,
               "key": urlparse(link).path[1:],
               "v": VERSION,
               "interval": INTERVAL}

    response = requests.get(f'https://api.vk.ru/method/{GETLINKSTATS}/',
                            params=headers)
    response.raise_for_status()

    return response.json()


def is_shorten_link(token, url):
    return 'error' not in count_clicks(token, url)


def reads_input():
    parser = argparse.ArgumentParser(
        description="""Эта программа позволяет получить 
        короткую ссылку на введенную ссылку, или получить
        статистику переходов по сгенерированной ссылке."""
    )
    parser.add_argument('url',
                        help='Введите ссылку вида https://dvmn.org/modules/')
    args = parser.parse_args()

    return args.url


def main():
    load_dotenv()

    env_token = os.getenv('VK_TOKEN')
    parser_input = reads_input()

    try:
        if is_shorten_link(env_token, parser_input):
            print("Количество просмотров:",
                  count_clicks(env_token,
                               parser_input)['response']['stats'][0]['views'])
        else:
            print("Короткая ссылка:",
                  shorten_link(env_token,
                               parser_input)['response']['short_url'])

    except KeyError:
        print("Вы ввели ошибочную ссылку")


if __name__ == "__main__":
    main()
