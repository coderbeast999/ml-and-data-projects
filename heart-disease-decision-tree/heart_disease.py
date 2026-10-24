import pandas as pd
import GWCutilities as util

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

print("\n-----\n")


df = pd.read_csv("heartDisease_2020_sampling.csv")


print(
    "We will be performing data analysis on this Indicators of Heart Disease Dataset. Here is a sample of it: \n"
)

#Print the dataset's first five rows

print(df.head())


input("\n Press Enter to continue.\n")



#Data Cleaning
#Label encode the dataset
df = util.labelEncoder(df,["HeartDisease", "GenHealth", "PhysicalActivity", "AgeCategory", "AlcoholDrinking", "Smoking"])

print("\nHere is a preview of the dataset after label encoding. \n")
print(df.head())

input("\nPress Enter to continue.\n")

#One hot encode the dataset
df = util.oneHotEncoder(df, ["Race", "Sex"])

print(
    "\nHere is a preview of the dataset after one hot encoding. This will be the dataset used for data analysis: \n"
)

print(df.head())

input("\nPress Enter to continue.\n")



#Decision Tree Model
from sklearn.model_selection import train_test_split

X = df.drop(["HeartDisease"], axis = 1)
y = df["HeartDisease"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 2)

print(X_train.head())


from sklearn.tree import DecisionTreeClassifier


clf = DecisionTreeClassifier(max_depth = 9, class_weight = 'balanced')
clf = clf.fit(X_train, y_train)



#Test the model with the testing data set and prints accuracy score
test_Predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score

test_acc = accuracy_score(y_test, test_Predictions)

print("the accuracy of the testing descion tree classifier is: "+str(test_acc))


#confusion matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, test_Predictions, labels = [1,0])

print("The confusion matrix of the tree is: ")

print(cm)

train_Predictions = clf.predict(X_train)

train_acc = accuracy_score(y_train, train_Predictions)

print("the accuracy of the descion training tree classifier is: "+str(train_acc))













#Prints a text representation of the Decision Tree
print("\nBelow is a text representation of how the Decision Tree makes choices:\n")
input("\nPress Enter to continue.\n")

util.printTree(clf,X.columns)
print("The leaf node containing the largest number of correctly classified patients with Heart Disease is the one where patients do not drink alcohol (AlcoholDrinking ≤ 0.50). This leaf node contains 200 correctly classified Heart Disease patients. The decision path to this leaf is: BMI ≤ 39.44, AgeCategory > 11.5, and AlcoholDrinking ≤ 0.50.")
