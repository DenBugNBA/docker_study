1. Создаем volume для хранения данных в CSV
```bash
docker volume create tg_result
```

2. Собираем образ
```bash
docker build -t tg_bot .
```

3. Создаем env с токеном Telegram бота
```bash
export APP_TOKEN=<token>
```

4. Поднимаем контейнер с volume и токеном 
```bash
docker run --rm -v tg_result:/app/todo_result -e APP_TOKEN=$APP_TOKEN --name tg_bot_container tg_bot
```

5. Копируем в контейнер директорию с CSV
```bash
docker cp ./todo_result tg_bot_container:/app
```
