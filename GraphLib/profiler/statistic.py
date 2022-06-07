import math


t_param_values = {
    6: 2.5702,
    11: 2.2281,
    16: 2.1314,
    21: 2.0860,
    26: 2.0555,
    31: 2.0423,
    36: 2.0301,
    41: 2.0211,
    51: 2.0086,
    101: 1.9840
}


class Statistic:
    def __init__(self, array):
        self.array = array
        self.avg = sum(array) / len(array)
        self.minimum = min(array)
        self.maximum = max(array)
        self.std_deviation = self.calculate_standard_deviation()
        self.confidence_interval = self.calculate_confidence_interval()

    def calculate_standard_deviation(self):
        s = 0
        for val in self.array:
            s += (val - self.avg) * (val - self.avg)

        return math.sqrt(s / (len(self.array) - 1))

    def calculate_confidence_interval(self):
        n = len(self.array)
        if n not in t_param_values:
            n = 6
        return t_param_values[n] * self.std_deviation / math.sqrt(len(self.array))
