"""
This module implements the random undersampling
"""

import numpy as np

from ..base import UnderSampling

class RandomUndersampling(UnderSampling):
    """
    The random undersampling
    """
    def __init__(self, random_state=None):
        """
        The constructor of the random undersampling

        Args:
            random_state (None|int|np.random.RandomState): the random seed or state to be used
        """
        UnderSampling.__init__(self, random_state=random_state)

    @classmethod
    def parameter_combinations(cls, raw=False):
        """
        Generates reasonable parameter combinations.

        Returns:
            list(dict): a list of meaningful parameter combinations
        """

        return cls.generate_parameter_combinations({}, raw=raw)

    def sample(self, X, y):
        """
        Carry out the undersampling

        Args:
            X (np.array): the feature vectors
            y (np.array): the corresponding class labels

        Returns:
            np.array, np.array: the undersampled feature vectors and class labels
        """
        n_maj, n_min = np.bincount(y)
        mask = self.random_state.choice(np.arange(n_maj), n_min, replace=False)
        X_maj = X[y == 0][mask]

        return np.vstack([X_maj, X[y == 1]]), np.hstack([np.repeat(0, n_min), np.repeat(1, n_min)])