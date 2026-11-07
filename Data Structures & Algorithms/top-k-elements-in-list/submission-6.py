class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        frequent = []
        for val in nums:
            if val not in seen:
                seen[val] = 1
            else:
                seen[val] += 1
        
        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        for i, (key, count) in enumerate(sorted_items):
            if i >= k:
                break
            frequent.append(key)
        return frequent
