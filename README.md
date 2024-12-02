# **Документация проекта "Event Booking Platform"**

---

## **Содержание**

1. [Введение](#введение)
2. [Обзор проекта](#обзор-проекта)
3. [Архитектура системы](#архитектура-системы)
   - 3.1. [Общая схема взаимодействия](#общая-схема-взаимодействия)
   - 3.2. [Описание микросервисов](#описание-микросервисов)
4. [Используемые технологии и стек](#используемые-технологии-и-стек)
5. [Детальное описание микросервисов](#детальное-описание-микросервисов)
   - 5.1. [User Service](#user-service)
   - 5.2. [Event Service](#event-service)
   - 5.3. [Booking Service](#booking-service)
   - 5.4. [Payment Service](#payment-service)
   - 5.5. [Notification Service](#notification-service)
   - 5.6. [Review Service](#review-service)
   - 5.7. [Log Service](#log-service)
   - 5.8. [Gateway Service](#gateway-service)
6. [Инфраструктура и коммуникация](#инфраструктура-и-коммуникация)
   - 6.1. [gRPC](#grpc)
   - 6.2. [RabbitMQ](#rabbitmq)
   - 6.3. [Consul](#consul)
   - 6.4. [Docker и Docker Compose](#docker-и-docker-compose)
7. [Настройка и запуск проекта](#настройка-и-запуск-проекта)
   - 7.1. [Предварительные требования](#предварительные-требования)
   - 7.2. [Клонирование репозитория](#клонирование-репозитория)
   - 7.3. [Настройка переменных окружения](#настройка-переменных-окружения)
   - 7.4. [Запуск микросервисов](#запуск-микросервисов)
8. [API документация](#api-документация)
   - 8.1. [User Service API](#user-service-api)
   - 8.2. [Event Service API](#event-service-api)
   - 8.3. [Booking Service API](#booking-service-api)
   - 8.4. [Payment Service API](#payment-service-api)
   - 8.5. [Notification Service API](#notification-service-api)
   - 8.6. [Review Service API](#review-service-api)
9. [Безопасность и аутентификация](#безопасность-и-аутентификация)
10. [Тестирование и мониторинг](#тестирование-и-мониторинг)
11. [Frontend на Next.js](#frontend-на-nextjs)
12. [Будущие планы и улучшения](#будущие-планы-и-улучшения)
13. [Заключение](#заключение)

---

## **Введение**

**Event Booking Platform** — это микросервисное приложение для организации и бронирования мероприятий. Платформа предоставляет возможность пользователям создавать, просматривать и бронировать мероприятия, осуществлять оплату билетов, получать уведомления и оставлять отзывы.

---

## **Обзор проекта**

- **Цель проекта**: Предоставить удобную и масштабируемую платформу для организации и участия в мероприятиях с использованием современных технологий и подходов.
- **Основные функции**:
  - Регистрация и авторизация пользователей с различными ролями (администратор, организатор, участник).
  - Создание, управление и просмотр мероприятий.
  - Бронирование билетов и оплата через интегрированные платёжные системы.
  - Отправка уведомлений пользователям.
  - Оставление отзывов и оценок о мероприятиях.

---

## **Архитектура системы**

### **3.1. Общая схема взаимодействия**

```plaintext
                            +----------------+
                            |  Gateway API   |
                            +--------+-------+
                                     |
                                     v
+-----------+     +-----------+     +-----------+
|  User     |     |  Event    |     |  Booking  |
|  Service  |<--->|  Service  |<--->|  Service  |
+-----+-----+     +-----+-----+     +-----+-----+
      |                 |                 |
      v                 v                 v
+-----+-----+     +-----+-----+     +-----+-----+
|  Payment  |     | Notification|   |  Review   |
|  Service  |     |  Service    |   |  Service  |
+-----------+     +-------------+   +-----------+

```

- **Gateway API**: Единая точка входа для всех запросов с фронтенда.
- **gRPC**: Используется для синхронного взаимодействия между сервисами.
- **RabbitMQ**: Для асинхронной коммуникации (уведомления, логи и т.д.).
- **Consul**: Сервис-реестр для обнаружения и регистрации микросервисов.

### **3.2. Описание микросервисов**

1. **User Service**: Управление пользователями и аутентификация.
2. **Event Service**: Управление мероприятиями.
3. **Booking Service**: Обработка бронирований.
4. **Payment Service**: Обработка платежей.
5. **Notification Service**: Отправка уведомлений.
6. **Review Service**: Система отзывов и оценок.
7. **Log Service**: Централизованное логирование.
8. **Gateway Service**: Маршрутизация запросов к соответствующим сервисам.

---

## **Используемые технологии и стек**

- **Язык программирования**: Python
- **Фреймворки**:
  - **Django REST Framework (DRF)** для `User Service`
  - **FastAPI** для остальных микросервисов
- **Базы данных**: PostgreSQL
- **Коммуникация между сервисами**:
  - **gRPC**
  - **RabbitMQ**
- **Сервис-реестр**: **Consul**
- **Контейнеризация**: Docker, Docker Compose
- **Оркестрация**: Планируется использование Kubernetes
- **Логирование**: Loguru, ELK Stack (Elasticsearch, Logstash, Kibana)
- **Мониторинг**: Prometheus, Grafana
- **Фронтенд**: Next.js

---

## **Детальное описание микросервисов**

### **5.1. User Service**

- **Функциональность**:
  - Регистрация и авторизация пользователей
  - Управление профилем и ролями
  - Аутентификация с использованием JWT
- **Технологии**:
  - Django REST Framework
  - PostgreSQL
- **API Эндпоинты**:
  - `POST /register/` — Регистрация пользователя
  - `POST /login/` — Авторизация и получение JWT
  - `GET /users/{id}/` — Получение информации о пользователе
- **gRPC Методы**:
  - Проверка токена и получение данных пользователя для других сервисов

### **5.2. Event Service**

- **Функциональность**:
  - Создание, редактирование, удаление мероприятий
  - Просмотр списка мероприятий
  - Управление категориями и тегами
- **Технологии**:
  - FastAPI
  - PostgreSQL
- **API Эндпоинты**:
  - `POST /events/` — Создать новое мероприятие
  - `GET /events/` — Получить список мероприятий
  - `GET /events/{id}/` — Получить детали мероприятия
  - `PUT /events/{id}/` — Обновить мероприятие
  - `DELETE /events/{id}/` — Удалить мероприятие

### **5.3. Booking Service**

- **Функциональность**:
  - Бронирование билетов на мероприятия
  - Управление статусами бронирования
- **Технологии**:
  - FastAPI
  - PostgreSQL
- **API Эндпоинты**:
  - `POST /bookings/` — Создать бронирование
  - `GET /bookings/{id}/` — Получить информацию о бронировании
  - `DELETE /bookings/{id}/` — Отменить бронирование

### **5.4. Payment Service**

- **Функциональность**:
  - Обработка платежей через **FreedomPay (PayBox)**
  - Взаимодействие с платёжным шлюзом
- **Технологии**:
  - FastAPI
  - PostgreSQL
- **API Эндпоинты**:
  - `POST /payments/` — Инициировать платеж
  - `GET /payments/{id}/` — Получить статус платежа
- **Интеграция**:
  - Получает информацию о бронированиях из `Booking Service`
  - Уведомляет `Notification Service` о статусе платежа

### **5.5. Notification Service**

- **Функциональность**:
  - Отправка уведомлений пользователям (email, SMS, push)
  - Обработка сообщений из очередей RabbitMQ
- **Технологии**:
  - FastAPI
  - RabbitMQ
  - Celery
- **API Эндпоинты**:
  - `POST /notifications/` — Отправить уведомление
- **Связь**:
  - Получает сообщения от других сервисов через RabbitMQ
  - Обрабатывает фоновые задачи с помощью Celery

### **5.6. Review Service**

- **Функциональность**:
  - Оставление отзывов и оценок о мероприятиях
  - Модерация отзывов
- **Технологии**:
  - FastAPI
  - PostgreSQL
- **API Эндпоинты**:
  - `POST /reviews/` — Оставить отзыв
  - `GET /reviews/{event_id}/` — Получить отзывы о мероприятии

### **5.7. Log Service**

- **Функциональность**:
  - Централизованное логирование
  - Сбор и хранение логов из всех микросервисов
- **Технологии**:
  - FastAPI
  - MongoDB (или Elasticsearch)
- **Интеграция**:
  - Получает логи от микросервисов через RabbitMQ
  - Предоставляет интерфейс для просмотра логов

### **5.8. Gateway Service**

- **Функциональность**:
  - Маршрутизация входящих запросов к соответствующим микросервисам
  - Обработка CORS, аутентификация, лимитирование запросов
- **Технологии**:
  - FastAPI или Nginx
- **Настройки**:
  - Конфигурация маршрутов к микросервисам
  - Защита API ключами или токенами

---

## **Инфраструктура и коммуникация**

### **6.1. gRPC**

- **Назначение**: Синхронное взаимодействие между микросервисами с высокой производительностью.
- **Использование**:
  - Проверка аутентификации и авторизации
  - Получение данных о пользователях и мероприятиях
- **Настройка**:
  - Файлы `.proto` определяют интерфейсы сервисов
  - Сгенерированные Python-модули используются в коде

### **6.2. RabbitMQ**

- **Назначение**: Асинхронная коммуникация между сервисами через очереди сообщений.
- **Использование**:
  - Отправка уведомлений
  - Логирование
  - Обработка событий платежей
- **Настройка**:
  - Очереди создаются для каждого типа сообщений
  - Микросервисы выступают в роли производителей и потребителей сообщений

### **6.3. Consul**

- **Назначение**: Сервис-реестр для регистрации и обнаружения микросервисов.
- **Использование**:
  - Регистрация микросервисов при запуске
  - Поиск сервисов другими микросервисами
- **Настройка**:
  - Конфигурация Consul в Docker Compose
  - Регистрация сервисов через API Consul

### **6.4. Docker и Docker Compose**

- **Назначение**: Контейнеризация микросервисов для упрощения развёртывания и масштабирования.
- **Использование**:
  - Каждый микросервис имеет свой Dockerfile
  - Docker Compose используется для запуска всех сервисов одновременно
- **Настройка**:
  - Общий `docker-compose.yml` файл в корне проекта
  - Сетевые настройки и зависимости между сервисами

---

## **Настройка и запуск проекта**

### **7.1. Предварительные требования**

- **Установленные приложения**:
  - Docker
  - Docker Compose
- **Порты**:
  - Убедитесь, что необходимые порты (например, 8000-8006, 5672, 8500) свободны

### **7.2. Клонирование репозитория**

```bash
git clone https://github.com/yourusername/event-booking-platform.git
cd event-booking-platform
```

### **7.3. Настройка переменных окружения**

- Создайте файлы `.env` для каждого микросервиса на основе примеров `example.env`
- Общие переменные:
  - **DATABASE_URL**
  - **RABBITMQ_HOST**
  - **CONSUL_URL**
  - **SECRET_KEY**

### **7.4. Запуск микросервисов**

- Запустите все сервисы с помощью Docker Compose:

```bash
docker-compose up --build
```

- **Примечание**: При первом запуске может потребоваться дополнительное время для загрузки образов и установки зависимостей.

---

## **API документация**

### **8.1. User Service API**

- **Регистрация пользователя**

  ```http
  POST /register/
  Content-Type: application/json

  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```

- **Авторизация**

  ```http
  POST /login/
  Content-Type: application/json

  {
    "email": "john@example.com",
    "password": "securepassword"
  }
  ```

- **Получение информации о пользователе**

  ```http
  GET /users/{id}/
  Authorization: Bearer <JWT_TOKEN>
  ```

### **8.2. Event Service API**

- **Создание мероприятия**

  ```http
  POST /events/
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "title": "Tech Conference",
    "description": "Annual tech conference",
    "date": "2024-12-01",
    "location": "New York",
    "max_participants": 500
  }
  ```

- **Получение списка мероприятий**

  ```http
  GET /events/
  ```

- **Получение деталей мероприятия**

  ```http
  GET /events/{id}/
  ```

### **8.3. Booking Service API**

- **Создание бронирования**

  ```http
  POST /bookings/
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "event_id": 123,
    "seats": 2
  }
  ```

- **Получение информации о бронировании**

  ```http
  GET /bookings/{id}/
  Authorization: Bearer <JWT_TOKEN>
  ```

### **8.4. Payment Service API**

- **Инициирование платежа**

  ```http
  POST /payments/
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "booking_id": 456,
    "payment_method": "credit_card"
  }
  ```

- **Получение статуса платежа**

  ```http
  GET /payments/{id}/
  Authorization: Bearer <JWT_TOKEN>
  ```

### **8.5. Notification Service API**

- **Отправка уведомления** (обычно вызывается другими сервисами через RabbitMQ)

  ```http
  POST /notifications/
  Content-Type: application/json

  {
    "user_id": 789,
    "message": "Your booking is confirmed!",
    "type": "email"
  }
  ```

### **8.6. Review Service API**

- **Оставление отзыва**

  ```http
  POST /reviews/
  Authorization: Bearer <JWT_TOKEN>
  Content-Type: application/json

  {
    "event_id": 123,
    "rating": 5,
    "comment": "Great event!"
  }
  ```

- **Получение отзывов о мероприятии**

  ```http
  GET /reviews/{event_id}/
  ```

---

## **Безопасность и аутентификация**

- **JWT-токены**: Используются для аутентификации пользователей. Токены выдаются `User Service` при авторизации.
- **Роли пользователей**:
  - **Администратор**: Полный доступ ко всем ресурсам.
  - **Организатор**: Может создавать и управлять своими мероприятиями.
  - **Участник**: Может бронировать мероприятия и оставлять отзывы.
- **Защита API**: Эндпоинты, требующие аутентификации, проверяют JWT-токен в заголовке `Authorization`.
- **Хранение паролей**: Пароли пользователей хранятся в хэшированном виде с использованием алгоритма `bcrypt` или аналогичного.

---

## **Тестирование и мониторинг**

- **Юнит-тестирование**: Использование `pytest` для тестирования функциональности микросервисов.
- **Интеграционное тестирование**: Проверка взаимодействия между микросервисами.
- **Мониторинг**:
  - **Prometheus**: Сбор метрик с микросервисов.
  - **Grafana**: Визуализация метрик и создание дашбордов.
- **Логирование**:
  - **Loguru**: Логирование в микросервисах.
  - **ELK Stack**: Централизованное хранение и анализ логов.

---

## **Frontend на Next.js**

- **Цель**: Создать пользовательский интерфейс для взаимодействия с платформой.
- **Основные страницы**:
  - **Главная страница**: Список доступных мероприятий.
  - **Страница мероприятия**: Детали выбранного мероприятия.
  - **Страница регистрации и входа**: Формы для регистрации и авторизации.
  - **Профиль пользователя**: Информация о бронированиях и настройках.
  - **Страница бронирования**: Процесс выбора мест и подтверждения.
- **Технологии**:
  - **Next.js**: Фреймворк для React с поддержкой SSR.
  - **UI-библиотеки**: Material-UI, Ant Design или Chakra UI.
- **Аутентификация**:
  - Хранение JWT-токена в httpOnly cookies для безопасности.
  - Использование контекста или Redux для управления состоянием.
- **Взаимодействие с бэкендом**:
  - Все API-запросы проходят через `Gateway Service`.
  - Обработка ошибок и уведомлений на фронтенде.

---

## **Будущие планы и улучшения**

- **Оркестрация с помощью Kubernetes**:
  - Развёртывание микросервисов в кластере Kubernetes для повышения отказоустойчивости и масштабируемости.
- **Внедрение CI/CD**:
  - Настройка непрерывной интеграции и доставки с использованием GitHub Actions или GitLab CI/CD.
- **Улучшение безопасности**:
  - Реализация двухфакторной аутентификации (2FA).
  - Проведение аудита безопасности.
- **Оптимизация производительности**:
  - Внедрение кэширования с помощью Redis.
  - Оптимизация запросов к базам данных.
- **Расширение функциональности**:
  - Добавление поддержки международных платежей.
  - Интеграция с социальными сетями для входа и распространения информации о мероприятиях.
- **Мобильное приложение**:
  - Разработка мобильного приложения на React Native или Flutter.

---

## **Заключение**

**Event Booking Platform** — это масштабируемый и функциональный проект, который объединяет современные технологии и подходы для создания удобной платформы по организации и бронированию мероприятий. Благодаря микросервисной архитектуре, каждый компонент системы может развиваться и масштабироваться независимо, обеспечивая гибкость и устойчивость всего приложения.

