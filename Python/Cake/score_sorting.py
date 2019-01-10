# https://www.interviewcake.com/question/python/top-scores?course=fc1&section=hashing-and-hash-tables
# Write a function that takes:
#
# a list of unsorted_scores
# the highest_possible_score in the game

unsorted_scores = [37, 89, -1, -10, -20, 41, 65, 91, 53, 91, 91, 41, 65]
HIGHEST_POSSIBLE_SCORE = 100


def sort_scores(scores, highest_possible_score):
    lowest_possible_score = -20
    score_counts = [0] * ((highest_possible_score + 1) - lowest_possible_score)
    for score in scores:
        score_counts[score - lowest_possible_score] += 1

    current_index = 0
    for index, score_count in enumerate(score_counts):
        for count in range(score_count):
            scores[current_index] = index + lowest_possible_score
            current_index += 1


sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
print(unsorted_scores)



