import numpy as np
import matplotlib as plt
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression

data = datasets.load_iris()
model = LogisticRegression(C=1e5)   # meaning of C?
model.fit(data.data, data.target)

expected = data.target
predicted = model.predict(data.data)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
