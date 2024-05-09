from unittest import TestCase, main
from unittest.mock import patch
from data_processing import prepare_data
import pandas as pd
from interface import get_user_input

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
                setattr(self, f"checkBox_{i}", FakeCheckBox(checked=bool(value)))  # Инициализация остальных checkBox_* атрибутов
        setattr(self, "checkBox_2", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_3", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_4", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_5", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_6", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_7", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_8", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_9", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_10", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_11", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_12", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_13", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_14", FakeCheckBox(checked=bool(1)))
        setattr(self, "checkBox_15", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_16", FakeCheckBox(checked=bool(0)))  # Инициализация атрибута checkBox_16
        setattr(self, "checkBox_17", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_18", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_19", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_20", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_21", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_22", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_23", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_24", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_25", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_26", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_27", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_28", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_29", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_30", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_31", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_32", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_33", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_34", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_35", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_36", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_37", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_38", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_39", FakeCheckBox(checked=bool(0)))
        setattr(self, "checkBox_40", FakeCheckBox(checked=bool(0)))



class CalculateRiskTest(TestCase):

    def test_get_user_input_positive(self):
        # Создаем фиктивный объект ui с установленными значениями для всех флажков
        class MockUi:
            pass

        ui = FakeUI([3, 4, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 0])


        # Вызываем функцию get_user_input и проверяем результат
        user_input = get_user_input(ui)
        expected_result = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
        self.assertEqual(user_input, expected_result)

    def test_get_user_input_negative(self):
        # Создаем фиктивный объект ui без выбранных флажков
        class MockUi:
            pass

        ui = FakeUI([3, 2, 3, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0])


        # Вызываем функцию get_user_input и проверяем результат
        user_input = get_user_input(ui)
        expected_result = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
        self.assertEqual(user_input, expected_result)

class MainTest(TestCase):
    #class MainTest(TestCase):

    def test_prepare_data_positive(self):
        # Создаем фиктивный объект ui и user_input
        ui = FakeUI()  # Use FakeUI instead of MockUi
        user_input = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]

        # Вызываем функцию prepare_data и проверяем результат
        data, data_ml_table = prepare_data(ui)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(list(data.columns),
                         ['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3'])
        self.assertEqual(list(data.values[0]), user_input)

    @patch('data_processing.mysql.connector.connect')
    def test_prepare_data_negative(self, mock_connect):
        # Мокируем ошибку подключения к базе данных
        mock_connect.side_effect = Exception("Ошибка подключения к базе данных")

        # Создаем фиктивный объект ui и user_input
        class MockUi:
            pass

        ui = MockUi()


        # Проверяем, что при возникновении исключения функция
        # prepare_data завершается с ошибкой
        with self.assertRaises(Exception):
            prepare_data(ui)

if __name__ == '__main__':
    main()
