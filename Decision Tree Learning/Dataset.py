def open_data(name, mode='r'):
    return open(name, mode=mode)

def num_or_str(x):
    """Convert string to a number if possible, or remove unwanted spaces."""
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return str(x).strip()

def unique(seq):
    """Remove duplicate elements from seq."""
    return list(set(seq))

def parse_csv(input, delim=','):
    """
    Convert csv file into a list of lists. Blank lines are skipped.
    Fields that look like numbers are converted to numbers.
    ex: parse_csv('1, 2, 3 \n d, e, f')
    [[1, 2, 3], ['d', 'e', 'f']]
    """
    lines = [line for line in input.splitlines() if line.strip()]
    return [list(map(num_or_str, line.split(delim))) for line in lines]


class DataSet:
    """
    A dataset for a Decision tree learning problem. It has the following fields:

    attrs      A list of attr index.
    attr_names Optional list of mnemonic names for corresponding attrs.
    target     The attribute that a learning algorithm will try to predict.
                  (final attribute by default)
    values     A list of lists: each sublist is the set of possible
                 values for the corresponding attribute.
    file_name  File name of the data set.
    inputs     The list of attrs without the target.
    """

    def __init__(self, attr_names=None, target=-1, file_name=''):
        """
        Create a dataset by parsing a csv file.
        """
        self.file_name = file_name
        # initialize .examples from a csv file
        self.examples = parse_csv(open_data(file_name + '.csv').read())

        # attrs are the indices of examples
        attrs = list(range(len(self.examples[0])))

        self.attrs = attrs

        self.attr_names = attr_names.split()

        self.target = self.attr_names.index(target)
        self.inputs = [a for a in self.attrs if a != self.target]
        self.values = list(map(unique, zip(*self.examples)))
