
# Given "n", generate all valid parenthesis strings of length "2n".

# Example:
# Given n=2

# Output:
# (())
# ()()

def print_all_parenthesis(stack, history, iterations_left):

    if iterations_left == 0:
        if not stack:
            print(history)

    else:
        if not stack:
            print_all_parenthesis(stack + [1], history + '(', iterations_left - 1)
        else:
            print_all_parenthesis(stack + [1], history + '(', iterations_left - 1)
            print_all_parenthesis(stack[:-1], history + ')', iterations_left - 1)


print_all_parenthesis([], '', 6)
