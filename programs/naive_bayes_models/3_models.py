from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------
# Gaussian Naive Bayes (for continuous data)
# -------------------------------
gnb = GaussianNB()
gnb.fit(X_train, y_train)
gnb_preds = gnb.predict(X_test)
gnb_accuracy = accuracy_score(y_test, gnb_preds)
print(f"GaussianNB Accuracy: {gnb_accuracy:.2f}")

# -------------------------------
# Multinomial Naive Bayes (best for count data)
# -------------------------------
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
mnb_preds = mnb.predict(X_test)
mnb_accuracy = accuracy_score(y_test, mnb_preds)
print(f"MultinomialNB Accuracy: {mnb_accuracy:.2f}")

# -------------------------------
# Bernoulli Naive Bayes (binary features)
# -------------------------------
bnb = BernoulliNB()
bnb.fit(X_train, y_train)
bnb_preds = bnb.predict(X_test)
bnb_accuracy = accuracy_score(y_test, bnb_preds)
print(f"BernoulliNB Accuracy: {bnb_accuracy:.2f}")
