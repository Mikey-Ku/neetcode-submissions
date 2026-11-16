class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[l] <= nums[m] and nums[r] >= nums[m + 1]:
                return nums[m + 1]
            elif nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
    