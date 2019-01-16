# https://www.interviewcake.com/question/python/stock-price?course=fc1&section=greedy
# rite an efficient function that takes stock_prices and returns the best profit
# I could have made from one purchase and one sale of one share of Apple stock yesterday.


def get_best_profit(stock_prices):
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
print(get_best_profit(sp))

