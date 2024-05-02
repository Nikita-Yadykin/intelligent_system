# interface.py
# pyside6-uic form.ui -o ui_form.py
from sklearn.metrics import classification_report, confusion_matrix
import random  # Импортируем модуль random для случайного выбора рекомендаций
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
def update_result_label(ui, prediction, total_sum, y_test, y_pred, user_input):
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
        if user_input == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]:  # Проверка, что user_input полностью заполнен нулями
            result_text = "Пожалуйста, заполните информацию об уязвимостях, информационных ресурсах и угрозах."  # Сообщение для вывода на метке

        elif user_input[:6] == [0, 0, 0, 0, 0, 0] and  user_input[6:10] == [0, 1, 1, 1]:
            result_text = "Пожалуйста, заполните информацию об уязвимостях и угрозах."  # Сообщение для вывода на метке
        elif user_input[:6] == [0, 0, 0, 0, 0, 0] and user_input[10:] == [0, 0, 0]:
            result_text = "Пожалуйста, заполните информацию об уязвимостях и информационных ресурсах."  # Сообщение для вывода на метке
        elif user_input[6:10] == [0, 1, 1, 1] and user_input[10:] == [0, 0, 0]:
            result_text = "Пожалуйста, заполните информацию об угрозах и информационных ресурсах."  # Сообщение для вывода на метке
        elif user_input[6:10] == [0, 1, 1, 1] and user_input[:6] == [0, 0, 0, 0, 0, 0]:
            result_text = "Пожалуйста, заполните информацию об угрозах и уязвимостях."  # Сообщение для вывода на метке

        elif user_input[:6] == [0, 0, 0, 0, 0, 0]:
             result_text = "Пожалуйста, заполните информацию об уязвимостях."  # Сообщение для вывода на метке
        elif user_input[6:10] == [0, 1, 1, 1]:
            result_text = "Пожалуйста, заполните информацию об угрозах."  # Сообщение для вывода на метке
        elif user_input[10:] == [0, 0, 0]:
            result_text = "Пожалуйста, заполните информацию об информационных ресурсах."  # Сообщение для вывода на метке
        elif user_input[10:] == [0, 0, 0]:

            result_text = "Пожалуйста, заполните информацию об информационных ресурсах."  # Сообщение для вывода на метке

        else:
            # Формирование строки с результатами
            result_text = f"Уровень риска: {prediction}\n "
            # Список общих рекомендаций
            recommendations = [
                "Регулярно обновляйте программное обеспечение и системные компоненты.",
                "Установите и поддерживайте антивирусное программное обеспечение.",
                "Внедрите механизм резервного копирования данных и регулярно проверяйте его работоспособность.",
                "Внедрите политику безопасности доступа к информационным ресурсам с учетом принципа наименьших привилегий.",
                "Проведите аудит информационной системы на наличие уязвимостей и исправьте их.",
                "Регулярно проводите обучение сотрудников по вопросам информационной безопасности."
            ]
            # Определение числа рекомендаций в зависимости от уровня риска
            num_recommendations = {
                "Низкий": 1,
                "Средний": 2,
                "Высокий": 3,
                "Критический": 4
            }

            # Получение случайных рекомендаций из списка
            selected_recommendations = random.sample(recommendations, num_recommendations.get(prediction, 1))

            # Проверяем, что уровень риска указан и выбираем описание в соответствии с ним
            if prediction:
                risk_descriptions = {
                    "Низкий": "Этот уровень риска указывает на незначительные потенциальные угрозы без серьезных последствий для организации. Вероятность негативных событий на этом уровне невелика.",
                    "Средний": "Уровень риска, требующий некоторых мер предосторожности. Возможны небольшие негативные последствия, но они могут быть управляемыми при правильном вмешательстве.",
                    "Высокий": "Этот уровень риска указывает на серьезные потенциальные угрозы для организации, которые могут привести к значительным негативным последствиям. Требуются срочные меры для снижения риска и защиты активов.",
                    "Критический": "Самый высокий уровень риска, который указывает на катастрофические последствия для организации. Этот уровень риска требует немедленного и наиболее серьезного вмешательства для минимизации ущерба и восстановления нормальной деятельности."
                }
                result_text += risk_descriptions.get(prediction, "") + "\n\n"

        if "Уровень риска" in result_text:
            result_text += "Рекомендации:\n" + "\n".join(selected_recommendations)


        # Установка текста метки с результатом
        ui.label_70.setText(result_text)
        # Обработка исключений
    except Exception as e:
        # Установка текста метки с сообщением об ошибке
        ui.label_70.setText(f"Ошибка: {e}")