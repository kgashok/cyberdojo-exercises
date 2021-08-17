class Statues:
    def steps_required(self, nlist):

        no_of_rooms = nlist[0]
        slist = nlist[1:]  # count of statues

        # Arrive at the equalizing value
        total = sum(slist)
        print ("Total: ", total)
        equal = int(total / no_of_rooms)
        print ("Equal value: ", equal)

        steps = sum([(equal-e) for e in slist if equal > e])
        print (steps)

        return steps

    def check_if_all_equal(self, slist, equal):
        for e in slist:
            if e < equal:
                return False
        return True

    def steps_required_legacy(self, nlist):

        no_of_rooms = nlist[0]
        slist = nlist[1:]  # count of statues

        # Arrive at the equalizing value
        total = sum(slist)
        print ("Total: ", total)
        equal = int(total / no_of_rooms)
        print ("Equal value: ", equal)

        steps = 0
        inventory = 0
        while True:
            if self.check_if_all_equal(slist, equal):
                break
            for i in range(no_of_rooms):
                if slist[i] < equal:
                    req = equal - slist[i]
                    inventory -= req
                    slist[i] = equal
                    steps += req
                elif slist[i] > equal:
                    avail = slist[i] - equal
                    inventory += avail
                    slist[i] = equal
                    steps += 1

            print ("Steps: ", steps, inventory, slist)

        return steps-1
