from rpy2.robjects.packages import importr

from .LearnStructure import LearnStructure


class FastIamb(LearnStructure):
    """Fast.iamb structure learning class."""

    def __init__(self, data, alpha, data_type=None,
                 states_names=None):
        """
        Fast.iamb structure learning constructor.
        @param data: DataFrame with the learning sample from which to infer the
            network.
        @type data: Pandas DataFrame.
        @param data_type: Type of the data introduced: continuous, discrete or
            hybrid.
        @param alpha:
        @param states_names: Dictionary with the set of states each variable
            takes in the input data.
        """
        super(FastIamb, self).__init__(data, data_type, states_names)
        self.alpha = alpha

    def run(self, backend="bnlearn"):
        """

        @param backend:
        @return:
        """
        if backend == "neurosuites":
            model = self.run_fast_iamb_neurosuites()
        elif backend == "bnlearn":
            model = self.run_bnlearn(importr("bnlearn").fast_iamb,
                                     self.alpha)

        return model

    def run_fast_iamb_neurosuites(self):

        return 0
