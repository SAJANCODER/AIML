from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=42)
#implementation of decision tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(x_train,y_train)
dt_pred=dt_model.predict(x_test)
dt_accuracy=accuracy_score(y_test,dt_pred)
print(f"Decision Tree Accuracy:{dt_accuracy:.2f}")

#implementation of random forest
rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(x_train,y_train)
rf_predict=rf_model.predict(x_test)
rf_accuracy=accuracy_score(y_test,rf_predict)
print(f"Random Forest Accuracy:{rf_accuracy:.2f}")