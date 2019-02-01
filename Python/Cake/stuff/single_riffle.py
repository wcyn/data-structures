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

def is_single_riffle(half1, half2, shuffled_deck):
    half1_index = 0
    half2_index = 0
    half1_max_index = len(half1) - 1
    half2_max_index = len(half2) - 1

    for card in shuffled_deck:
        # If we still have cards in half1
        # and the "top" card in half1 is the same
        # as the top card in shuffled_deck
        if half1_index <= half1_max_index and card == half1[half1_index]:
            half1_index += 1

        # If we still have cards in half2
        # and the "top" card in half2 is the same
        # as the top card in shuffled_deck
        elif half2_index <= half2_max_index and card == half2[half2_index]:
            half2_index += 1

        # If the top card in shuffled_deck doesn't match the top
        # card in half1 or half2, this isn't a single riffle.
        else:
            return False

    # All cards in shuffled_deck have been "accounted for"
    # so this is a single riffle!
    return True

class TestRecursive(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6], 0, 0, 0)
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5], 0, 0, 0)
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6], 0, 0, 0)
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5], 0, 0, 0)
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8], 0, 0, 0)
        self.assertFalse(result)


class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)