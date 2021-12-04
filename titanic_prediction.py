predictions = model_LogisticRegression.predict(X_test)
pd.DataFrame({"Prediction": predictions, "Actual": y_test})