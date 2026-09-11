class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # my solution

        l, r = 0, 0
        res = ""

        while l < len(word1) and r < len(word2):
            res += word1[l] + word2[r]
            l, r = l + 1, r + 1

        if l >= len(word1):
            res += word2[r:]
        elif r >= len(word2):
            res += word1[l:]

        return res