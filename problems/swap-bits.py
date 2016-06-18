
# A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant bit, and the bit at index 63 corresponding to the most significant bit. Implement code that takes as input a 64-bit integer x and swaps the bits at indices i and j.

# swap_bits :: Int -> Int -> Int -> Int
def swap_bits(num, i, j):

    # check if bits i and j are even different in the first place. if they are not different, we can just return the number as-is
    # we check the bits i and j by right-shifting the number until we reach that number, and ANDing it with 1 (...000001), which
    # clears all the bits but the last

    if num >> i & 1 != num >> j & 1:

        # we construct 2 1's, then left shift them to their correct positions, and then we OR them together to combine them
        # then, we XOR the num with our constructed 1s to flip their bits

        # remember: XOR-ing by 1 achieves bit flipping

        # In this example, the second integer was constructed by left shifting and OR-ing them together
        #   00101 ^
        #   01001
        # = 01100

        num ^= (1 << i) | (1 << j)

    return num