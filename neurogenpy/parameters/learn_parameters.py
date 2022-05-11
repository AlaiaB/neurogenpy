"""
Parameters learning base module.
"""

# Computational Intelligence Group (CIG). Universidad Politécnica de Madrid.
# http://cig.fi.upm.es/
# License:

from abc import ABCMeta, abstractmethod

from networkx import to_numpy_matrix


class LearnParameters(metaclass=ABCMeta):
    """
    Base class for all learn parameters classes.

    Parameters
    ----------
    data : pandas DataFrame
        Input data used to learn the parameters from.

    graph : networkx.DiGraph
        Structure of the Bayesian network.
    """

    def __init__(self, data, graph, **_):
        self.data = data
        self.graph = graph

    @abstractmethod
    def run(self):
        """
        Learns the parameters of the Bayesian network.
        """
