
# In the pick-up-coins game, an even number of coins are placed in a line, as in Figure 4.6 on Page 44. Two players, F and S, take tums at choosing one coin each- they can only choose from the two coins at the ends of the line. Player F goes first. The game ends when all the coins have been picked up. The player whose coins have the higher total value wins. A player cannot pass his turn.

# Design an efficient algorithm for computing the maximum margin of victory for the starting player in the pick-up-coins game.

# maximum_margin :: [Int] -> Int
def maximum_margin(arr):
    table = [ [ None for y in range(len(arr)) ] for x in range(len(arr)) ]

    def calculate_max_margin(a, b):
        if a > b:
            return 0

        if not table[a][b]:

            # assuming that the opponent always picks the best option available
            max_if_pick_left = arr[a] + min(calculate_max_margin(a + 1, b - 1), calculate_max_margin(a + 2, b))
            max_if_pick_right = arr[b] + min(calculate_max_margin(a, b - 2), calculate_max_margin(a + 1, b - 1))

            table[a][b] = max(max_if_pick_left, max_if_pick_right)

        return table[a][b]

    return calculate_max_margin(0, len(arr) - 1)

# arr = [1,5,2,2,1,2,17,9,4,2,3,5,16]

arr = [1,5,2,3,1,3]

print(maximum_margin(arr))