# Используем официальный образ Python в качестве базового
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда для запуска бота
CMD ["python", "-m", "bot.main"]
