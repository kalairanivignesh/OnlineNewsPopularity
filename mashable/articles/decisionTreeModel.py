from sklearn.tree import DecisionTreeClassifier


def predict(x_train, x_test, y_train):
    model = DecisionTreeClassifier(criterion="entropy", max_depth=None)
    model.fit(x_train, y_train)
    return model.predict(x_test)

