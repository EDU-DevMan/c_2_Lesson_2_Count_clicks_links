import requests

from decouple import config


headers = {"access_token": config('TOKEN'),
           "user_id":  config('USER_ID'),
           "v":  config('VERSION')}

response = requests.get('https://api.vk.ru/method/utils.getServerTime?/',
                        params=headers)

print(response.text)
