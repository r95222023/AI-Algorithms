# Decision Tree Learner

This project implements a decision tree learner using a dataset from a CSV file. It reads the data, builds a decision tree, and displays it.

## Features
- **Decision Tree Construction**: Builds a decision tree from the provided dataset.
- **Classification & Regression**: Can be adapted for both classification and regression tasks.
- **Easy Visualization**: Displays the decision tree structure in an easily interpretable format.

## Usage

1. **Prepare your CSV file**: Ensure your CSV file is formatted correctly. For example, use `restaurant.csv` for this project.

2. **Configure the program**: Modify the `run.py` to configure the decision tree:

```python
from Dataset import DataSet
from DTL import DecisionTreeLearner

# attr_names is a string including space-delimited attribute names
# target is the target we want to show as the final result
# file_name is the file name of the csv file(ex: file_name='restaurant' for  restaurant.csv)

dataset = DataSet(file_name='restaurant', target='Wait',
                   attr_names='Alternate Bar Fri/Sat Hungry Patrons Price Raining Reservation Type WaitEstimate Wait')


dtl= DecisionTreeLearner(dataset)
dtl.show(indent=0)
```

3. **Run the program**: Execute the following command to build and display the decision tree:

```bash
python run.py
```
