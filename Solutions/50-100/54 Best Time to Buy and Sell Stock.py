def solve(prices):
    result = 0
    if len(prices) == 0:
      return 0
    minimum = prices[0]
    benefit = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            result += benefit
            benefit = 0
            minimum = prices[i]
        else:
            benefit = max(benefit, prices[i] - minimum)
    result += benefit
    return result