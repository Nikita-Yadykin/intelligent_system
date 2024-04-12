import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_Widget
from interface import update_result_label, get_user_input  # Импорт функции get_user_input
from data_processing import prepare_data
from machine_learning import train_and_predict

class YourMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_risk)

    def calculate_risk(self):
        try:
            data, data_ml_table = prepare_data(self.ui)

            # Получение ввода пользователя
            user_input = get_user_input(self.ui)

            # Предсказание и анализ риска
            prediction, total_sum, y_test, y_pred = train_and_predict(data_ml_table, data, user_input)

            update_result_label(self.ui, prediction, total_sum, y_test, y_pred)

        except Exception as e:
            self.ui.label_70.setText(f"Ошибка: {e}")

def main():
    app = QApplication(sys.argv)
    window = YourMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
