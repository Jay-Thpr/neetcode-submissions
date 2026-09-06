class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0

        for t_idx in range(len(t)):
            if s_idx == len(s):
                return True

            if t[t_idx] == s[s_idx]:
                s_idx += 1
        
        return s_idx == len(s)