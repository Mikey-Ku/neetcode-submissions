class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minimum = 1
        maximum = max(piles)

        while minimum < maximum:
            guess = (maximum + minimum) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / guess)
            
            if total > h:
                minimum = guess + 1
            else:
                maximum = guess
    
        return minimum