import unittest
import lift


class TestLift(unittest.TestCase):

    def test_must_return_10_for4_10_15_as_input(self):
        alift = lift.Lift()
        self.assertEqual(10, alift.desired_floor(10, [4, 10, 15]))

    # 10 4 8 15 output -> 8
    def test_must_return_8_for4_8_15_as_input(self):
        alift = lift.Lift()
        self.assertEqual(8, alift.desired_floor(10, [4, 8, 15]))

    # 10 4 8 12 output -> 12
    def test_must_return12_for_4_8_12_as_input(self):
        alift = lift.Lift()
        self.assertEqual(12, alift.desired_floor(12, [4, 8, 12]))

    # 130 10 200 600 output -> 200
    def test_must_return10_for_10_200_600_as_input(self):
        alift = lift.Lift()
        self.assertEqual(200, alift.desired_floor(130, [10, 200, 600]))

    # A test case where it is better to walk
    # 20 100 200 300 output -> -1
    def test_must_returnMinus1_for_100_200_300_and_20_as_desired(self):
        alift = lift.Lift()
        self.assertEqual(-1, alift.desired_floor(20, [100, 200, 300]))

    # A test case where you arrive below ground level, at basement
    # 2, (int[]){4, 8, 12}, 3, -2
    def test_must_return4_for_4_8_12_and_2_as_desired_when_start_at_B2(self):
        alift = lift.Lift()
        self.assertEqual(4, alift.desired_floor(2, [4, 8, 12], -2))


if __name__ == '__main__':
    unittest.main()
