class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minRepInCoin = [float('inf')] * (amount + 1)
        #Base case
        minRepInCoin[0] = 0
        
        for amount in range(1, amount + 1):
            # brute force thru State Space Tree
            for coin in coins:
                if amount - coin >= 0: # Got coins to do
                    minRepInCoin[amount] = min(minRepInCoin[amount], minRepInCoin[amount - coin] + 1)

        return minRepInCoin[amount] if minRepInCoin[amount] != float('inf') else -1


