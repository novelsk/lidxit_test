# leadhit.ru - тестовое задание

### Запуск
Запустить docker-compose.yaml
```bash
docker-compose up -d
```
Перейти в /src
```bash
cd ./src
```
Создать venv c python 3.11 и установить requirements
```bash
.venv/Scripts/activate # для linux: source .venv/Scripts/activate
pip install -r requirements.txt
```
Создать .env файл
```bash
# Шаблон .env файла:
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example
MONGO_DB_URI=mongodb://root:example@localhost:27017/
```
Заполнить БД данными
```bash
python scripts/generate_data.py # Опционально можно обновить тестовые данные
python scripts/fill_data.py
```
Запустить
```bash
uvicorn app.main:app
```
Тестовый скрипт
```bash
python scripts/tests_requests.py
```
### [Swagger](http://127.0.0.1:8000/docs)
