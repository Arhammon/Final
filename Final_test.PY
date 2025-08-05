###### Документация и импорт расположены после блока переменных

###### Блок параметрических переменных
petid = 123457
jdata = {
    "id": petid,
    "category": {"id": 1, "name": "Dogs"},
    "name": "Angel",
    "photoUrls": ["http://ph.to/url.jpg"],
    "tags": [{"id": 3412, "name": "Shepherd"}],
    "status": "sold",
}
url = "https://petstore.swagger.io/v2/pet/"
###### Блок текстовых переменных Allure
allure_str = {
    "epic": "Новая профессия",
    "feature": 'Курс повышения квалификации "Специалист по тестированию"',
    "story": "Итоговая работа",
    "postz": "Отправка POST запроса",
}
###### Блок переменных
###### Документация
###### Блок импорта библиотек
import allure
import requests


###### Блок вспомогательных функции
#### Вспомогательная функция для очистки результатов
def delete_files_in_folder(folder_path):
    import os

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Ошибка при удалении файла {file_path}. {e}")


delete_files_in_folder("allure-result")


###### Блок тестов
@allure.title("Функция создания питомца (POST/pet)")
@allure.description(f"Проверка на код ответа операции POST/pet по адресу {url}")
@allure.epic(allure_str["epic"])
@allure.feature(allure_str["feature"])
@allure.story(allure_str["story"])
def test_post_pet():
    jpost = jdata  # создание копии массива для дальнейшей замены ИД на 0
    jpost["id"] = 0
    with allure.step(allure_str["postz"]):
        respost = requests.post(url, json=jpost)
        assert 200 == respost.status_code
