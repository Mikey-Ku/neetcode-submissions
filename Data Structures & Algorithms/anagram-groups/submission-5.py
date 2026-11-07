class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            counts = [0] * 26
            for letter in string:
                index = ord(letter) - ord("a")
                counts[index] += 1
        
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        
        return list(groups.values())
            