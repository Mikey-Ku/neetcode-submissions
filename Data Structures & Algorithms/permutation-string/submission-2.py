class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
           return False
       
        count = {}
        for val in s1:
            if val not in count:
                count[val] = 0
            count[val] += 1

        window = {}
        L = 0

        for R in range(len(s2)):
            char = s2[R]
            window[char] = window.get(char, 0) + 1

            if R - L + 1 > len(s1):
                left_char = s2[L]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                L += 1

            if window == count:
                return True
        return False
            

        




