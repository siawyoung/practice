# Returns the maximum value of the knapsack

# _0_1_knapsack :: [Int] -> [Int] -> Int -> Int
def _0_1_knapsack(values, weights, capacity):

    number_of_items = len(values)
    table = []

    for i in range(number_of_items):
        table.append([None] * capacity)

    for j in range(capacity):
        table[0][j] = 0

    for i in range(1, number_of_items):
        for j in range(capacity):
            if weights[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-weights[i-1]] + values[i-1])

    return table[-1][-1]

values  = [3,5,1,2,4,6,3,2,4]
weights = [1,2,4,6,1,6,2,3,4]
capacity = 10

print(_0_1_knapsack(values, weights, capacity)) # 17