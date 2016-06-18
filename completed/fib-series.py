
# zero-indexed fibonacci series, DP version.

def fib(n):

    if n <= 1:
        return n

    table = [0,1]
    for i in range(n):
        table.append(table[i + 1] + table[i])

    return table[-1]

print(fib(10))
