# # machine_learning.py
#
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report, confusion_matrix
#
# def train_and_predict_model(data_ml_table, user_input):
#     # Разделите данные на признаки (X) и целевую переменную (y)
#     X = data_ml_table[['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3', '4.3']]
#     y = data_ml_table['risk']
#
#     # Разделите данные на обучающий и тестовый наборы
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#     # Инициализируйте и обучите модель случайного леса
#     model = RandomForestClassifier()
#     model.fit(X_train, y_train)
#
#     # Получение предсказаний для тестового набора данных
#     y_pred = model.predict(X_test)
#
#     # Делаем предсказание на основе введенных данных
#     prediction = model.predict([user_input])[0]
#
#     return model, prediction, X_test, y_test, y_pred

# # ИНТЕРФЕЙС !!!

