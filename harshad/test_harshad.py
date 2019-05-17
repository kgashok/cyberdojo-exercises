import harshad
import unittest

class TestHarshad(unittest.TestCase):

    def test_201_is_a_harshad(self):
        hchecker = harshad.Harshad()
        self.assertEqual(True, hchecker.check(201) )

    def test_201_is_a_strong_harshad(self):
        shchecker = harshad.StrongHarshad()
        self.assertEqual(True, shchecker.check(201) )

    def test_12_is_NOT_a_strong_harshad(self):
        shchecker = harshad.StrongHarshad()
        self.assertEqual (False, shchecker.check(12) )

    def test_bignumber_is_a_harshad(self):
        hchecker = harshad.Harshad()
        self.assertEqual(True, hchecker.check(2162049150) )

    def test_bignumber_is_NOT_a_strong_harshad(self):
        shchecker = harshad.StrongHarshad()
        self.assertEqual (False, shchecker.check(2162049150) )


    def test_all_harshads(self):

        hc = harshad.Harshad()
        shc = harshad.StrongHarshad()

        print ("Harshad Numbers---------")
        for i in range (10, 1001):
            if hc.check(i): print (i, end=" ")

        print ("\nStrong Harshad Numbers---------")
        for i in range (10, 2001):
            if shc.check(i): print (i, end=" ")

        self.assertTrue(True)

if __name__ == '__main__':

    unittest.main()