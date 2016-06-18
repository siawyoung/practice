
# Given denominations of 10, 20 and 50, find the total number of ways to make up an amount.

def count_change(amount, n):

    if n == 1:
        denoms = [10]
    elif n == 2:
        denoms = [10,20]
    else:
        denoms = [10,20,50]

    counts = 0
    for index, denom in enumerate(denoms):
        if denom == amount:
            counts += 1
        elif denom < amount:
            counts += count_change(amount - denom, index + 1)
    return counts

print(count_change(50, 3))
print(count_change(50, 1))
print(count_change(50,2))
print(count_change(400, 3))
