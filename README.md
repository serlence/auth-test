# Auth Service

## Технологии

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy 
- JWT 
- bcrypt для хеширования паролей
- Docker Compose


### POST `/api/auth/register`
Регистрация нового пользователя
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "password123"
}
```

### POST `/api/auth/login`
Вход в систему
```json
{
  "username": "username",
  "password": "password123"
}
```

### GET `/api/auth/me`
Получение информации о текущем пользователе

### POST `/api/auth/logout`
Выход из системы

## Запуск=

1. Клонируйте репозиторий
2. Запустите проект:
```bash 
docker-compose up --build
```

## Переменные окружения

- `DATABASE_URL` - URL подключения к PostgreSQL
- `SECRET_KEY` - Секретный ключ для JWT токенов


