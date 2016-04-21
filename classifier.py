#!/usr/bin/python
import sys
from sklearn import svm
from sklearn import ensemble,tree
from sklearn import neighbors
from sklearn.metrics import confusion_matrix
from sklearn import cross_validation
import random
import numpy as np

def main():
	reader = open("./Dataset/final.csv")
	data = reader.readlines()
	random.shuffle(data)
	data=data[:10000]
	newdata = np.array([x.strip().split(',') for x in data])
	training=newdata[:8000]
	train_a = [row[-1] for row in training]
	train_f=[row[:12] for row in training]	
	testing = newdata[8001:]
	test_a = [row[-1] for row in testing]
	test_f=[row[:12] for row in testing]
	print "training started"
	clf = svm.SVC(kernel="rbf")
	clf.fit(train_f,train_a)
	#num_train_a=np.asarray(train_a)
	#scores = cross_validation.cross_val_score(clf,train_a,train_f, cv=5)
	#print scores
	print "training done"
	correct=0
	wrong=0
	ans=list(clf.predict(test_f))
	print "prediction done"
	for i in range(len(ans)):
		if(ans[i]==test_a[i]):
			correct+=1
		else:
			wrong+=1
	print correct,wrong
	print confusion_matrix(ans,test_a)	
main()	

