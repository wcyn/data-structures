# https://www.interviewcake.com/question/python/stock-price?course=fc1&section=greedy
# rite an efficient function that takes stock_prices and returns the best profit
# I could have made from one purchase and one sale of one share of Apple stock yesterday.
import unittest


def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError("Getting a profit requires at least two prices")

    # buy, sell = 0, len(stock_prices) - 1
    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]

    for index in range(1, len(stock_prices)):
        max_profit = max(max_profit, stock_prices[index] - min_price)
        min_price = min(min_price, stock_prices[index])

    return max_profit


stock_prices = [10, 8, 7, 5, 4, 3, 2]
sp = [1, 1, 1, 1, 1, 1]
print(get_max_profit(sp))

# Tests


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
