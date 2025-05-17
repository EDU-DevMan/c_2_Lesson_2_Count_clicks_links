### О программе

Эта программа позволяет получить короткую ссылку на введенную ссылку, или получить статистику переходов по сгенерированной ссылке.

Программа использует API VK.COM/RU, подробности [тут](https://dev.vk.com/ru/reference)


## Запуск

- Скачайте код проекта:

[c_2_Lesson_2_Count_clicks_links](https://github.com/EDU-DevMan/c_2_Lesson_2_Count_clicks_links.git)

- Создайте виртальное окружение для вашего проекта.

`Пример для  Windows`

```python3 -m venv --copies C:\DevMan\Course_2\Layout\clicks_links\```

, где `clicks_links` - папка виртуального окружения

- Активируйте ваше виртальное окружение:

```..\clicks_links\Scripts\activate.bat```

- Важно, если используется VS Code, активацию виртального окружения можно провести следующим образом:

Нажать `ctrl+shift+p`, из списка Выбрать:

 `Python Selected Interpreter > Create Virtusl Enviroment > venv >`
 
 `> Find C:\DevMan\Course_2\Layout\clicks_links\Scripts\python.exe`

Обязательно перезапустить терминал 

`Terminal > New Terminal`

[`Пример для Windows`](https://dvmn.org/encyclopedia/pip/pip_virtualenv/)

- Установите зависимости

`Пример для Windows`

```py -m pip install -r requirements.txt```

[`Пример для Unix/macOS`](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

- В корне проекта создайте файл `.env`, и заведите переменную `VK_TOKEN=`, в этой переменной будет храниться Ваш личный токен VK `config('VK_TOKEN')`

Как получить токен [VK](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token)


### Примеры использования 

Программа запускается командой ```python.exe .\main.py https://dvmn.org/modules/```

, где ```python.exe .\main.py``` - исполняемы файл программы

, ```https://dvmn.org/modules/``` - аргумент - ссылка для преобразования

Для получения информации о работе программы запустите:

```python.exe .\main.py -h```

1. Можно указать вашу ссылку для получения из неё короткой ссылки, например вводим: `https://dvmn.org/modules/`, ответ: `https://vk.cc/aCA1ad`

Описание API  [utils.getShortLink](https://dev.vk.com/ru/method/utils.getShortLink)

2. Можно получить статистику переходов по этой ссылке, вводим `https://vk.cc/aCA1ad`, в ответ программа выдаст `109` - число переходов.

Описание API  [utils.getLinkStats](https://dev.vk.com/ru/method/utils.getLinkStats)

### Дополнительные настройки

```VERSION = '5.199'``` - текущая версия API (*)
```GETSHORTLINK = 'utils.getShortLink'``` - API для сокращения исходной ссылки
```GETLINKSTATS = 'utils.getLinkStats'``` - API статистики кликов по сокращенной ссылки
```INTERVAL = 'forever'``` - статистика кликов по сокращенной ссылки (по умолчанию 'forever' за весь период)