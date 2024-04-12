# data_processing.py
import mysql.connector
import pandas as pd
from interface import get_user_input

def prepare_data(ui):
    user_input = get_user_input(ui)
    data = pd.DataFrame([user_input],
                        columns=['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3'])

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )

    data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)

    return data, data_ml_table
