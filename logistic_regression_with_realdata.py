import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

data = pd.read_csv('adults.txt', sep=',')

for label in ['race', 'occupation']:
	data[label] = LabelEncoder().fit_transform(data[label])

X = data[['race', 'hours_per_week', 'occupation']]

y = data['sex'].values.tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = LogisticRegression()

clf.fit(X_train, y_train)

Accuracy = clf.score(X_test, y_test)

print("Accuracy: " + str(Accuracy))

prediction = clf.predict(X_test)

print(prediction)

cfs = confusion_matrix(prediction, y_test)

print("Confusion_matrix: " + str(cfs))

