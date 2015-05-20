# Data Mining Assigment 
# ----------------------
# Title:		PREDICTION OF A BIOLOGICAL RESPONSE OF A MOLECULE
# Language: 	Python
# Libraries:	NumPy, SKLearn - Python Machine Learning Library
# Submitted By:
# 		Rahul P 		B090195CS
# 		Mohammed Hashir		B090167CS
# 		Delbin Thomas		B090109CS
# 		Assim Ambadi P 		B090068CS
# Date:	March 31, 2013


import os, sys
from numpy import genfromtxt, savetxt
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

def Classifiy ():
	"""Function which creates training and test datasets and does the classification using 
	Random Forest Classifier using sklearn library."""

	# Generate datset from the given csv file of training data
	Traincsv = sys.argv[1]
	if os.path.isfile (Traincsv):
		pass
	else:
		raise IOError ('File does not exist')
	Dataset = genfromtxt (open (Traincsv, 'r'), delimiter = ',', dtype = 'f8')[1:]

	# Create a list of target values or labels (first entry in each row of the dataset)
	Target = [x[0] for x in Dataset]

	# Create a list of training data
	Train = [x[1:] for x in Dataset]

	# Create test data from the given csv file of test data
	Testcsv = sys.argv[2]
	if os.path.isfile (Testcsv):
		pass
	else:
		raise IOError ('File does not exist')
	Test = genfromtxt (open (Testcsv, 'r'), delimiter = ',', dtype = 'f8')[1:]

	# Create the random forest classifier. n_jobs = -1 will use the number of cores in the machine
	RFClassifier = RandomForestClassifier (n_estimators = 100, n_jobs = -1)

	# Train the random forest classifier
	RFClassifier.fit (Train, Target)

	# Prediction of test data
	Prediction = [x[1] for x in RFClassifier.predict_proba (Test)]

	# Saving the results
	savetxt ('Data/results.csv', Prediction, delimiter = ',', fmt = '%f')
	print "The results are saved in \"Data/results.csv\". Each line corresponds to the \"Probability of a molecule in the test dataset evoking the particular Biological Response\"."

if __name__ == '__main__':
	"""Invoking the Classify routine"""
	
	ErrorFlag = False

	if len (sys.argv) != 3:
		ErrorFlag = True

	if not ErrorFlag:
		ext1 = sys.argv[1].split('.')[1]
		ext2 = sys.argv[2].split('.')[1]
		if ext1 != 'csv' or ext2 != 'csv':
			ErrorFlag = True

	if ErrorFlag:
		print "python classify.py [csv file for Training data] [csv file for Test data]"
		sys.exit(1)
	Classifiy ()
