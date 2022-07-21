"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def get_best(prices) -> int:
    max_profit = 0
    left_ptr, right_ptr = 0, 0
    while right_ptr < (len(prices) - 1):
        right_ptr += 1
        if prices[left_ptr] < prices[right_ptr]:
            price = prices[right_ptr] - prices[left_ptr]
            if price > max_profit:
                max_profit = price
        else:
            left_ptr = right_ptr
    return max_profit
            


result1 = get_best([7,1,5,3,6,4])
if result1 != 5:
    print(f"Got {result1}, expected 5")
    assert False

result2 = get_best([7,6,4,3,1])
if result2 != 0:
    print(f"Got {result2}, expected 0")
    assert False

result3 = get_best([1,2,4,2,5,7,2,4,9,0,9])
if result3 != 9:
    print(f"Got {result3}, expected 9")
    assert False
