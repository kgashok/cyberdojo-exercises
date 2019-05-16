import gift
import unittest

class TestGift(unittest.TestCase):

    def test_returns_TrueFor2_ABoxOnTheEdge_For3by3_box(self):
        gb     = gift.Box(3, 3)
        box_id = 2
        self.assertEqual("yes", gb.is_damaged(box_id) )

    def test_returns_TrueFor11_ABoxOnTheEdge_For3by3_box(self):
        gb     = gift.Box(3, 3)
        box_id = 2+9
        self.assertEqual("yes", gb.is_damaged(box_id) )

    def test_returns_TrueFor14_WhichIsInCentre_For3by3_box(self):
        gb     = gift.Box(3, 3)
        box_id = 14
        self.assertEqual("no", gb.is_damaged(box_id) )

    def test_returns_True_for_5_for_7by6_box(self):
        gb     = gift.Box(7, 6)
        box_id = 5
        self.assertEqual("yes", gb.is_damaged(box_id) );
        box_id = 7
        self.assertEqual("yes", gb.is_damaged(box_id) );


    def test_returns_True_for_5_for_7by6_box(self):
        gb     = gift.Box(7, 6)
        box_id = 43
        self.assertEqual("yes", gb.is_damaged(box_id) );
        box_id = 421
        self.assertEqual("yes", gb.is_damaged(box_id) );
        box_id = 211
        self.assertEqual("yes", gb.is_damaged(box_id) );
        box_id = 210
        self.assertEqual("yes", gb.is_damaged(box_id) );

    def test_returns_False_for_42_for_7by6_reinforced_box(self):
        gb = gift.Box(7, 6)
        gb.corners_reinforced()
        box_id = 42
        self.assertEqual("no", gb.is_damaged(box_id) );

    def test_returns_True_for_5_for_7by6_box_weak_only_at_the_corners(self):
        gb = gift.Box(7, 6)
        gb.all_reinforced().corners_weakened()

        box_id =  37  # Bottom left corner
        self.assertEqual("yes", gb.is_damaged(box_id) );
        box_id =  14   # at the Edge
        self.assertEqual("no", gb.is_damaged(box_id) );



if __name__ == '__main__':
    unittest.main()