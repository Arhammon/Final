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
headers = {"content-type": "application/json", "accept": "application/json"}
###### Блок текстовых переменных Allure
allure_str = {
    "epic": "Новая профессия",
    "feature": 'Курс повышения квалификации "Специалист по тестированию"',
    "story": "Итоговая работа",
    "postz": "Отправка POST запроса",
    "putz": "Отправка PUT запроса",
    "getz": "Отправка GET запроса",
}
###### Блок переменных
###### Документация
###### Блок импорта библиотек
import pprint
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
    jpost = jdata  # создание копии массива для дальнейшей замены ИД на 0, как если бы присвоение корректно работало !!!!!!! питон не умеет копировать это получилась ссылка!!!!
    jpostfix = jpost["id"] # Временный фикс !!!!
    jpost["id"] = 0

    with allure.step(allure_str["postz"]):
        respost = requests.post(url=url, json=jpost)
        jpost["id"] = jpostfix # Временный фикс !!!!
        assert 200 == respost.status_code


@allure.title("Функция создания питомца (PUT/pet)")
@allure.description(f"Проверка на код ответа операции PUT/pet по адресу {url}")
@allure.epic(allure_str["epic"])
@allure.feature(allure_str["feature"])
@allure.story(allure_str["story"])
def test_put_pet_id():
    with allure.step(allure_str["putz"]):
        respost = requests.put(url=url, json=jdata, headers=headers)
        resp = respost.json()
    with allure.step("Проверка кода ответа"):
        assert 200 == respost.status_code
    with allure.step("Проверка соответствия ИД"):   
        assert jdata["id"] == resp["id"]

@allure.title("Функция получения питомца (GET/pet)")
@allure.description(f"Проверка на код ответа операции GET/pet по адресу {url}")
@allure.epic(allure_str["epic"])
@allure.feature(allure_str["feature"])
@allure.story(allure_str["story"])
def test_get_pet_id():
    with allure.step(allure_str["getz"]):
        cUrl = url + str(petid) #собирание адреса путем добавления ИД
        print(cUrl) # Дебаг
        resp = requests.get(cUrl)
    with allure.step("Проверка кода ответа"):
        assert 200 == resp.status_code
    with allure.step("Проверка соответствия ИД"):  
        resp = resp.json() # преобразование в Json  перед сравнением
        assert jdata["id"] == resp["id"]


@allure.title("Функция удаления питомца (DELETE/pet)")
@allure.description(f"Проверка на код ответа операции GET/pet по адресу {url}")
@allure.epic(allure_str["epic"])
@allure.feature(allure_str["feature"])
@allure.story(allure_str["story"])
def test_del_pet_id():
    with allure.step(allure_str["getz"]):
        cUrl = url + str(petid) #собирание адреса путем добавления ИД
        print(cUrl) # Дебаг
        resp = requests.delete(cUrl)
    with allure.step("Проверка кода ответа"):
        assert 200 == resp.status_code

@allure.title("Функция создания питомца (POST/pet) Негативное тестирование")
@allure.description(f"Проверка на код ответа операции POST/pet по адресу {url}")
@allure.epic(allure_str["epic"])
@allure.feature(allure_str["feature"])
@allure.story(allure_str["story"])
def test_postN_pet():
    jpost = jdata  # создание копии массива для дальнейшей замены ИД на 0, как если бы присвоение корректно работало !!!!!!! питон не умеет копировать это получилась ссылка!!!!
    jpostfix = jpost["id"] # Временный фикс !!!!
    jpost["id"] = "error" # привносим ошибку

    with allure.step(allure_str["postz"]):
        respost = requests.post(url=url, json=jpost)
        jpost["id"] = jpostfix # Временный фикс !!!!
        assert 500 == respost.status_code #сервер не может обработать запрос со строкой вместо ожидаемого инт