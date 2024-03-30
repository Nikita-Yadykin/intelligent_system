# # data_processing.py
#
# import pandas as pd
# import mysql.connector
#
# def load_data_from_database():
#     # Подключение к базе данных
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="test"
#     )
#
#     # Загрузите данные из таблицы ML_table
#     data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)
#     return data_ml_table

# # ИНТЕРФЕЙС !!!

import pandas as pd
import mysql.connector

def load_data_from_database():
    # Подключение к базе данных
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )

    # Загрузите данные из таблицы ML_table
    data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)
    return data_ml_table
