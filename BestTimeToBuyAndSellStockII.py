prices = [7,6,4,3,1]
def maxProfit(prices):
    profit = 0
    current_price = None
    currently_bought = False
    for x in range(len(prices) - 1):
        if prices[x + 1] < prices[x]:
            if currently_bought:
                profit += prices[x] - current_price
                currently_bought = False
        else:
            if not currently_bought:
                current_price = prices[x]
                currently_bought = True
    if currently_bought:
        profit += prices[len(prices) - 1] - current_price
    return profit

print(maxProfit(prices))