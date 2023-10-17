# Foodgram - продуктовый помощник

## Описание

Foodgram это сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Пользователям сайта также будет доступен сервис «Список покупок». Он позволит создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Технологии

- Python 3.9
- Django 3.2
- Django Rest Framework 3.12.4
- Ginocorn
- PostgreSQL

## Информация об авторе

Я студент Яндекс практикума по профессии Python-Разработчик. Меня зовут Влад, мой псевдоним Pupok.
Связь со мной nasyr02001@gmail.com

## Доступ к сайту
    Савина Александра
    https://pupoktestsite.ddns.net/
    Логин от админки: nasyr02001@gmail.com
    Пароль от админки: Jjwcmpb92

## Запуск проекта

- Клонировать репозиторий:
```
https://github.com/Pupoj/foodgram-project-react.git
```

- Cоздать файл .env и заполнить.

- Создать и запустить контейнеры Docker:
```
docker compose up -d
```

- После успешной сборки выполнить миграции:
```
docker compose exec backend python manage.py migrate
```

- Создать суперпользователя:
```
docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
docker compose exec backend python manage.py collectstatic
```

- переместить статику:
```
docker compose exec backend cp -r /app/static/. /backend_static/
```
Перейти на локальный сервер для проверки : http://localhost/
Рабочий проект: https://pupoktestsite.ddns.net/