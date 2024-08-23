from Dataset import DataSet
from DTL import DecisionTreeLearner


dataset = DataSet(file_name='restaurant', target='Wait',
                   attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Type WaitEstimate Wait')

print('Dataset:', dataset.examples)
# [['Yes', 'No', 'No', 'Yes', 'Some', '$$$', 'No', 'Yes', 'French', '0-10', 'Yes'],
# ['Yes', 'No', 'No', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '30-60', 'No'],
# ['No', 'Yes', 'No', 'No', 'Some', '$', 'No', 'No', 'Burger', '0-10', 'Yes'],
# ['Yes', 'No', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Thai', '10-30', 'Yes'],
# ['Yes', 'No', 'Yes', 'No', 'Full', '$$$', 'No', 'Yes', 'French', '>60', 'No'],
# ['No', 'Yes', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Italian', '0-10', 'Yes'],
# ['No', 'Yes', 'No','No', 'None', '$', 'Yes', 'No', 'Burger', '0-10', 'No'],
# ['No', 'No', 'No', 'Yes', 'Some', '$$', 'Yes', 'Yes', 'Thai', '0-10', 'Yes'],
# ['No', 'Yes', 'Yes', 'No', 'Full', '$', 'Yes', 'No', 'Burger', '>60', 'No'],
# ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$$$', 'No', 'Yes', 'Italian', '10-30', 'No'],
# ['No', 'No', 'No', 'No', 'None', '$', 'No', 'No', 'Thai', '0-10', 'No'],
# ['Yes', 'Yes', 'Yes', 'Yes', 'Full', '$', 'No', 'No', 'Burger', '30-60', 'Yes']]
print('-'*200)
dtl= DecisionTreeLearner(dataset)
# Information gain for first split  [0.0, 0.0, 0.020720839623908027, 0.19570962879973086, 0.5408520829727552, 0.19570962879973086, 0.0, 0.020720839623908027, 0.0, 0.20751874963942196]
print('-'*200)
print('Decision Tree')
dtl.show(indent=1)
# Result Example
#
# Patrons ?
#  Patrons = Some --> Wait = Yes
#  Patrons = Full --> Price ?
#      Price = $$ --> Wait = No
#      Price = $ --> WaitEstimate ?
#          WaitEstimate = >60 --> Wait = No
#          WaitEstimate = 0-10 --> Wait = No
#          WaitEstimate = 10-30 --> Wait = Yes
#          WaitEstimate = 30-60 --> Bar ?
#              Bar = Yes --> Wait = Yes
#              Bar = No --> Wait = No
#      Price = $$$ --> Wait = No
#  Patrons = None --> Wait = No
