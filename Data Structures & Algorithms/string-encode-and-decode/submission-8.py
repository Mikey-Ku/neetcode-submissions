class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            length = len(string)
            encoded += str(length) + "#" + string

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        while s:
            seperator = s.index("#")
            split = len(s[:seperator])
            length = int(s[:seperator])

            string = s[split + 1:split+ 1 +length]
            decoded.append(string)
            s = s[split + 1 + length:]

        return decoded