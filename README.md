# Платформа для Бронирования Мероприятий

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Django Rest Framework](https://img.shields.io/badge/DRF-3.14.0-red.svg)](https://www.django-rest-framework.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-brightgreen.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10.14-blue.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.5-blue.svg)](https://www.postgresql.org/)

## 📋 Описание проекта
Платформа для организации и бронирования мероприятий позволяет пользователям создавать и управлять событиями, бронировать билеты и получать уведомления о своих действиях. Проект основан на микросервисной архитектуре, что делает его гибким и масштабируемым.

**Основные пользователи**:
- Организаторы мероприятий
- Участники (пользователи, бронирующие билеты)

## 🏗️ Архитектура проекта
Проект состоит из следующих микросервисов:

1. **Gateway-сервис (FastAPI)**:
   - Управляет маршрутизацией запросов к различным микросервисам.
2. **Сервис пользователей (Django Rest Framework)**:
   - Регистрация, авторизация, управление пользователями.
3. **Сервис мероприятий (FastAPI)**:
   - Создание и управление мероприятиями.
4. **Сервис бронирования (FastAPI)**:
   - Управление бронированиями и обновление данных о доступных местах.
5. **Сервис уведомлений (FastAPI)**:
   - Асинхронные уведомления пользователей по электронной почте.

## 🛠️ Технологический стек
- **Языки программирования**: Python
- **Фреймворки**: Django Rest Framework, FastAPI
- **Базы данных**: PostgreSQL
- **Контейнеризация**: Docker, Docker Compose
- **Коммуникации между сервисами**: gRPC
- **DevOps и инфраструктура**: Nginx, GitHub Actions (CI/CD)

## 📂 Файловая структура
project-root/ ├── gateway/ │ ├── main.py │ ├── requirements.txt │ └── ... ├── user_service/ │ ├── manage.py │ ├── user_app/ │ ├── requirements.txt │ └── ... ├── event_service/ │ ├── main.py │ ├── requirements.txt │ └── ... ├── booking_service/ │ ├── main.py │ ├── requirements.txt │ └── ... ├── notification_service/ │ ├── main.py │ ├── requirements.txt │ └── ... ├── docker-compose.yml └── README.md

markdown
Копировать код

## 🚀 Установка и запуск
### Требования:
- **Docker** и **Docker Compose**

### Инструкция по запуску:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш_профиль/платформа-мероприятий.git
   cd платформа-мероприятий
Соберите и запустите контейнеры:
bash
Копировать код
docker-compose up --build
Откройте http://localhost в браузере для доступа к платформе.
📄 Описание сервисов

Gateway-сервис
Маршруты:
/: Главная точка входа для всех запросов.
Сервис пользователей
URL: /users/
Основные функции:
Регистрация пользователей
Авторизация и аутентификация
Управление профилем
Сервис мероприятий
URL: /events/
Функции:
Создание и редактирование мероприятий
Просмотр доступных мероприятий
Сервис бронирования
URL: /booking/
Функции:
Бронирование билетов
Управление данными о билетах
Сервис уведомлений
Описание:
Отправка уведомлений по электронной почте после успешных бронирований или при изменении мероприятий.
📚 Документация API

Для каждого микросервиса доступна Swagger-документация:

Сервис пользователей: http://localhost:8003/docs
Сервис мероприятий: http://localhost:8004/docs
Сервис бронирования: http://localhost:8005/docs
🤝 Контрибьютинг

Форкните репозиторий.
Создайте ветку для новой функциональности (git checkout -b feature/НоваяФункция).
Сделайте коммит изменений (git commit -m 'Добавил новую функцию').
Запушьте изменения (git push origin feature/НоваяФункция).
Создайте Pull Request.
📬 Контакты

Автор: [Ваше имя]
Email: [ваш email]
GitHub: [ваш профиль]
Будем рады вашим отзывам и предложениям по улучшению проекта!

Копировать код

Настройте этот шаблон в соответствии с вашим проектом, добавив уникальные детали или ссылки, чтобы сделать его более информативным.
