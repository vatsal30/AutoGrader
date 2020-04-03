import os
import pandas as pd

os.system('cd /home/vatsal/Desktop/LT-Autograder-master/TestCode')
os.system('python2 /home/vatsal/Desktop/LT-Autograder-master/TestCode/preProcessData.py')
os.system('Rscript /home/vatsal/Desktop/LT-Autograder-master/TestCode/predict_labels.R')
os.system('Rscript /home/vatsal/Desktop/LT-Autograder-master/TestCode/modelingRf.R')
os.system('Rscript /home/vatsal/Desktop/LT-Autograder-master/TestCode/modelingGbm.R')
os.system('Rscript /home/vatsal/Desktop/LT-Autograder-master/TestCode/AveModels.R')

prediction = pd.read_csv('/home/vatsal/Desktop/LT-Autograder-master/TestCode/finalModel/finalPrediction.csv',sep=',')

print(prediction)