import copy
import random
from collections import defaultdict
from statistics import stdev
import numpy as np
from DecisionTree import DecisionLeaf, DecisionTree


def DecisionTreeLearner(dataset):
    """Algorithm follows Figure 18.5 of `AI a modern approach 3rd edition`"""
    target, values, attr_names = dataset.target, dataset.values, dataset.attr_names
    target_attr_name = attr_names[target]

    def decision_tree_learning(examples, attrs, parent_examples=()):
        if len(examples) == 0:
            return plurality_value(parent_examples)
        elif all_have_same_class(examples, target):
            return DecisionLeaf(examples[0][target], target_attr_name)
        elif len(attrs) == 0:
            return plurality_value(examples)
        A = argmax_random_if_tie(attrs, key=lambda a: information_gain(a, examples))
        tree = DecisionTree(A, attr_names[A], plurality_value(examples))
        for v_k in [v for v in values[A]]:
            exs = [e for e in examples if e[A] == v_k]
            subtree = decision_tree_learning(exs, [x for x in attrs if x != A], examples)
            tree.add(v_k, subtree)
        return tree

    def plurality_value(examples):
        """
        Return the most popular target value for this set of examples.
        """
        popular = argmax_random_if_tie(values[target], key=lambda v: count(target, v, examples))
        return DecisionLeaf(popular, target_attr_name)

    def information_gain(attr, examples):
        """Return the expected reduction in entropy from splitting by attr."""

        # examples, values, target = dataset.examples, dataset.values, dataset.target

        def I(exs):
            return information_content([count(target, v, exs) for v in values[target]])

        n = len(examples)
        remainder = sum((len(examples_i) / n) * I(examples_i) for (v, examples_i) in
                        [(v, [e for e in examples if e[attr] == v]) for v in values[attr]])
        return I(examples) - remainder

    return decision_tree_learning(dataset.examples, dataset.inputs)

def all_have_same_class(examples, target):
    """Whether all examples have the same target class?"""
    target_class = examples[0][target]

    return all(e[target] == target_class for e in examples)

def argmax_random_if_tie(seq, key=lambda x: x):
    """Return an element with highest key(seq[i]); break ties at random."""
    if len(seq)>2:print('Information gain:', list(map(key, seq)))
    return max(randomize(seq), key=key)

def information_content(values):
    """Number of bits to represent the probability distribution in values."""
    probabilities = normalize([x for x in values if x != 0])
    return sum(-p * np.log2(p) for p in probabilities)


def count(attr, val, examples):
    """Count the number of examples that have example[attr] = val."""
    return sum(e[attr] == val for e in examples)


def randomize(seq):
    """Randomize a copy of list."""
    items = list(seq)
    random.shuffle(items)
    return items


def normalize(dist):
    """Multiply each number by a constant such that the sum is 1.0"""
    if isinstance(dist, dict):
        total = sum(dist.values())
        for key in dist:
            dist[key] = dist[key] / total
        return dist
    total = sum(dist)
    return [(n / total) for n in dist]
