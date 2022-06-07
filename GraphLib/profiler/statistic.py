import math
import numpy as np
import warnings
import scipy.stats as st


class Statistic:
    def __init__(self, array):
        self.array = array
        self.avg = sum(array) / len(array)
        self.minimum = min(array)
        self.maximum = max(array)
        self.precision = 0.95
        self.std_deviation = self.calculate_standard_deviation()
        self.confidence_interval = self.calculate_confidence_interval()

    def calculate_standard_deviation(self):
        s = 0
        for val in self.array:
            s += (val - self.avg) * (val - self.avg)

        return math.sqrt(s / (len(self.array) - 1))

    def calculate_confidence_interval(self):
        warnings.simplefilter("ignore", RuntimeWarning)
        interval = st.t.interval(alpha=self.precision, df=len(self.array) - 1,
                                 loc=np.mean(self.array),
                                 scale=st.sem(self.array))
        return interval[1] - interval[0]
