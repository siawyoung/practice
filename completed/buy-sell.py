
# Given an array of stock prices, if you can buy once, then sell once, find the most profit you can make.

# This idea is to first preprocess the array from right to left, keeping track of the maximum (sell) point from that point onwards. Then we iterate through from left to right, checking which generates the largest difference.

# This takes 2 linear passes and O(n) auxilliary space.

# buy_then_sell :: [Int] -> (Int, Int)
def buy_then_sell(arr):
    max_at_point = []
    _max = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > _max:
            _max = arr[i]
            max_at_point = [(_max, i)] + max_at_point
        else:
            max_at_point = [max_at_point[0]] + max_at_point

    max_difference = 0
    best_buying_point = 0

    for i in range(len(arr) - 1):
        if max_at_point[i+1][0] - arr[i] >= max_difference:
            max_difference = max_at_point[i+1][0] - arr[i]
            best_buying_point = i

    return (best_buying_point, max_at_point[best_buying_point + 1][1])

arr = [3,1,4,1,2,1,2,6,3,0]
print(buy_then_sell(arr))
