# https://www.interviewcake.com/question/python/single-riffle-check?section=array-and-string-manipulation&course=fc1
# Write a function to tell us if a full deck of cards shuffled_deck is
# a single riffle of two other halves half1 and half2.


def is_single_riffle(shuffled_deck, half1, half2, deck_ptr,  half1_ptr, half2_ptr):
    if deck_ptr == len(shuffled_deck):
        return True
    if half1_ptr < len(half1) and half1[half1_ptr] == shuffled_deck[deck_ptr]:
        half1_ptr += 1
    elif half2_ptr < len(half2) and half2[half2_ptr] == shuffled_deck[deck_ptr]:
        half2_ptr += 1
    else:
        return False
    deck_ptr += 1
    is_single_riffle(shuffled_deck, half1, half2, deck_ptr, half1_ptr, half2_ptr)


shuffled_deck = []
half1 = []
half2 = []
print(is_single_riffle(shuffled_deck, half1, half2, 0, 0, 0))



