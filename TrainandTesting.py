import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier

import csv
import sys
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
training_datafile = "./spam_training.csv"
your_list = []
with open(training_datafile, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
label = []
feat = []

trstart = time.time()
for i in range(0, len(your_list)):
    n = len(your_list[i])
    x = []
    for j in range(0, n-1):
        x.append(your_list[i][j])
    x = map(int, x)
    feat.append(x)
    label.append(str(your_list[i][n-1]))

#clf = tree.DecisionTreeClassifier()
clf = GaussianNB()
#clf = SVC()
#clf = KNeighborsClassifier()
#clf = BernoulliNB()
#clf = MultinomialNB()
#clf = RandomForestClassifier(n_estimators=10)
#clf = AdaBoostClassifier(n_estimators=100)
clf = clf.fit(feat, label)
trend = time.time()
print "Total Files Trained = ", len(your_list)


count=0
right=0
wrong=0
total=0
spam_right=0
spam_wrong=0
spam_total=0
ham_right=0
ham_wrong=0
ham_total=0
testart = time.time()
print "testing..."

output_file = "InfoRetriev_AAP.csv"

out = open(output_file, 'w')

testing_datafile = "spam_test.csv"
your_list = []
with open(testing_datafile, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
testart = time.time()
label = []
feat = []
predict_0=0
predict_1=0
for i in range(0, len(your_list)):
    n = len(your_list[i])
    x = []
    for j in range(0, n-1):
        x.append(your_list[i][j])
    x = map(int, x)
    feat.append(x)
    fileID = your_list[i][n-1]
    fileID = fileID.strip(' \t\n\r')
    # lab = 
    #label.append(int(your_list[i][n-1]))  
    total = total + 1
    # 0 for spam
    # 1 for ham
    predict = clf.predict(x)[0]
    # if (predict == 0 && label==0)
        
    out.write(fileID+","+str(predict)+"\n")
    if(predict[1]==0):
    	predict_0 = predict_0+1
    else:
    	predict_1 = predict_1+1
teend = time.time()

print "summary:"
print "total running time: ", teend - trstart
print "total training time: ", trend - trstart
print "total testing time: ", teend - testart
print ""
print "total predicts: ", total
print "total spam(0) predicts: ", predict_0
print "total ham(1) predicts: ", predict_1
