# BioResponse

PREDICTION OF A BIOLOGICAL RESPONSE OF A MOLECULE
--------------------------------------------------

NOTE: For this particular program to work, you will need to install the following:
	* Python
	* NumPy
	* SKLearn or python-scikits-learn

Files:
	Code:			classify.py
	Training Data: 	Data/train.csv
	Test Data:		Data/test.csv
	Results:		Data/results.csv

Datsets:
	Both training and the test data is represented in the CSV format.
	Each row in the training dataset should correspond to a molecule with 
	the first row in the file being the names of the features used. 
	The first column contains the actual biological response (label) and 
	remaining columns represents molecular features used. 
	The test data set[2] is in the same format as the training set except for the first column (label).

Running the python script:
	python classify.py [path_for_training_data_file] [path_for_test_data_file]

Results:
	Results are saved in Data/results.csv.
	Each line in the output corresponds to a molecule in the test dataset.
