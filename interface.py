# # interface.py
#
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report
#
# # Функция для запроса данных у пользователя
# def get_user_input():
#     print("Оцените класс уязвимости: \n"
#           "1- Уязвимость кода, \n"
#           "2- Уязвимость архитектуры, \n"
#           "3- Уязвимость многофакторная, \n")
#     class_vulnerability = int(input())
#
#     print("Оцените уязвимость по системе CVSS: \n"
#           "1- Низкий уровень опасности, \n"
#           "2- Средний уровень опасности, \n"
#           "3- Высокий уровень опасности, \n"
#           "4- Критический уровень опасности, \n")
#     cvss = int(input())
#
#     print("Оцените статус уязвимости от 1 до 3: \n"
#           "1-Подтверждена производителем, \n"
#           "2-Подтверждена в ходе исследований, \n"
#           "3-Потенциальная уязвимость, \n")
#     vulnerability_status = int(input())
#
#     print("Оцените наличие эксплойта от 1 до 3:\n"
#           "1-Данные уточняются, \n"
#           "2-Существует, \n"
#           "3-Существует в открытом доступе, \n")
#     exploit_presence = int(input())
#
#     print("Оцените информацию об устранении от 1 до 2: \n"
#           "1-Уязвимость устранена, \n"
#           "2-Информация об устранении отсутствует, \n")
#     fix_info = int(input())
#
#     print("Оцените связь с инцидентами ИБ от 1 до 2: \n"
#           "1-Связь с инцидентами ИБ присутвует, \n"
#           "2-Связь с инцидентами ИБ отсутствует, \n")
#     incident_relation = int(input())
#
#     print(
#         "Укажите источник угрозы: 1-Внешний нарушитель с низким потенциалом, 2-Внутренний нарушитель с низким потенциалом, "
#         "3-Внешний нарушитель со средним потенциалом, 4-Внутренний нарушитель со средним потенциалом, "
#         "5-Внешний нарушитель с высоким потенциалом, 6-Внутренний нарушитель с высоким потенциалом:")
#     threat_source = int(input())
#
#     print("Укажите присутствует ли нарушение конфиденциальности: 1-да, 2-нет")
#     confidentiality_violation = int(input())
#
#     print("Укажите присутствует ли нарушение целостности: 1-да, 2-нет")
#     integrity_violation = int(input())
#
#     print("Укажите присутствует ли нарушение доступности: 1-да, 2-нет")
#     availability_violation = int(input())
#
#     print("Укажите тип ресурса: 1-общедоступный, 2-конфиденциальный")
#     resource_type = int(input())
#     # Проверяем, выбран ли тип ресурса "общедоступный" (значение 1)
#     if resource_type == 1:
#         # Присваиваем нулевое значение категории конфиденциальности
#         confidentiality_category = 0
#     else:
#         # Запрашиваем категорию конфиденциальности: Для служебного пользования (ДСП), Секретно (С), Совершенно секретно (СС),
#         # Особой важности (ОВ).
#         print("Укажите категорию конфиденциальности: "
#               "1-Ограничено, "
#               "2-Ограниченный доступ, "
#               "3-Не для публичного распространения, "
#               "4-Для внутреннего пользования, "
#               "5-Личная информация, "
#               "6-Собственность компании, "
#               "7-Защищено по авторскому праву, "
#               "8-Частная информация, "
#               "9-Конфиденциально, "
#               "10-Секретно, "
#               "11-Конфиденциальный обмен, "
#               "12-Конфиденциальная связь, "
#               "13-Специальная обработка, "
#               "14-Коммерческая тайна, "
#               "15-Секретная коммерческая информация, "
#               "16-Специальная категория:")
#         confidentiality_category = int(input())
#
#     print(
#         "Укажите стоимость ресурса: 1-Недорогой ресурс, 2-Среднестоимостной ресурс, 3-Дорогостоящий ресурс, 4-Эксклюзивный ресурс:")
#     resource_cost = int(input())
#
#     print("Укажите место хранения ресурса: "
#           "1-Локально на компьютерах, "
#           "2-Локальный сервер, "
#           "3-Офис, "
#           "4-Веб-сервер, "
#           "5-На серверах, "
#           "6-Облачные операционные системы, "
#           "7-Облачное хранилище, "
#           "8-Дата-центр, "
#           "9-Глобальная сеть Интернет, "
#           "10-Хостинг на серверах провайдеров:")
#     resource_storage_location = int(input())
#
#     total_sum = class_vulnerability + cvss + vulnerability_status + exploit_presence + fix_info + incident_relation + threat_source + \
#                 confidentiality_violation + integrity_violation + availability_violation + resource_type + \
#                 confidentiality_category + resource_cost + resource_storage_location
#
#     if 13 <= total_sum <= 24:
#         print("Сумма всех цифр:", total_sum, "Низкий")
#     elif 25 <= total_sum <= 36:
#         print("Сумма всех цифр:", total_sum, "Средний")
#     elif 37 <= total_sum <= 48:
#         print("Сумма всех цифр:", total_sum, "Высокий")
#     elif 49 <= total_sum <= 61:
#         print("Сумма всех цифр:", total_sum, "Критический")
#     else:
#         print("Сумма всех цифр:", total_sum, "Проверьте правильность ввода")
#
#     return [class_vulnerability, cvss, vulnerability_status, exploit_presence, fix_info, incident_relation,
#             threat_source, confidentiality_violation, integrity_violation, availability_violation, resource_type,
#             confidentiality_category, resource_cost, resource_storage_location]
#
#
#
# def print_result(prediction, model, X_test, y_test, y_pred):
#     # Отобразите предсказанное значение пользователю
#     print("Предсказанное значение столбца risk:", prediction)
#
#     # Оцените точность модели
#     accuracy = model.score(X_test, y_test)
#     print("Точность модели:", accuracy)
#
#     # Вывод матрицы ошибок
#     print("Матрица ошибок:")
#     print(confusion_matrix(y_test, y_pred))
#
#     # Вывод отчета о классификации
#     print("\nОтчет о классификации:")
#     print(classification_report(y_test, y_pred))
#
# #         ИНТЕРФЕЙС!!!
#
