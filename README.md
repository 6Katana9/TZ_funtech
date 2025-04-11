## Инструкция по локальному запуску
1) **git clone <https-link>** - склонируйте проект
2) **touch .env** - в корневой директории создайте файл .env для переменных окружения, и заполните его в соответствии с .env.example
3) **createdb tz_db** - создайте базу данных для проекта
4) **Настройте POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB в docker-compose.yml(контейнер db) под свои данные пользователя бд**
5) **docker-compose up --build** - запустите cборку контейнеров

## Миграции в директории migrations
1) **accounts_migrations** - миграции accounts
2) **rewards_migrations** - миграции rewards