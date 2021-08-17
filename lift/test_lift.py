import lift
import unittest


class TestLift(unittest.TestCase):

    def test_must_return_10_for4_10_15_as_input(self):
        liftO = lift.Lift()
        self.assertEqual(10, liftO.desired_floor(10, [4, 10, 15]))

    # 10 4 8 15 output -> 8
    def test_must_return_8_for4_8_15_as_input(self):
        liftO = lift.Lift()
        self.assertEqual(8, liftO.desired_floor(10, [4, 8, 15]))

    # 10 4 8 12 output -> 12
    def test_must_return12_for_4_8_12_as_input(self):
        liftO = lift.Lift()
        self.assertEqual(12, liftO.desired_floor(12, [4, 8, 12]))

    # 130 10 200 600 output -> 200
    def test_must_return10_for_10_200_600_as_input(self):
        liftO = lift.Lift()
        self.assertEqual(200, liftO.desired_floor(130, [10, 200, 600]))

    # A test case where it is better to walk
    # 20 100 200 300 output -> -1
    def test_must_returnMinus1_for_100_200_300_and_20_as_desired(self):
        liftO = lift.Lift()
        self.assertEqual(-1, liftO.desired_floor(20, [100, 200, 300]))


if __name__ == '__main__':
    unittest.main()
