import statues
import unittest


class TestStatues(unittest.TestCase):

    def test_one_off_example(self):

        equalizer = statues.Statues()
        input = [4, 3, 3, 2, 4]
        self.assertEqual(1, equalizer.steps_required(input))

    def test_seven_rooms_test_case(self):

        equalizer = statues.Statues()
        input = [7, 6, 5, 4, 1, 2, 7, 5]
        self.assertEqual(5, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [4, 1, 1, 1, 1]
        self.assertEqual(0, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [4, 1, 2, 3, 4]
        self.assertEqual(1, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(10, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
        self.assertEqual(0, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11]
        self.assertEqual(9, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [5, 45, 23, 11, 2, 33]
        self.assertEqual(31, equalizer.steps_required(input))

    def test_no_steps_required(self):
        equalizer = statues.Statues()
        input = [6, 6, 0, 0, 0, 0, 0]
        self.assertEqual(5, equalizer.steps_required(input))


if __name__ == '__main__':
    unittest.main()
