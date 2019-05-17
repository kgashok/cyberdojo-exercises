import pangram
import unittest

class TestPG(unittest.TestCase):

    def test_quick_brown_fox_jumped_over_the_fence_as_TRUE(self):
        pc = pangram.Checker()
        sentence = "A quick brown fox jumps over the lazy dog."
        self.assertEqual(True, pc.test(sentence))

    def test_quick_brown_fox_jumped_over_the_fence_as_FALSE(self):
        pc = pangram.Checker()
        sentence = "A quick brown fox jumps over the dog."
        self.assertEqual(False, pc.test(sentence))

    def test_from_pangrams_list (self):
        #
        # from http://clagnut.com/blog/2380/
        #
        sentence = "Sympathizing would fix Quaker objectives."
        pc = pangram.Checker()
        self.assertEqual(True, pc.test(sentence))


if __name__ == '__main__':
    unittest.main()