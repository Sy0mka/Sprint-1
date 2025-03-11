# Проект "Федерация Спортивного Туризма России" (ФСТР)

REST API для управления данными о горных перевалах с системой модерации.

## 📌 Оглавление
- [Возможности API](#-возможности-api)
- [Технологии](#-технологии)
- [Установка](#-установка)
- [Использование API](#-использование-api)
- [Документация](#-документация)
- [Деплой](#-деплой)
- [Тестирование](#-тестирование)
- [Структура проекта](#-структура-проекта)
- [Разработчики](#-разработчики)

## 🚀 Возможности API
- **Добавление новых перевалов** с автоматическим статусом "new"
- **Модерация записей** (статусы: pending, accepted, rejected)
- **Редактирование записей** в статусе "new"
- **Фильтрация по email пользователя**
- **Автоматическая документация** через Swagger UI
- **Docker-развертывание**

## 💻 Технологии
- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker
- Swagger

## 📥 Установка

### Требования
- Python 3.9+
- PostgreSQL 13+
- Docker (опционально)

### Локальная настройка
1. Клонировать репозиторий:
```bash
git clone https://github.com/Sy0mka/fstr-project.git
cd fstr-project
