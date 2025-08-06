### Подготовка окружения к работе
```
python -m venv .venv
.venv\Scripts\activate
pip install requests
pip install Pytest
pip install allure-pytest
```
#### Команды запуска тестов и генерации отчетности
```
pytest --alluredir allure-result
allure serve .\allure-result\
```

# Если ломается пайтест переименовать *.PY в *.py