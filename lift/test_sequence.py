import sequence
import unittest


class TestSequence(unittest.TestCase):

    def test_generate_sequence(self):
        print ("Sequence Generation upto 10")

        expected = [2, 5, 9, 19, 37]
        self.assertEqual(expected, sequence.generate(10)[:5])

        expected = [2, 5, 9, 19, 37, 75]
        self.assertEqual(expected, sequence.generate(10)[:6])


if __name__ == '__main__':
    unittest.main()
