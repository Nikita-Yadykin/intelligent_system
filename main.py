# main.py
# Импортируем модуль sys для работы с системными параметрами и путями
import sys
# Импортируем класс QApplication и QMainWindow из модуля PySide6.QtWidgets для создания графического интерфейса
from PySide6.QtWidgets import QApplication, QMainWindow
# Импортируем класс Ui_Widget из модуля ui_form для использования графического интерфейса, созданного в Qt Designer
from ui_form import Ui_Widget
# Импортируем функции update_result_label и get_user_input из модуля interface для работы с интерфейсом
from interface import update_result_label, get_user_input
# Импортируем функцию prepare_data из модуля data_processing для обработки данных
from data_processing import prepare_data
# Импортируем функцию train_and_predict из модуля machine_learning для обучения и предсказания результатов машинного обучения
from machine_learning import train_and_predict


# Определение класса YourMainWindow, который наследует функциональность класса QMainWindow
class YourMainWindow(QMainWindow):
    # Определение конструктора класса YourMainWindow
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        # Создание экземпляра класса Ui_Widget, который содержит описание интерфейса
        self.ui = Ui_Widget()
        # Настройка графического интерфейса с использованием метода setupUi
        self.ui.setupUi(self)
        # Подключение обработчика события нажатия кнопки к методу calculate_risk
        self.ui.pushButton.clicked.connect(self.calculate_risk)

    # Метод для расчета риска при нажатии кнопки
    def calculate_risk(self):
        try:
            # Подготовка данных для анализа
            data, data_ml_table = prepare_data(self.ui)

            # Получение ввода пользователя
            user_input = get_user_input(self.ui)

            # Проведение обучения и предсказания с использованием машинного обучения
            prediction, total_sum, y_test, y_pred = train_and_predict(data_ml_table, data, user_input)

            # Обновление меток результатов на графическом интерфейсе
            update_result_label(self.ui, prediction, total_sum, y_test, y_pred)

        except Exception as e:
            # Вывод сообщения об ошибке на графический интерфейс
            self.ui.label_70.setText(f"Ошибка: {e}")


# Определение функции main, которая является точкой входа в приложение
def main():
    # Создание экземпляра приложения QApplication
    app = QApplication(sys.argv)
    # Создание экземпляра главного окна
    window = YourMainWindow()
    # Отображение главного окна
    window.show()
    # Запуск главного цикла обработки событий приложения
    sys.exit(app.exec())


# Проверка, является ли файл main.py основным файлом для запуска
if __name__ == '__main__':
    # Вызов функции main
    main()
