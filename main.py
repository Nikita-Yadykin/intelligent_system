# # main.py
#
# from data_processing import load_data_from_database
# from interface import get_user_input, print_result
# from machine_learning import train_and_predict_model
#
#
# def main():
#     # Получение данных из базы данных
#     data_ml_table = load_data_from_database()
#
#     # Получение ввода от пользователя
#     user_input = get_user_input()
#
#     # Обучение модели и предсказание
#     model, prediction, X_test, y_test, y_pred = train_and_predict_model(data_ml_table, user_input)
#
#     # Вывод результатов
#     print_result(prediction, model, X_test, y_test, y_pred)
#
#
# if __name__ == "__main__":
#     main()
#
# # ИНТЕРФЕЙС !!!
# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QMessageBox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mysql.connector
from sklearn.metrics import classification_report, confusion_matrix


class RiskCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # ComboBoxes for vulnerability assessment
        class_vulnerability_options = {"Уязвимость кода": 1, "Уязвимость архитектуры": 2,
                                       "Уязвимость многофакторная": 3}
        cvss_options = {"Низкий уровень опасности": 1, "Средний уровень опасности": 2, "Высокий уровень опасности": 3,
                        "Критический уровень опасности": 4}
        vulnerability_status_options = {"Подтверждена производителем": 1, "Подтверждена в ходе исследований": 2,
                                        "Потенциальная уязвимость": 3}
        exploit_presence_options = {"Данные уточняются": 1, "Существует": 2, "Существует в открытом доступе": 3}
        elimination_information_options = {"Уязвимость устранена": 1, "Информация об устранении отсутствует": 2}
        incident_relation_options = {"Связь с инцидентами ИБ присутвует": 1, "Связь с инцидентами ИБ отсутствует": 2}
        threat_source_options = {"Внешний нарушитель с низким потенциалом": 1,
                                 "Внутренний нарушитель с низким потенциалом": 2,
                                 "Внешний нарушитель со средним потенциалом": 3,
                                 "Внутренний нарушитель со средним потенциалом": 4,
                                 "Внешний нарушитель с высоким потенциалом": 5,
                                 "Внутренний нарушитель с высоким потенциалом": 6}
        confidentiality_violation_options = {"Да": 1, "Нет": 2}
        integrity_violation_options = {"Да": 1, "Нет": 2}
        availability_violation_options = {"Да": 1, "Нет": 2}
        resource_type_options = {"Общедоступный": 1, "Конфиденциальный": 2}
        confidentiality_category_options = {f"Категория {i}": i for i in range(1, 17)}
        resource_cost_options = {"Недорогой ресурс": 1, "Среднестоимостной ресурс": 2, "Дорогостоящий ресурс": 3,
                                 "Эксклюзивный ресурс": 4}
        resource_storage_location_options = {f"Место хранения {i}": i for i in range(1, 11)}

        self.class_vulnerability_label = QLabel("Укажите вид уязвимости:")
        layout.addWidget(self.class_vulnerability_label)
        self.class_vulnerability_combobox = QComboBox()
        self.class_vulnerability_combobox.addItems(class_vulnerability_options.keys())
        layout.addWidget(self.class_vulnerability_combobox)

        self.cvss_options_label = QLabel("Укажите уровень опасности уязвимости:")
        layout.addWidget(self.cvss_options_label)
        self.cvss_options_combobox = QComboBox()
        self.cvss_options_combobox.addItems(cvss_options.keys())
        layout.addWidget(self.cvss_options_combobox)

        self.vulnerability_status_label = QLabel("Укажите статус уязвимости:")
        layout.addWidget(self.vulnerability_status_label)
        self.vulnerability_status_combobox = QComboBox()
        self.vulnerability_status_combobox.addItems(vulnerability_status_options.keys())
        layout.addWidget(self.vulnerability_status_combobox)

        self.exploit_presence_label = QLabel("Укажите наличие эксплойта:")
        layout.addWidget(self.exploit_presence_label)
        self.exploit_presence_combobox = QComboBox()
        self.exploit_presence_combobox.addItems(exploit_presence_options.keys())
        layout.addWidget(self.exploit_presence_combobox)

        self.fix_info_label = QLabel("Укажите информацию об устранении:")
        layout.addWidget(self.fix_info_label)
        self.fix_info_combobox = QComboBox()
        self.fix_info_combobox.addItems(elimination_information_options.keys())
        layout.addWidget(self.fix_info_combobox)

        self.incident_relation_label = QLabel("Укажите связь с инцидентами ИБ:")
        layout.addWidget(self.incident_relation_label)
        self.incident_relation_combobox = QComboBox()
        self.incident_relation_combobox.addItems(incident_relation_options.keys())
        layout.addWidget(self.incident_relation_combobox)

        self.threat_source_label = QLabel("Укажите источник угрозы:")
        layout.addWidget(self.threat_source_label)
        self.threat_source_combobox = QComboBox()
        self.threat_source_combobox.addItems(threat_source_options.keys())
        layout.addWidget(self.threat_source_combobox)

        self.confidentiality_violation_label = QLabel("Укажите нарушение конфиденциальности:")
        layout.addWidget(self.confidentiality_violation_label)
        self.confidentiality_violation_combobox = QComboBox()
        self.confidentiality_violation_combobox.addItems(confidentiality_violation_options.keys())
        layout.addWidget(self.confidentiality_violation_combobox)

        self.integrity_violation_label = QLabel("Укажите нарушение целостности:")
        layout.addWidget(self.integrity_violation_label)
        self.integrity_violation_combobox = QComboBox()
        self.integrity_violation_combobox.addItems(integrity_violation_options.keys())
        layout.addWidget(self.integrity_violation_combobox)

        self.availability_violation_label = QLabel("Укажите нарушение доступности:")
        layout.addWidget(self.availability_violation_label)
        self.availability_violation_combobox = QComboBox()
        self.availability_violation_combobox.addItems(availability_violation_options.keys())
        layout.addWidget(self.availability_violation_combobox)

        self.resource_type_label = QLabel("Укажите тип ресурса:")
        layout.addWidget(self.resource_type_label)
        self.resource_type_combobox = QComboBox()
        self.resource_type_combobox.addItems(resource_type_options.keys())
        layout.addWidget(self.resource_type_combobox)

        self.confidentiality_category_label = QLabel("Укажите категорию конфиденциальности:")
        layout.addWidget(self.confidentiality_category_label)
        self.confidentiality_category_combobox = QComboBox()
        self.confidentiality_category_combobox.addItems(confidentiality_category_options.keys())
        layout.addWidget(self.confidentiality_category_combobox)

        self.resource_cost_label = QLabel("Укажите стоимость ресурса:")
        layout.addWidget(self.resource_cost_label)
        self.resource_cost_combobox = QComboBox()
        self.resource_cost_combobox.addItems(resource_cost_options.keys())
        layout.addWidget(self.resource_cost_combobox)

        self.resource_storage_location_label = QLabel("Укажите место хранения ресурса:")
        layout.addWidget(self.resource_storage_location_label)
        self.resource_storage_location_combobox = QComboBox()
        self.resource_storage_location_combobox.addItems(resource_storage_location_options.keys())
        layout.addWidget(self.resource_storage_location_combobox)

        self.button = QPushButton("Рассчитать")
        self.button.clicked.connect(self.calculate_risk)
        layout.addWidget(self.button)

        # QLabel for displaying the result
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def get_user_input(self):
        label_encodings = {
            "class_vulnerability": {"Уязвимость кода": 1, "Уязвимость архитектуры": 2, "Уязвимость многофакторная": 3},
            "cvss_level": {"Низкий уровень опасности": 1, "Средний уровень опасности": 2,
                           "Высокий уровень опасности": 3, "Критический уровень опасности": 4},
            "vulnerability_status": {"Подтверждена производителем": 1, "Подтверждена в ходе исследований": 2,
                                     "Потенциальная уязвимость": 3},
            "exploit_presence": {"Данные уточняются": 1, "Существует": 2, "Существует в открытом доступе": 3},
            "fix_info": {"Уязвимость устранена": 1, "Информация об устранении отсутствует": 2},
            "incident_relation": {"Связь с инцидентами ИБ присутвует": 1, "Связь с инцидентами ИБ отсутствует": 2},
            "threat_source": {"Внешний нарушитель с низким потенциалом": 1,
                              "Внутренний нарушитель с низким потенциалом": 2,
                              "Внешний нарушитель со средним потенциалом": 3,
                              "Внутренний нарушитель со средним потенциалом": 4,
                              "Внешний нарушитель с высоким потенциалом": 5,
                              "Внутренний нарушитель с высоким потенциалом": 6},
            "confidentiality_violation": {"Да": 1, "Нет": 2},
            "integrity_violation": {"Да": 1, "Нет": 2},
            "availability_violation": {"Да": 1, "Нет": 2},
            "resource_type": {"Общедоступный": 1, "Конфиденциальный": 2},
            "confidentiality_category": {f"Категория {i}": i for i in range(1, 17)},
            "resource_cost": {"Недорогой ресурс": 1, "Среднестоимостной ресурс": 2, "Дорогостоящий ресурс": 3,
                              "Эксклюзивный ресурс": 4},
            "resource_storage_location": {f"Место хранения {i}": i for i in range(1, 11)}
        }

        user_input = []
        for combo_box, encoding_dict in zip(
                [
                    self.class_vulnerability_combobox, self.cvss_options_combobox,
                    self.vulnerability_status_combobox, self.exploit_presence_combobox,
                    self.fix_info_combobox, self.incident_relation_combobox,
                    self.threat_source_combobox, self.confidentiality_violation_combobox,
                    self.integrity_violation_combobox, self.availability_violation_combobox,                     self.resource_type_combobox, self.confidentiality_category_combobox,
                    self.resource_cost_combobox, self.resource_storage_location_combobox
                ],
                label_encodings.values()
        ):
            current_text = combo_box.currentText()
            encoding = encoding_dict.get(current_text)
            if encoding is not None:
                user_input.append(encoding)
            else:
                raise ValueError(f"Invalid value '{current_text}' for combo box {combo_box.objectName()}")

        return user_input

    def calculate_risk(self):
        try:
            user_input = self.get_user_input()
            data = pd.DataFrame([user_input],
                                columns=['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3', '4.3'])

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="test"
            )

            data_ml_table = pd.read_sql_query('SELECT * FROM ml_table_all_random', connection)

            X = data_ml_table[
                ['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3', '4.3']]
            y = data_ml_table['risk']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            prediction = model.predict(data)[0]
            # Calculate total sum
            total_sum = sum(user_input)
            if 13 <= total_sum <= 24:
                risk_level = "Низкий"
            elif 25 <= total_sum <= 36:
                risk_level = "Средний"
            elif 37 <= total_sum <= 48:
                risk_level = "Высокий"
            elif 49 <= total_sum <= 61:
                risk_level = "Критический"
            else:
                risk_level = "Проверьте правильность ввода"

                # Set the result label text
            self.result_label.setText(f"Предсказанное значение столбца risk: {prediction}\n"
                                      f"\nСумма всех цифр: {total_sum} {risk_level}\n"
                                      f"\nОтчет о классификации:\n{classification_report(y_test, y_pred)}\n"
                                      f"Матрица ошибок:\n{str(confusion_matrix(y_test, y_pred))}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

def excepthook(exctype, value, traceback):
    # Выводим сообщение об ошибке
    QMessageBox.critical(None, "Error", f"An error occurred: {value}")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = RiskCalculator()
        window.show()
        sys.exit(app.exec_())