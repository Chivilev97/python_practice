import unittest
import computing_statistics as cs


class ComputingStatisticsTest(unittest.TestCase):
    def test_standard_deviation(self):
        numbers = [100, 200, 1000, 155]
        result = cs.standard_deviation(numbers)
        self.assertAlmostEqual(369.04, result, 2)
        numbers = [100, 200, 1000, 300]
        result = cs.standard_deviation(numbers)
        self.assertAlmostEqual(353.55, result, 2)
        numbers = [0, 0, 0]
        result = cs.standard_deviation(numbers)
        self.assertAlmostEqual(0, result, 2)
        numbers = []
        self.assertRaises(ValueError, cs.standard_deviation, numbers)


if __name__ == '__main__':
    unittest.main()
