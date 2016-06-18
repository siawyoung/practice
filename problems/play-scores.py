
# You have an aggregate score 5 and W which specifies the points that can be scored in an individual play. How would you find the number of combinations of plays that result in an aggregate score of s? How would you compute the number of distinct sequences of individual plays that result in a score of s7

possible_scores = [2,3,5]

score = 5

def count_combinations(possible_scores, final_score):
    table_of_scores = [0] * (final_score + 1)

    table_of_scores[0] = 1

    for score in possible_scores:
        for i in range(score, final_score + 1):
            table_of_scores[i] += table_of_scores[i - score]

    return table_of_scores[final_score]

print(count_combinations(possible_scores, score))