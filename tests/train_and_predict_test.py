import mysql.connector
import pandas as pd
from unittest import TestCase, main
from machine_learning import train_and_predict
from data_processing import prepare_data

class TestTrainAndPredict(TestCase):
    def test_train_and_predict_positive(self):
        # Создаем тестовый ввод пользователя, где все флажки отмечены
        user_input = [1] * 40

        # Подготовка данных из базы данных с использованием фиктивного интерфейса
        data, data_ml_table_train = prepare_data(FakeUI(user_input))

        # Выполняем функцию train_and_predict
        prediction, total_sum, y_test, y_pred = train_and_predict(data_ml_table_train, data, user_input)

        # Проверяем, что предсказание прошло успешно
        self.assertEqual(prediction, 'Критический')

    def test_train_and_predict_negative(self):
        # Передаем некорректные данные для обучения (None)
        X_train = None
        y_train = None

        # Передаем некорректные данные для предсказания (None)
        X_test = None

        # Пытаемся вызвать функцию train_and_predict с некорректными данными
        with self.assertRaises(Exception) as context:
            train_and_predict(X_train, y_train, X_test)

        # Проверяем, что полученное исключение соответствует ожидаемому
        self.assertEqual(str(context.exception), "'NoneType' object is not subscriptable")


class FakeCheckBox:
    def __init__(self, checked=False):
        self._checked = checked

    def isChecked(self):
        return self._checked


class FakeUI:
    def __init__(self, user_input=None):
        self.checkBox = FakeCheckBox()  # Инициализация checkBox экземпляром FakeCheckBox
        if user_input:
            for i, value in enumerate(user_input, start=1):
                setattr(self, f"checkBox_{i}",
                        FakeCheckBox(checked=bool(value)))  # Инициализация остальных checkBox_* атрибутов



if __name__ == '__main__':
    main()
