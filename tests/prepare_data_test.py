from unittest import TestCase, main
from data_processing import prepare_data


# Фиктивный класс для чекбокса
class FakeCheckBox:
    def __init__(self, checked=False):
        self._checked = checked

    def isChecked(self):
        return self._checked


class PrepareDataTest(TestCase):
    def test_prepare_data_user_input_length(self):  # Проверить, что масссив имеет длину 13
        # Создаем фиктивный интерфейс
        class FakeUI:
            def __init__(self):
                self.checkBox = FakeCheckBox()  # Инициализация checkBox экземпляром FakeCheckBox
                for i in range(1, 41):
                    setattr(self, f"checkBox_{i}", FakeCheckBox())  # Инициализация остальных checkBox_* атрибутов

        # Создаем экземпляр фиктивного интерфейса
        fake_ui = FakeUI()

        # Получаем данные
        data, _ = prepare_data(fake_ui)

        # Получаем user_input
        user_input = data.iloc[0].tolist()

        # Проверяем, что user_input содержит массив из 13 интов
        self.assertEqual(len(user_input), 13)

    def test_prepare_data_user_input_int(self):  # Проверить что все элементы в массиве инты
        # Создаем фиктивный интерфейс
        class FakeUI:
            def __init__(self):
                self.checkBox = FakeCheckBox()  # Инициализация checkBox экземпляром FakeCheckBox
                for i in range(1, 41):
                    setattr(self, f"checkBox_{i}", FakeCheckBox())  # Инициализация остальных checkBox_* атрибутов

        # Создаем экземпляр фиктивного интерфейса
        fake_ui = FakeUI()

        # Получаем данные
        data, _ = prepare_data(fake_ui)

        # Получаем user_input
        user_input = data.iloc[0].tolist()

        # Проверяем, что user_input содержит массив из 13 интов
        for value in user_input:
            self.assertIsInstance(value, int)

    def test_prepare_data_invalid_interface(self):  # проверить только сообщение об ошибке без учета типа исключения
        # Создаем фиктивный интерфейс с None
        fake_ui = None

        # Пытаемся вызвать функцию prepare_data с некорректным интерфейсом
        with self.assertRaises(AttributeError) as context:
            prepare_data(fake_ui)

        # Получаем текст исключения
        exception_message = str(context.exception)

        # Проверяем, что полученное исключение содержит указанное сообщение
        self.assertIn("has no attribute 'checkBox'", exception_message)


if __name__ == '__main__':
    main()
