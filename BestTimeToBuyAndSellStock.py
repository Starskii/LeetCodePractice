def maxProfit(self, prices):
    max_profit = 0
    buy_price = None
    for buy_index in range(len(prices)):
        if buy_price is None or buy_price > prices[buy_index]:
            buy_price = prices[buy_index]
            for sell_index in range(buy_index + 1, len(prices)):
                if prices[sell_index] - prices[buy_index] > max_profit:
                    max_profit = prices[sell_index] - prices[buy_index]
        else:
            continue
    return max_profit

def maxProfit_OnePass(self, prices):
    max_profit = 0
    minimum_price = prices[0]
    for x in range(len(prices)):
        if prices[x] < minimum_price:
            minimum_price = prices[x]
        if prices[x] - minimum_price > max_profit:
            max_profit = prices[x] - minimum_price
    return max_profit