
# There is an island which is represented by square matrix NxN.
# A person on the island is standing at any given co-ordinates (x,y). He can move in any direction one step right, left, up, down on the island. If he steps outside the island, he dies.

# Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix) & person is standing at given co-ordinates (x,y). He is allowed to move n steps on the island (along the matrix). What is the probability that he is alive after he walks n steps on the island?


# get_prob :: Int -> [Int, Int] -> Int -> Float

def get_prob(island_size, coordinates, steps):

    if steps <= 0:
        return 1

    # up right down left
    # True if got land, False if water
    def check_surroundings(coordinates):
        output = [None] * 4
        i, j = coordinates
        output[0] = True if i > 0 else False
        output[1] = True if j < island_size - 1 else False
        output[2] = True if i < island_size - 1 else False
        output[3] = True if j > 0 else False

        return output

    def _get_prob(coordinates, steps):

        i, j = coordinates
        surroundings = check_surroundings(coordinates)

        if steps == 1:

            return surroundings.count(True) * 0.25

        else:
            probability = 0
            if surroundings[0]:
                probability += 0.25 * _get_prob([i - 1, j], steps - 1)
            if surroundings[1]:
                probability += 0.25 * _get_prob([i, j + 1], steps - 1)
            if surroundings[2]:
                probability += 0.25 * _get_prob([i + 1, j], steps - 1)
            if surroundings[3]:
                probability += 0.25 * _get_prob([i, j - 1], steps - 1)

            return probability



    return _get_prob(coordinates, steps)

print(get_prob(3, [1,0], 2))
