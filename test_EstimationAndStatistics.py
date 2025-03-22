import unittest
import numpy as np
from estimationAndStatistics import mean, variance, leastSquaresEstimate


# Sample values to test
prices = [8.4, 9.0, 9.4, 9.8, 10.2]
years = [2016, 2018, 2020, 2022, 2024]


class TestEstimationAndStatistics(unittest.TestCase):
    def testMean(self):
        # Test if the mean function calulates the right mean
        self.assertAlmostEqual(mean(prices), 9.36)

    def testVariance(self):
        # Test if the varaince function calculates the right variance
        self.assertAlmostEqual(variance(prices), 0.488)

    def testEstimation(self):
        # Test if the estimation function calulates the right answer
        self.assertAlmostEqual(leastSquaresEstimate(years, prices, 2028), 11.12)
