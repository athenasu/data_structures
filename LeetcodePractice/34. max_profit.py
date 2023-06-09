def max_profit(prices):
    """
        Takes the list of stock prices as input
        Returns the maximum profit you can make by buying and selling
        Steps:
            1. Set up min_price and max_profit
            2. Compare each price in prices to see:
                i. if they are the min_price
                ii. what's the profit with the min_price
                iii. get max_profit
            3. Return max_profit
    """
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


    
    

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Maximum profit:", profit)


"""
    EXPECTED OUTPUT:
    ----------------
    Maximum profit: 5


"""

# Solution 1
# Would have to function like a LinkedList because we're staring from day 1 to day *
# max_price, min_price = prices[1], prices[1]
# max_price_index = 1
# for i, num in enumerate(prices):
#     if num < min_price:
#         min_price = num
#     if num > max_price and i > max_price_index:
#         max_price = num
#         max_price_index = i
# return max_price - min_price


# Solutions 2
# min_value = float('inf')
# max_profit = 0

# for price in prices:
#     min_value = min(min_value, price)
#     profit = price - min_value
#     max_profit = max(profit, max_profit)
# return max_profit