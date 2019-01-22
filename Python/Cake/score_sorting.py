# https://www.interviewcake.com/question/python/top-scores?course=fc1&section=hashing-and-hash-tables
# Write a function that takes:
#
# a list of unsorted_scores
# the highest_possible_score in the game
# You created a game that is more popular than Angry Birds.
#
# Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest.
# So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time,
# but players are complaining that their rankings aren't updated fast enough.
# You need a faster sorting algorithm.
#
# Write a function that takes:
#
# a list of unsorted_scores
# the highest_possible_score in the game
# and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.

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


# sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# print(unsorted_scores)


unsorted_scores_2 = [37, 89, 37, 0, 91, 41, 100, 65, 91, 53, 53]


def top_scores(score_list, highest_possible_score):
    lowest_possible_score = 0
    score_frequencies = [0] * ((highest_possible_score + 1) - lowest_possible_score)
    for score in score_list:
        score_frequencies[score] += 1

    sorted_scores = []
    for index in range(len(score_frequencies)-1, -1, -1):
        count = score_frequencies[index]
        while count:
            sorted_scores.append(index)
            count -= 1
    return sorted_scores


print(top_scores(unsorted_scores_2, 100))

