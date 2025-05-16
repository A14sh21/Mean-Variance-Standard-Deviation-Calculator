import unittest
#from mean_var_std import calculate  # or adjust import as needed

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        
        expected_means = [
            [3.6666666666666665, 5.0, 3.0],
            [3.3333333333333335, 4.0, 4.333333333333333],
            3.888888888888889
        ]
        expected_variances = [
            [9.555555555555555, 0.6666666666666666, 8.666666666666666],
            [3.5555555555555554, 10.666666666666666, 6.222222222222222],
            6.987654320987654
        ]
        expected_stddevs = [
            [3.0912061651652345, 0.816496580927726, 2.943920288775949],
            [1.8856180831641267, 3.265986323710904, 2.494438257849294],
            2.6434171674156266
        ]
        expected_ints = {
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        }

        for i in range(3):
            if isinstance(actual['mean'][i], list):
                for j in range(len(actual['mean'][i])):
                    self.assertAlmostEqual(actual['mean'][i][j], expected_means[i][j], places=10)
                    self.assertAlmostEqual(actual['variance'][i][j], expected_variances[i][j], places=10)
                    self.assertAlmostEqual(actual['standard deviation'][i][j], expected_stddevs[i][j], places=10)
            else:
                self.assertAlmostEqual(actual['mean'][i], expected_means[i], places=10)
                self.assertAlmostEqual(actual['variance'][i], expected_variances[i], places=10)
                self.assertAlmostEqual(actual['standard deviation'][i], expected_stddevs[i], places=10)

        self.assertEqual(actual['max'], expected_ints['max'])
        self.assertEqual(actual['min'], expected_ints['min'])
        self.assertEqual(actual['sum'], expected_ints['sum'])

    def test_calculate2(self):
        actual = calculate([9,1,5,3,3,3,2,9,0])

        expected_means = [
            [4.666666666666667, 4.333333333333333, 2.6666666666666665],
            [5.0, 3.0, 3.6666666666666665],
            3.888888888888889
        ]
        expected_variances = [
            [9.555555555555555, 11.555555555555555, 4.222222222222222],
            [10.666666666666666, 0.0, 14.888888888888891],
            9.209876543209875
        ]
        expected_stddevs = [
            [3.091206165165235, 3.39934634239519, 2.0548046676563256],
            [3.265986323710904, 0.0, 3.8586123009300755],
            3.0347778408328137
        ]
        expected_ints = {
            'max': [[9, 9, 5], [9, 3, 9], 9],
            'min': [[2, 1, 0], [1, 3, 0], 0],
            'sum': [[14, 13, 8], [15, 9, 11], 35]
        }

        for i in range(3):
            if isinstance(actual['mean'][i], list):
                for j in range(len(actual['mean'][i])):
                    self.assertAlmostEqual(actual['mean'][i][j], expected_means[i][j], places=10)
                    self.assertAlmostEqual(actual['variance'][i][j], expected_variances[i][j], places=10)
                    self.assertAlmostEqual(actual['standard deviation'][i][j], expected_stddevs[i][j], places=10)
            else:
                self.assertAlmostEqual(actual['mean'][i], expected_means[i], places=10)
                self.assertAlmostEqual(actual['variance'][i], expected_variances[i], places=10)
                self.assertAlmostEqual(actual['standard deviation'][i], expected_stddevs[i], places=10)

        self.assertEqual(actual['max'], expected_ints['max'])
        self.assertEqual(actual['min'], expected_ints['min'])
        self.assertEqual(actual['sum'], expected_ints['sum'])

    def test_calculate_with_few_digits(self):
        with self.assertRaises(ValueError):
            calculate([2, 6, 2, 8, 4, 0, 1])  # fewer than 9

# Optional to run in a script
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
