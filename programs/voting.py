from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data[:,:4]
Y= iris.target

X_train , X_test , y_train , y_test = train_test_split(X,Y,test_size = 0.20 , random_state = 42)

#ensemble of models
estimator = []
estimator.append(('LR',LogisticRegression(solver='lbfgs',multi_class = 'multinomial',max_iter =200)))
estimator.append(('SVC',SVC(gamma='auto',probability = True)))
estimator.append(('DTC',DecisionTreeClassifier()))

#voting classifier with hard voting

vot_hard = VotingClassifier(estimators = estimator , voting = 'hard')
vot_hard.fit(X_train,y_train)
y_pred = vot_hard.predict(X_test)


#using accuracy_score
score = accuracy_score(y_test,y_pred)
print("hard voting %d" %score)

#soft voting
vot_soft=VotingClassifier(estimators = estimator , voting = 'soft')
vot_soft.fit(X_train,y_train)
y_pred = vot_soft.predict(X_test)

#accuruacy
score = accuracy_score(y_test,y_pred)
print("soft voting score %d" %score)



