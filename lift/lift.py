class Lift:

    def desired_floor(self, target, stop_list):

        desired = -1
        dist = target  # assume no elevator and no stops
        minimum = dist

        for stop_level in stop_list:
            dist = target - stop_level
            if abs(dist) < minimum:
                desired = stop_level
                minimum = dist

        print ("minimum: ", minimum, "desired: ", desired)

        return desired
