# interface.py
# pyside6-uic form.ui -o ui_form.py
from sklearn.metrics import classification_report, confusion_matrix

# Определение функции get_user_input, которая получает ввод пользователя
# и кодирует его в массив значений
def get_user_input(ui):
    # Словарь для сопоставления флажков с их значениями
    checkbox_encodings = {
        "class_vulnerability": {
            ui.checkBox: 1,
            ui.checkBox_2: 2,
            ui.checkBox_3: 3
        },
        "cvss_level": {
            ui.checkBox_4: 1,
            ui.checkBox_5: 2,
            ui.checkBox_6: 3,
            ui.checkBox_7: 4
        },
        "vulnerability_status": {
            ui.checkBox_8: 1,
            ui.checkBox_9: 2,
            ui.checkBox_10: 3
        },
        "exploit_presence": {
            ui.checkBox_11: 1,
            ui.checkBox_12: 2,
            ui.checkBox_13: 3
        },
        "fix_info": {
            ui.checkBox_14: 1,
            ui.checkBox_15: 2
        },
        "incident_relation": {
            ui.checkBox_16: 1,
            ui.checkBox_17: 2
        },
        "threat_source": {
            ui.checkBox_18: 1,
            ui.checkBox_19: 2,
            ui.checkBox_20: 3,
            ui.checkBox_21: 4,
            ui.checkBox_22: 5,
            ui.checkBox_23: 6
        },
        "confidentiality_violation": {
            ui.checkBox_24: 2 if ui.checkBox_24.isChecked() else 1
        },
        "integrity_violation": {
            ui.checkBox_25: 2 if ui.checkBox_25.isChecked() else 1
        },
        "availability_violation": {
            ui.checkBox_26: 2 if ui.checkBox_26.isChecked() else 1,
        },
        "resource_type": {
            ui.checkBox_27: 1,
            ui.checkBox_28: 2,
            ui.checkBox_29: 3,
            ui.checkBox_30: 4,
            ui.checkBox_31: 5
        },
        "resource_cost": {
            ui.checkBox_32: 1,
            ui.checkBox_33: 2,
            ui.checkBox_34: 3,
            ui.checkBox_35: 4
        },
        "resource_storage_location": {
            ui.checkBox_36: 1,
            ui.checkBox_37: 2,
            ui.checkBox_38: 3,
            ui.checkBox_39: 4,
            ui.checkBox_40: 5,
        }
    }
    # Создание пустого списка для хранения ввода пользователя
    user_input = []

    # Итерация по группам флажков
    for group_name, checkbox_map in checkbox_encodings.items():
        max_value = 0 # Инициализация переменной для максимального значения

        # Итерация по флажкам в текущей группе
        for checkbox, value in checkbox_map.items():
            if checkbox.isChecked(): # Проверка, выбран ли флажок
                max_value = max(max_value, value)  # Обновление максимального значения

        # Обработка особых случаев для некоторых групп
        if group_name in ["confidentiality_violation", "integrity_violation", "availability_violation"]:
            user_input.append(max_value if max_value > 0 else 1)   # Добавление максимального значения в список
        else:
            user_input.append(max_value)  # Добавление максимального значения в список (0, если флажки не выбраны)

    return user_input

# Определение функции update_result_label, которая обновляет метку с результатом
def update_result_label(ui, prediction, total_sum, y_test, y_pred):
    try:
        # if 13 <= total_sum <= 20:
        #     risk_level = "Низкий"
        # elif 21 <= total_sum <= 28:
        #     risk_level = "Средний"
        # elif 29 <= total_sum <= 36:
        #     risk_level = "Высокий"
        # elif 37 <= total_sum <= 43:
        #     risk_level = "Критический"
        # else:
        #     risk_level = "Проверьте правильность ввода"

        # result_text = (f"Уровень риска: {prediction}\n"
        #                f"\nСумма всех цифр: {total_sum} {risk_level}\n"
        #                f"\nОтчет о классификации:\n{classification_report(y_test, y_pred)}\n"
        #                f"Матрица ошибок:\n{str(confusion_matrix(y_test, y_pred))}")
        # Формирование строки с результатами
        result_text = f"Уровень риска: {prediction}\n"
        # Установка текста метки с результатом
        ui.label_70.setText(result_text)
        # Обработка исключений
    except Exception as e:
        # Установка текста метки с сообщением об ошибке
        ui.label_70.setText(f"Ошибка: {e}")
