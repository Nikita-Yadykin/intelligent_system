import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_Widget
import mysql.connector
import pandas as pd
from interface import get_user_input, update_result_label
from machine_learning import train_and_predict

class YourMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_risk)

    def calculate_risk(self):
        try:
            user_input = get_user_input(self.ui)
            data = pd.DataFrame([user_input],
                                columns=['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3'])

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="test"
            )

            data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)

            prediction, total_sum, y_test, y_pred = train_and_predict(data_ml_table, data, user_input)

            if 13 <= total_sum <= 20:
                risk_level = "Низкий"
            elif 21 <= total_sum <= 28:
                risk_level = "Средний"
            elif 29 <= total_sum <= 36:
                risk_level = "Высокий"
            elif 37 <= total_sum <= 43:
                risk_level = "Критический"
            else:
                risk_level = "Проверьте правильность ввода"

            update_result_label(self.ui, prediction, total_sum, risk_level, y_test, y_pred)

        except Exception as e:
            self.ui.label_70.setText(f"Ошибка: {e}")


def main():
    app = QApplication(sys.argv)
    window = YourMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
