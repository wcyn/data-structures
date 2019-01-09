# https://www.interviewcake.com/question/python/inflight-entertainment?section=hashing-and-hash-tables&course=fc1
# Write a function that takes an integer flight_length (in minutes) and a list of integers
# movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers
# in movie_lengths whose sum equals flight_length.


def get_two_movies(flight_length, movie_lengths):
    length_map = {}
    for length in movie_lengths:
        complement = flight_length - length
        if complement in length_map:
            return True
        length_map[length] = True
    return False


print(get_two_movies(8, [5, 3, 2, 4, 8, 1, 4]))

