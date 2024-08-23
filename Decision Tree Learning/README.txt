Usage:

read csv file by using Dataset class and then run DecisionTreeLearner with the generated dataset.
Simply run 'python run.py' to get a decision tree from restaurant.csv. The following codes are from run.py:

from Dataset import DataSet
from DTL import DecisionTreeLearner

# attr_names is a string including space-delimited attribute names
# target is the target we want to show as the final result
# file_name is the file name of the csv file(ex: file_name='restaurant' for  restaurant.csv)

dataset = DataSet(file_name='restaurant', target='Wait',
                   attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Type WaitEstimate Wait')


dtl= DecisionTreeLearner(dataset)
dtl.show(indent=0)