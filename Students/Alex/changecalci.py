def countWays(n, coins, index):
    
    if n == 0:
        return 1
    
    if n < 0 or index == len(coins):
        return 0
    
    
    include_current_coin = countWays(n - coins[index], coins, index)
    exclude_current_coin = countWays(n, coins, index + 1)
    

    return include_current_coin + exclude_current_coin


def printWaysToSplit(n):
    coins = [500, 100, 10, 5, 1]  # Coin denominations
    result = countWays(n, coins, 0)
    print(f"Total ways to split {n} using given coins: {result}")


n = int(input("Enter the amount n: "))
printWaysToSplit(n)