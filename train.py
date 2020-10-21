from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt
import json
import os
import numpy as np

# Read in data
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")

# Fit a model
depth = 5
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)

os.mkdir("./metrics/")

with open("./metrics/metrics.json", 'w') as outfile:
    json.dump({"accuracy": acc}, outfile)


with open("./metrics/classification_report.json", "w") as outfile:
    json.dump(classification_report(y_test, clf.predict(X_test), output_dict=True), outfile)

# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize='true', cmap=plt.cm.Blues)
plt.savefig('confusion_matrix.png')

