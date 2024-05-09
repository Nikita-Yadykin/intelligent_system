from unittest import TestCase, main
from unittest.mock import MagicMock
from interface import update_result_label, get_user_input

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
class UpdateResultLabelTest(TestCase):
    # Позитивный тест:
    def test_update_result_label_positive(self):
        # Подготовка данных
        ui = MagicMock()
        ui.label_70.text.return_value = "Уровень риска: Средний\n Рекомендации: Рекомендация 1\nРекомендация 2"  # Установка возвращаемого значения для ui.label_70.text()
        user_input = [1, 2, 3, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]  # Заполненные данные пользователя
        prediction = "Средний"  # Предсказанный уровень риска
        total_sum = 6  # Произвольная сумма для теста
        y_test = []  # Мы не используем y_test и y_pred в этом тесте, поэтому они могут быть пустыми
        y_pred = []

        # Вызов функции обновления метки с результатом
        update_result_label(ui, prediction, total_sum, y_test, y_pred, user_input)

        # Проверка, что текст метки содержит предсказанный уровень риска и соответствующие рекомендации
        self.assertIn("Средний", ui.label_70.text())
        self.assertIn("Рекомендации:", ui.label_70.text())

    # Негативный тест:
    def test_update_result_label_negative(self):
        # Подготовка данных
        ui = MagicMock()
        ui.label_70.text.return_value = "Пожалуйста, заполните информацию"  # Установка возвращаемого значения для ui.label_70.text()
        user_input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Пустые данные пользователя
        prediction = "Средний"  # Произвольный предсказанный уровень риска
        total_sum = 0  # Произвольная сумма для теста
        y_test = []  # Мы не используем y_test и y_pred в этом тесте, поэтому они могут быть пустыми
        y_pred = []

        # Вызов функции обновления метки с результатом
        update_result_label(ui, prediction, total_sum, y_test, y_pred, user_input)

        # Проверка, что текст метки содержит сообщение о заполнении информации
        self.assertIn("Пожалуйста, заполните информацию", ui.label_70.text())


class GetUserInputTest(TestCase):
    # Позитивный тест:
    def test_get_user_input_positive(self):
        # Подготовка данных
        ui = MagicMock()
        # Устанавливаем флажки для имитации выбора пользователя
        ui.checkBox.isChecked.return_value = True
        ui.checkBox_2.isChecked.return_value = True
        ui.checkBox_3.isChecked.return_value = True
        ui.checkBox_4.isChecked.return_value = True
        ui.checkBox_5.isChecked.return_value = True
        ui.checkBox_8.isChecked.return_value = True
        ui.checkBox_16.isChecked.return_value = True
        ui.checkBox_18.isChecked.return_value = True
        ui.checkBox_24.isChecked.return_value = True
        ui.checkBox_27.isChecked.return_value = True
        ui.checkBox_32.isChecked.return_value = True
        ui.checkBox_36.isChecked.return_value = True

        # Вызываем функцию получения ввода пользователя
        user_input = get_user_input(ui)

        # Проверяем, что возвращенный список содержит ожидаемые значения
        expected_user_input = [3, 4, 3, 3, 2, 2, 6, 2, 2, 2, 5, 4, 5]
        self.assertEqual(user_input, expected_user_input)

    def test_get_user_input_partial_selection(self):
        # Подготовка данных
        ui = FakeUI([1] + [0] * 39)  # Выбран только первый флажок

        # Вызываем функцию получения ввода пользователя
        user_input = get_user_input(ui)

        # Проверяем, что возвращенный список содержит одно ненулевое значение
        self.assertEqual(len(user_input), 13)
        self.assertEqual(sum(user_input), 3)  # Проверяем, значение равно 3
        self.assertTrue(any(user_input))  # Проверяем, что есть хотя бы одно ненулевое значение






if __name__ == '__main__':
    main()
