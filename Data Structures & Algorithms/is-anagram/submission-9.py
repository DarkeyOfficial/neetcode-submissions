class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Solution:
            # return sorted(s) == sorted(t)

        # 2. Solution:
        if len(s) != len(t): 
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # chars von s zählen
            countT[t[i]] = 1 + countT.get(t[i], 0)  # chars von t zählen
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True