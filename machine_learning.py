# machine_learning.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score, learning_curve, train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error, roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from lightgbm import LGBMClassifier


def train_and_predict(data_ml_table, data, user_input):
    # Преобразуем целевую переменную 'risk' в числовой формат
    risk_mapping = {'Низкий': 0, 'Средний': 1, 'Высокий': 2, 'Критический': 3}
    reverse_risk_mapping = {v: k for k, v in risk_mapping.items()}  # обратное отображение для имен классов
    data_ml_table['risk'] = data_ml_table['risk'].map(risk_mapping)

    X = data_ml_table[['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3']]
    y = data_ml_table['risk']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #model = RandomForestClassifier()
    #model = LogisticRegression()
    #model = SVC()
    #model = GradientBoostingClassifier()
    model = LGBMClassifier()

    # Выполнить крос-валидацию
    scores = cross_val_score(model, X, y, cv=5)  # 5-fold cross-validation
    print("Cross-Validation Scores:", scores)
    print("Mean Accuracy:", scores.mean())
    print("Standard Deviation of Accuracy:", scores.std())

    # Отобразиь кривые обучения
    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        model, X, y, cv=5, n_jobs=-1, train_sizes=np.linspace(.1, 1.0, 5), return_times=True)

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(10, 6))
    plt.title("Learning Curve")
    plt.xlabel("Training examples")
    plt.ylabel("Score")

    plt.grid()
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
    plt.legend(loc="best")
    #plt.show()

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    prediction = model.predict(data.values)[0]
    total_sum = sum(user_input)

    # Рассчитать accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Отчет о классификации
    report = classification_report(y_test, y_pred, target_names=[reverse_risk_mapping[i] for i in range(len(reverse_risk_mapping))])

    # Матриа ошибок
    matrix = confusion_matrix(y_test, y_pred)

    # Ошибка обучения на тренировочных данных
    train_error = mean_squared_error(y_train, model.predict(X_train))

    # Ошибка обучения на тестовых данных
    test_error = mean_squared_error(y_test, y_pred)

    # Вычисление AUC-ROC
    y_proba = model.predict_proba(X_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(len(risk_mapping)):
        fpr[i], tpr[i], _ = roc_curve(label_binarize(y_test, classes=[0, 1, 2, 3])[:, i], y_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    plt.figure(figsize=(10, 6))
    for i in range(len(risk_mapping)):
        plt.plot(fpr[i], tpr[i], lw=2, label=f'ROC curve for class {i} (area = {roc_auc[i]:0.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC)')
    plt.legend(loc="lower right")
    #plt.show()

    print(f"Prediction: {reverse_risk_mapping[prediction]}")
    print(f"Total sum: {total_sum}")
    print(f"Accuracy: {accuracy}")
    print("Classification Report:")
    print(report)
    print("Confusion Matrix:")
    print(matrix)
    print("Train Error:", train_error)
    print("Test Error:", test_error)
    prediction = reverse_risk_mapping[model.predict(data.values)[0]]

    return prediction, total_sum, y_test, y_pred

##############

# Определение функции train_and_predict, которая обучает модель и делает предсказание
def train_and_predict(data_ml_table, data, user_input):
    # Преобразование целевой переменной 'risk' в числовой формат
    risk_mapping = {'Низкий': 0, 'Средний': 1, 'Высокий': 2, 'Критический': 3}
    reverse_risk_mapping = {v: k for k, v in risk_mapping.items()}  # Обратное отображение для имен классов
    data_ml_table['risk'] = data_ml_table['risk'].map(risk_mapping)

    # Выделение признаков и целевой переменной из данных
    X = data_ml_table[['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3']]
    y = data_ml_table['risk']

    # Разделение данных на обучающий и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Выбор модели классификации
    model = LGBMClassifier()

    # Обучение модели
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    prediction = model.predict(data.values)[0]
    total_sum = sum(user_input)

    # Отчет о классификации
    report = classification_report(y_test, y_pred, target_names=[reverse_risk_mapping[i] for i in range(len(reverse_risk_mapping))])

    # Предсказание и возврат результата
    prediction = reverse_risk_mapping[model.predict(data.values)[0]]

    return prediction, total_sum, y_test, y_pred
