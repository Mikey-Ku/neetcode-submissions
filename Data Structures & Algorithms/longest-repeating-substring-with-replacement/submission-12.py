class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        maximum = 0
        count = {}

        while R < len(s):
            count[s[R]] = count.get(s[R], 0) + 1

            highest = max(count.values())
            replace = (R - L + 1) - highest

            while replace > k:
                count[s[L]] -= 1
                L += 1

                highest = max(count.values())
                replace = (R - L + 1) - highest

            maximum = max(maximum, R - L + 1)
            R += 1

        return maximum