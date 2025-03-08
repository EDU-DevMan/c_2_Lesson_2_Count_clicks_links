import requests

from decouple import config


VERSION = '5.199'
GETSHORTLINK = 'utils.getShortLink'
YOUR_LINK = input()


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


if __name__ == "__main__":
    print('Сокращенная ссылка: ', shorten_link(config('TOKEN'), YOUR_LINK))
