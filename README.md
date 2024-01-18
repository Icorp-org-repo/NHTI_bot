# Для запуска 
## На сервере
1. Установите зависимости (Модули, библиотеки)
```Bash
pip install aiogram==2.21
pip install aiohttp
pip install attrs==23.2.0
pip install Babel==2.9.1
pip install aiofiles==23.2.1
```
2. Создайте файл config.py и запишити
```python
BOT_TOKEN = 'YOUR_BOT_TOKEN'
```
3. Запустите Бота
```Bash
 # python or python3 
 python main.py
 ```
## Через Docker
1. Создайте файл config.py и запишити
```python
BOT_TOKEN = 'YOUR_BOT_TOKEN'
```
2. Соберите контейнеры
```Bash
docker compose up
```
