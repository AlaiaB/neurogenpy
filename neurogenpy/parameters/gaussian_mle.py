"""
Gaussian maximum likelihood estimation module.
"""

# Computational Intelligence Group (CIG). Universidad Politécnica de Madrid.
# http://cig.fi.upm.es/
# License:

from collections import namedtuple

import numba
import numpy as np

from .learn_parameters import LearnParameters


class GaussianMLE(LearnParameters):
    """
    Gaussian maximum likelihood estimation.
    """

    def run(self, env='neurogenpy'):
        """
        Learns the parameters of the network using Gaussian maximum likelihood
        estimation.

        Parameters
        ----------
        env : str, default='neurogenpy'
            Environment used to learn the parameters.

        Returns
        -------
        dict
            A dictionary with the nodes IDs as keys and GaussianNode objects
            as values.

        Raises
        ------
        ValueError
            If the environment is not supported.
        """

        if env == 'neurogenpy':
            return self._run_neurogenpy()
        else:
            raise ValueError(f'{env} environment is not supported.')

    def _run_neurogenpy(self):
        nodes = self.data.columns.values.tolist()

        n = len(nodes)
        mu = np.zeros(n)
        sigmas = np.zeros(n)
        parents_coeffs = []
        parents = []

        for i, node in enumerate(nodes):
            node_parents = [pred for pred in self.graph.predecessors(node)]
            parents.append(node_parents)

            y = self.data.loc[:, node].values.reshape(self.data.shape[0],
                                                      -1).astype(float)

            if not node_parents:
                mean = y.mean()
                variance = y.var()
                parents_coeffs.append([])
            else:
                x = self.data.loc[:, node_parents].values.reshape(
                    self.data.shape[0], -1)
                variance, coeffs = _linear_gaussian(x, y)
                mean = coeffs[-1]
                parents_coeffs.append(coeffs[:-1])

            mu[i] = mean
            sigmas[i] = variance

        return mu, sigmas, parents_coeffs, parents, nodes


GaussianNode = namedtuple('GaussianNode',
                          ('mean', 'var', 'parents', 'parents_coeffs'))


@numba.jit(nopython=True, fastmath=True)
def _linear_gaussian(x, y):
    """
    Computes the linear regression of a variable `y` on a set of variables `x`.
    """

    n = x.shape[0]
    x = np.ascontiguousarray(x).reshape(n, -1)
    k = x.shape[1]
    y = np.ascontiguousarray(y).reshape(n, -1)

    if k == 0:
        return None

    # Bias is the last column of ones
    a = np.ones((n, k + 1), dtype=np.float64)
    a[:, :k] = x

    result_lr = np.linalg.lstsq(a, y)
    w = result_lr[0]

    y_pred = np.dot(w.T, a.T)
    residuals = y - y_pred.T
    mean_sq_error = np.sum(np.square(residuals)) / n

    return mean_sq_error, list(w.flatten())
