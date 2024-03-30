import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_Widget
import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

class YourMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_risk)

    def get_user_input(self):
        checkbox_encodings = {
            "class_vulnerability": {
                self.ui.checkBox: 1,
                self.ui.checkBox_2: 2,
                self.ui.checkBox_3: 3
            },
            "cvss_level": {
                self.ui.checkBox_4: 1,
                self.ui.checkBox_5: 2,
                self.ui.checkBox_6: 3,
                self.ui.checkBox_7: 4
            },
            "vulnerability_status": {
                self.ui.checkBox_8: 1,
                self.ui.checkBox_9: 2,
                self.ui.checkBox_10: 3
            },
            "exploit_presence": {
                self.ui.checkBox_11: 1,
                self.ui.checkBox_12: 2,
                self.ui.checkBox_13: 3
            },
            "fix_info": {
                self.ui.checkBox_14: 1,
                self.ui.checkBox_15: 2
            },
            "incident_relation": {
                self.ui.checkBox_16: 1,
                self.ui.checkBox_17: 2
            },
            "threat_source": {
                self.ui.checkBox_18: 1,
                self.ui.checkBox_19: 2,
                self.ui.checkBox_20: 3,
                self.ui.checkBox_21: 4,
                self.ui.checkBox_22: 5,
                self.ui.checkBox_23: 6
            },
            "confidentiality_violation": {
                self.ui.checkBox_24: 2 # if self.ui.checkBox_24.isChecked() else 1
            },
            "integrity_violation": {
                self.ui.checkBox_25: 2 # if self.ui.checkBox_25.isChecked() else 1
            },
            "availability_violation": {
                self.ui.checkBox_26: 2 # if self.ui.checkBox_26.isChecked() else 1,
            },
            "resource_type": {
                self.ui.checkBox_27: 1,
                self.ui.checkBox_28: 2
            },
            "confidentiality_category": {
                self.ui.checkBox_29: 1,
                self.ui.checkBox_30: 2,
                self.ui.checkBox_31: 3,
                self.ui.checkBox_32: 4,
                self.ui.checkBox_36: 5,
                self.ui.checkBox_34: 6,
                self.ui.checkBox_33: 7,
                self.ui.checkBox_35: 8,
                self.ui.checkBox_40: 9,
                self.ui.checkBox_38: 10,
                self.ui.checkBox_37: 11,
                self.ui.checkBox_39: 12,
                self.ui.checkBox_44: 13,
                self.ui.checkBox_42: 14,
                self.ui.checkBox_41: 15,
                self.ui.checkBox_43: 16
            },
            "resource_cost": {
                self.ui.checkBox_45: 1,
                self.ui.checkBox_46: 2,
                self.ui.checkBox_47: 3,
                self.ui.checkBox_48: 4
            },
            "resource_storage_location": {
                self.ui.checkBox_49: 1,
                self.ui.checkBox_50: 2,
                self.ui.checkBox_52: 3,
                self.ui.checkBox_51: 4,
                self.ui.checkBox_55: 5,
                self.ui.checkBox_54: 6,
                self.ui.checkBox_53: 7,
                self.ui.checkBox_56: 8,
                self.ui.checkBox_58: 9,
                self.ui.checkBox_57: 10
            }
        }

        user_input = []

        # Iterate through checkbox groups
        for group_name, checkbox_map in checkbox_encodings.items():
            max_value = 0

            # Iterate through checkboxes in the current group
            for checkbox, value in checkbox_map.items():
                if checkbox.isChecked():
                    max_value = max(max_value, value)  # Update for checked boxes

            # Special handling for the three groups
            if group_name in ["confidentiality_violation", "integrity_violation", "availability_violation"]:
                user_input.append(max_value if max_value > 0 else 1)  # Append 1 if none checked
            else:
                user_input.append(max_value)  # Append 0 if none checked in other groups

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

            self.ui.label_70.setText(f"Предсказанное значение столбца risk: {prediction}\n"
                                          f"\nСумма всех цифр: {total_sum} {risk_level}\n"
                                          f"\nОтчет о классификации:\n{classification_report(y_test, y_pred)}\n"
                                          f"Матрица ошибок:\n{str(confusion_matrix(y_test, y_pred))}")

        except Exception as e:
            self.ui.label_70.setText(f"Ошибка: {e}")


def main():
    app = QApplication(sys.argv)
    window = YourMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
