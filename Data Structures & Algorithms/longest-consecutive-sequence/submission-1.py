class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_sequence = 0
        current = 0
        for num in numbers:
            if num-1 not in numbers:
                sequence = 1
                current = num
                while current + 1 in numbers:
                    current = current + 1
                    sequence += 1
                max_sequence = max(max_sequence, sequence)
        return max_sequence



                