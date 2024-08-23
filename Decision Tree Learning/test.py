from Dataset import DataSet
from DTL_old import DecisionTreeLearner


dataset = DataSet(file_name='restaurant', target='Wait',
                   attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Type WaitEstimate Wait')


dtl= DecisionTreeLearner(dataset)
print(dtl)