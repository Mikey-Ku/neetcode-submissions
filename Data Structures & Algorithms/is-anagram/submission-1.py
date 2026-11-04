class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count_s = {}
        for letter in s:
            if letter not in count_s:
                count_s[letter] = 1
            else:
                count_s[letter] += 1
        
        for letter in t:
            if letter not in count_s:
                return False
            else:
                count_s[letter] -= 1
                if count_s[letter] < 0:
                    return False
        
        return True