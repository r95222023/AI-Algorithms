
class DecisionTree:
    """
    A decision tree forked by testing an attribute, and a dict
    of branches, one for each of the attribute's values.
    """

    def __init__(self, attr, attr_name=None, default_child=None, branches=None):
        """Initialize by saying what attribute this node tests."""
        self.attr = attr
        self.attr_name = attr_name or attr
        self.default_child = default_child
        self.branches = branches or {}

    def add(self, val, subtree):
        """Add a branch."""
        self.branches[val] = subtree

    def show(self, indent=0):
        name = self.attr_name
        print(name, '?')
        for (val, subtree) in self.branches.items():
            print(' ' * 4 * indent, name, '=', val, '-->', end=' ')
            subtree.show(indent=indent + 1)

class DecisionLeaf:
    """A leaf of a decision tree with a given result"""

    def __init__(self, result, target_attr_name="Target"):
        self.result = result
        self.target_attr_name=target_attr_name

    def show(self, indent=0):
        print(self.target_attr_name, '=', self.result)