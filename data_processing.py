# data_processing.py
# Импорт необходимых библиотек
import mysql.connector  # Импорт библиотеки для работы с MySQL
import pandas as pd  # Импорт библиотеки pandas для работы с данными
from interface import get_user_input  # Импорт функции get_user_input из модуля interface

# Определение функции prepare_data, которая подготавливает данные для анализа
def prepare_data(ui):
    # Получение ввода пользователя с помощью функции get_user_input
    user_input = get_user_input(ui)

    # Создание DataFrame из введенных пользователем данных
    data = pd.DataFrame([user_input],
                        columns=['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3'])

    # Установление соединения с базой данных MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )

    # Выполнение запроса к базе данных и чтение данных в DataFrame
    data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)

    # Возврат подготовленных данных и данных из базы данных
    return data, data_ml_table
