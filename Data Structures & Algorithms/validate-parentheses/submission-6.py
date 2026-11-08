class Solution:
    def isValid(self, s: str) -> bool:
        start = {"{", "(", "["}
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []
        for char in s:
            if not stack or char in start:
                stack.append(char)
            else:
                if stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return True
        else:
            return False