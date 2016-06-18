
# Design an efficient algorithm for computing the skyline.

# assume that the starting x-coordinate is 0

# skyline :: [[Int, Int, Int]] -> [Int]
def skyline(buildings):

    def _skyline_from_building(building):
        skyline = [0] * (building[1] + 1)
        skyline[building[0]:building[1] + 1] = [building[2]] * (building[1] - building[0] + 1)
        return skyline

    if not buildings:
        return []
    if len(buildings) == 1:
        return _skyline_from_building(buildings[0])

    def merge(b1, b2):
        if len(b1) == 1:
            skyline_1 = _skyline_from_building(b1[0])
        else:
            skyline_1 = merge(b1[:len(b1) // 2], b1[len(b1) // 2:])

        if len(b2) == 1:
            skyline_2 = _skyline_from_building(b2[0])
        else:
            skyline_2 = merge(b2[:len(b2) // 2], b2[len(b2) // 2:])

        longer_skyline = skyline_1 if len(skyline_1) > len(skyline_2) else skyline_2
        shorter_skyline = skyline_1 if longer_skyline == skyline_2 else skyline_2

        output = longer_skyline
        # combine 2 skylines together
        for i in range(len(shorter_skyline)):
            output[i] = max(longer_skyline[i], shorter_skyline[i])

        return output


    return merge(buildings[:len(buildings) // 2], buildings[len(buildings) // 2:])

# expected
# [] -> []
# [[0, 2, 1]] -> [1,1,1]
# [[0,2,1],[1,3,2]] -> [1,2,2,2]
# [[0,3,1], [1,6,3], [4,8,4], [5,9,2], [7,14,3], [10,12,6], [11,17,1], [13,16,2]]

# print(skyline([[0,2,1],[1,3,2]]))
print(skyline([[0,3,1], [1,6,3], [4,8,4], [5,9,2], [7,14,3], [10,12,6], [11,17,1], [13,16,2]]))