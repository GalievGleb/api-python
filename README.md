# Тестовое задание

Этот репозиторий содержит код и материалы, связанные с тестовым заданием.

## Структура проекта

Проект имеет следующую структуру:

- **lib**: В этой директории содержатся все вспомогательные функции, необходимые для выполнения тестовых задач.

- **log**: Директория, в которой хранятся логи. Ниже приведен пример содержания лога:

    ```
    -----
    Test:test_user_edit.py::TestUserEdit::test_edit_user (call)
    Time:2023-08-23 05:57:01.754641
    Request method: PUT
    Request URL: https://reqres.in/api/users/2
    Request data: {'name': 'Gleb', 'job': 'zion resident'}
    Request headers: {}
    Request cookies: {}

    Response code: 200
    Response text: {"name":"Gleb","job":"zion resident","updatedAt":"2023-08-23T02:57:02.486Z"}
    Response header: {'Date': 'Wed, 23 Aug 2023 02:57:02 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Etag': 'W/"4c-wsRL2U3BoN6kjLet++tdvdXvpBo"', 'Via': '1.1 vegur', 'CF-Cache-Status': 'DYNAMIC', 'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=vJmlMGEe5ep0brxRYXyz25FlIZG%2FZPIChN9m9FY28Gwr9XmwEiK67Qb64hJ1K98j3IkZCqm0gLwWaVb%2F%2BQQfPJLxk0p8BK0Js8U9R%2FVzqZuj6XJDUnq4eBw%2FTA%3D%3D"}],"group":"cf-nel","max_age":604800}', 'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '7fb015f5df049d67-DME', 'Content-Encoding': 'gzip'}
    Response cookies: {}
    -----

    ```

- **tests**: Директория, содержащая две поддиректории: `api` и `web`. 

    - **api**: В этой поддиректории находятся тесты для API.

    - **web**: В этой поддиректории находятся тесты для веб-приложения. Тесты можно запускать из класса файла `test_main_page`.

- **.gitignore**: В этом файле указаны пути и файлы, которые должны быть проигнорированы Git. Обычно в `.gitignore` включаются временные и локальные файлы, такие как логи, кэши, файлы конфигурации, и т.д.

- **requirements.txt**: Файл, содержащий список зависимостей проекта. Зависимости можно установить с помощью команды `pip install -r requirements.txt`.

## Запуск тестов

Для запуска тестов необходимо выполнить следующие шаги:

1. Установите зависимости, перейдя в корневой каталог проекта и выполнив следующую команду:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустите тесты API, выполнив команду:

    ```bash
    pytest tests/api
    ```

3. Для запуска тестов веб-приложения, используйте команду:

    ```bash
    pytest tests/web/test_main_page.py
    ```

## Зависимости

Список зависимостей проекта находится в файле `requirements.txt`. Вы можете установить все необходимые зависимости, выполнив команду `pip install -r requirements.txt`.

## Лицензия

Этот проект лицензирован в соответствии с условиями [лицензии](LICENSE), которая разрешает использование, копирование и распространение кода в соответствии с указанными условиями.

