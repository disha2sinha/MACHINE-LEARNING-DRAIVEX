import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

data=pd.read_csv("Train.csv")
testx_data=pd.read_csv("test_X.csv")
testy_data=pd.read_csv("test_Y.csv")
testx_data["Survived"]=testy_data["Survived"]
main_data=(data.append(testx_data))

print(main_data.isnull().sum())
main_data["Age"]=main_data["Age"].fillna(main_data["Age"].mean())
main_data["Fare"]=main_data["Fare"].fillna(main_data["Fare"].mean())
s_count=main_data[main_data["Embarked"]=="S"].count()
q_count=main_data[main_data["Embarked"]=="Q"].count()
c_count=main_data[main_data["Embarked"]=="C"].count()
main_data["Embarked"]=main_data["Embarked"].fillna("S")
main_data.drop(["Cabin","Name","Ticket"],axis=1,inplace=True)
print(main_data.isnull().sum())

math=main_data.describe()
print(math)

plt.hist(main_data.Survived)
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

plt.hist(main_data.Age)
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.hist(main_data.Parch)
plt.xlabel("Parch")
plt.ylabel("Count")
plt.show()

plt.hist(main_data.SibSp)
plt.xlabel("SibSp")
plt.ylabel("Count")
plt.show()

plt.hist(main_data.Fare)
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

plt.hist(main_data.Pclass)
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.show()

sns.countplot(main_data.Survived,hue=main_data.Sex)
plt.show()

sns.countplot(main_data.Survived,hue=main_data.Pclass)
plt.show()

sns.countplot(main_data.Survived,hue=main_data.Parch)
plt.show()

sns.countplot(main_data.Survived,hue=main_data.SibSp)
plt.show()

sns.countplot(main_data.Survived,hue=main_data.Embarked)
plt.show()

sns.boxplot(x=main_data.Pclass,y=main_data.Age)
plt.show()

plt.scatter(main_data.Fare,main_data.Age)
plt.xlabel("Fare")
plt.ylabel("Age")
plt.show()

plt.scatter(main_data.Survived,main_data.Age)
plt.ylabel("Age")
plt.xlabel("Survived")
plt.show()

plt.scatter(main_data.Survived,main_data.Fare)
plt.ylabel("Fare")
plt.xlabel("Survived")
plt.show()

dataset=main_data[["PassengerId","Pclass","Sex","Age","Fare","SibSp","Parch","Embarked"]]
dummy_set=pd.get_dummies(dataset)

X=dummy_set
y=main_data["Survived"]

X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.8675)
trained_model=LogisticRegression()
trained_model.fit(X_train, y_train)
predict=trained_model.predict(X_test)
print("ACURRACY : ",trained_model.score(X_test, y_test))







