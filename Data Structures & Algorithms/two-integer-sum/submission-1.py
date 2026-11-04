class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            goal = target - val
            if goal in seen:
                return [seen[goal], idx]
            else:
                seen[val] = idx