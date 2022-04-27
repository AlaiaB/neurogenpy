from abc import ABCMeta, abstractmethod


class JointDistribution(metaclass=ABCMeta):
    """
    Abstract class for joint probability distributions.
    """

    def __init__(self):
        pass

    @abstractmethod
    def from_parameters(self, parameters, order):
        """
        Computes the joint probability distribution given the topological order
        of some nodes and their parameters.

        Parameters
        ----------
        parameters : dict
            Parameters of the nodes.

        order : list
            Topological order of the nodes.

        Returns
        -------
        self : JointDistribution
            The joint probability distribution.
        """

    @abstractmethod
    def marginal(self, nodes, marginal_nodes):
        """
        Retrieves the marginal distribution parameters for a set of nodes.

        Parameters
        ----------
        nodes : list
            Full set of nodes in the joint distribution.

        marginal_nodes : list
            Set of nodes whose marginal distribution will be computed.

        Returns
        -------
        JointDistribution
            The marginal distribution.
        """

    @abstractmethod
    def condition(self, evidence, order):
        """
        Conditions a joint probability distribution on some evidence.

        Parameters
        ----------
        order : list
            Topological order of the nodes.

        evidence : dict
            The evidence to use for conditioning the distribution. The keys are
            nodes and the values the observed value for them.
        """

    def clear(self):
        """
        Clears the distribution.
        """

        keys = self.__dict__.keys()
        for k in keys:
            setattr(self, k, None)
