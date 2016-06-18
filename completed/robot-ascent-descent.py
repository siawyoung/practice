
# A robot needs to travel along a path that includes several ascents and descents. When it goes up, it uses its battery to power the motor and when it descends, it recovers the energy which is stored in the battery. The battery recharging process is ideal: on descending, every Joule of gravitational potential energy converts to a Joule of electrical energy which is stored in the battery. The battery has a limited capacity and once it reaches this capacity,the energy generated in descending is lost.

# Design an algorithm that takes a sequence of n height coordinates to be traversed, and returns the minimum battery capacity needed to complete the journey. The robot begins with a fully charged battery.

# The minimum required battery is just the maximum difference in an array:

# max_diff :: [Int] -> Int

def max_diff(arr):

    if len(arr) <= 0:
        return -1

    _min = arr[0]
    _max = arr[0]

    for i in arr:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

    return _max - _min

print(max_diff([1,3,-1]))

