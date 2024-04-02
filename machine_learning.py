import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_and_predict(data_ml_table, data, user_input):
    X = data_ml_table[
        ['1', '2', '3', '4', '5', '6', '1.2', '2.2', '3.2', '4.2', '1.3', '2.3', '3.3']]
    y = data_ml_table['risk']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    prediction = model.predict(data.values)[0]
    total_sum = sum(user_input)

    return prediction, total_sum, y_test, y_pred
