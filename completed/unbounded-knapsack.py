
# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

# For example:

#   cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20

# max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)

# Runs in O(nW) time, where W is the capacity (pseudo-polynomial because W is not a polynomial to the number of items)

# we can use just a 1 dimensional table for this

def max_duffel_bag_value(cake_tuples, capacity):

    table = [0]

    for w in range(1, capacity + 2):

        candidates = [0]

        for cake in cake_tuples:
            if w > cake[0]:
                candidates.append(table[w - cake[0]] + cake[1])

        table.append(max(candidates))

    return table[-1]

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print(max_duffel_bag_value(cake_tuples, capacity))

