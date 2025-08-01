# Stripe Django

## Установка проекта и зависимостей

### Установка проекта
`git clone https://github.com/ZenoFromoren/stripe_django.git` <br /><br />

### Установка зависимостей
В папке с установленным проектом

```
python -m venv venv

venv/Scripts/activate

pip install -r requirements.txt
```

### Запуск проекта
`cd stripe_project` (из корневой папки)

В папке `stripe_project` нужно создать файл `.env` по примеру `.env.example`

`python manage.py runserver` <br /><br />


## Описание запросов


### GET `/buy/{id}`
Возвращает `Stripe Session Id` для оплаты продукта с идентификатором `id`

Возвращаемое значение: `{ checkout_session_id: str }` <br /><br />


### GET `/item/{id}`
Возвращает HTML-страницу с информацией о товаре с идентификатором `id` с возможностью его купить <br /><br />


### GET `/buy/order/{id}`
Возвращает `Stripe Session Id` для оплаты заказа с идентификатором `id`

Возвращаемое значение: `{ checkout_session_id: str }` <br /><br />


### GET `/order/{id}`
Возвращает HTML-страницу с информацией о заказе с идентификатором `id` с возможностью его купить
