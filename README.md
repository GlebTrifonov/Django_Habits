# Habit Tracker | Django + DRF

Минималистичный трекер привычек с полноценным веб-интерфейсом и защищенным API. Проект построен по принципу разделения монолитной логики и REST-архитектуры.

![Python](https://img.shields.io)
![Django](https://img.shields.io)
![DRF](https://img.shields.io)
![JWT](https://img.shields.io)

---

## Основные возможности

### Веб-интерфейс (Monolith)
- **Авторизация:** Регистрация, вход и выход пользователей.
- **Персонализация:** Каждый пользователь видит и управляет только своими привычками.
- **CRUD:** Создание, просмотр списка, переключение статуса (выполнено/нет) и удаление.

### API (Django REST Framework)
- **JSON Эндпоинты:** Полный набор API для интеграции с мобильными или фронтенд-приложениями.
- **Security:** Доступ только для авторизованных пользователей через `IsAuthenticated`.
- **JWT Auth:** Поддержка JSON Web Tokens (Access & Refresh tokens).
- **Browsable API:** Удобный графический интерфейс для тестирования запросов.

---

## Технологический стек

*   **Backend:** Python, Django
*   **API:** Django REST Framework, SimpleJWT
*   **Database:** SQLite (локально)

---

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com
   cd Django_Habits

2. **Создайте и активируйте виртуальное окружение**
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows

3. **Установите зависимости**
pip install django djangorestframework djangorestframework-simplejwt

4. **Примените миграции и создайте админа**
python manage.py migrate
python manage.py createsuperuser

5. **Запустите сервер**
python manage.py runserver


