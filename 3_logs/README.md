```bash
docker build -t logs_ex .
```

```bash
docker run --rm --name file logs_ex file
```

```bash
docker run -d --rm --name console logs_ex console
```
 
Смотреть логи контейнера:
```bash
docker logs -f console
```
