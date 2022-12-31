import pandas as pd
import json
from openpyxl import Workbook

csv_file = pd.read_csv('skills.csv')                    # Чтение исходного файла

new_book = Workbook()                                   # Создание объекта табоицы
new_book_sheet = new_book.active                        # Создание объекта листа
new_book_sheet.append(['cvName', 'skills'])             # Создание колонок

for line in csv_file.values:                            # Чтение csv по строкам
    position = line[0]                                  # Получение первого значения csv как должности
    data = line[1]                                      # Получение втого значения как строки json
    json_data = json.loads(data)                        # Преобразование строки в json

    data_to_excel = [position]                          # Создание массива для удобной передачи

    for skill in json_data['Стэк']:                     # Проходим по всем значенения коллекции Стэк
        data_to_excel.append(skill['Name'])             # Заполнение массива необходимыми данными

    new_book_sheet.append(data_to_excel)                # Обновление данных в файле Excel по строчно

new_book.save(filename='new.xlsx')                      # Сохранение объекта таблицы с указанием имени