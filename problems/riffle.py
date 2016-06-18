
# Check if a list is a riffle of 2 lists.

# A list that is a riffle of 2 lists means that the list will have a bit of list 1, a bit of list 2, then a bit of list 1 etc, like shuffling a card deck by splitting it into two halves and using both thumbs to mix it together.

# The approach uses dynamic programming for a linear time solution.

# We memoize all the possible ways to take from each list at each step. For a current iteration, if there are no possible ways for the previous iteration, we can halt the algorithm prematurely.

# The solution will be whether there are any possible solutions for the last entry in the table.

def check_riffle(full_list, list1, list2):
    table = [ [] for _ in range(len(full_list)) ]

    if list1[0] == full_list[0]:
            table[0].append((0, -1))

    if list2[0] == full_list[0]:
        table[0].append((-1, 0))

    for i in range(1, len(full_list)):
        curr_candidates = table[i - 1]
        if not curr_candidates:
            return False

        for cand in curr_candidates:
            if cand[0] < len(list1) - 1 and list1[cand[0] + 1] == full_list[i]:
                table[i].append((cand[0] + 1, cand[1]))
            if cand[1] < len(list2) - 1 and list2[cand[1] + 1] == full_list[i]:
                table[i].append((cand[0], cand[1] + 1))


    return bool(table[-1])

full = [1,4,5,2,4,8,1,8,0,0]

list1 = [1,4,5,8,0]
list2 = [2,4,1,8,0]

print(check_riffle(full, list1, list2))
