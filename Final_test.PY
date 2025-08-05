#### Документация
#### Блок параметрических переменных 
#### Блок текстовых переменных Allure
#### Блок параметрических переменных 
#### Блок импорта библиотек
#### Блок вспомогательных функции
## Вспомогательная функция для очистки результатов 
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
#### Блок тестов