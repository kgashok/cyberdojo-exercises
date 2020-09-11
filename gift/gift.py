class Box:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b
        self.size = l * b

        self.topLeft = 1
        self.topRight = self.breadth
        self.bottomRight = self.size
        self.bottomLeft = self.size - self.breadth + 1

        self.corner_list = [self.topLeft, self.topRight,
                            self.bottomLeft, self.bottomRight]
        self.safe = self.safe_locations()

    def safe_locations(self):
        slist = []
        loc_id = 1
        for i in range(1, self.length+1):
            for j in range(1, self.breadth+1):
                if (i != 1 and i != self.length) and \
                   (j != 1 and j != self.breadth):
                    slist.append(loc_id)
                loc_id += 1

        print ("\nsafe_list for {0}x{0}: ".
               format(self.length, self.breadth),
               sorted(slist))
        return slist

    def is_damaged(self, box_id):
        loc_id = box_id if box_id <= self.size else box_id % self.size
        print ("checking box({0}) at loc_id:".format(box_id), loc_id)
        return "yes" if loc_id not in self.safe else "no"

    def corners_reinforced(self):
        self.safe += self.corner_list

    def corners_weakened(self):
        [self.safe.remove(x) for x in self.corner_list]
        return self

    def all_reinforced(self):
        self.safe = []
        self.safe += range(1, self.size+1)
        return self
