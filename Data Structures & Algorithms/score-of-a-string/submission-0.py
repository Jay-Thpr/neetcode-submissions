class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        right = 1

        for left in range(len(s) - 1):
            res += abs(ord(s[left]) - ord(s[right]))
            right += 1
        return res