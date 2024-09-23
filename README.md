## Instructions

* [<span style="color:orange">Полезные ссылки</span>](instruction%2FInfo_Dev.md)
* [<span style="color:orange">Работа с миграциями</span>](instruction%2Falembic_command.md)
---
### Запуск базы данных.
Перейдите папку с файлом docker-compose.yml\
Выполните команду:
```
docker compose up -d pg
```
Либо подключейтесь к своей локальной базе данных.\
Для этого создайте пользователя, и базу данных в своем приложении pg4admin.

Имя базы, а так же пароль и пользователь указан в конфигурации docker-compose.yml
```
CREATE USER admin WITH PASSWORD 'password';
```
```
CREATE DATABASE db WITH OWNER admin;
```
---
# Обновление зависимостей:

* [<span style="color:orange">Инструкция Poetry</span>](https://habr.com/ru/articles/593529/)

```
poetry install
```
---
Создайте .env файл, заполните ключи по примеру из шаблона .env.template
```dotenv
APP_CONFIG__DB__URL=postgresql+asyncpg://user:pwd@localhost:5432/app
APP_CONFIG__DB__ECHO=1
...
...
```
