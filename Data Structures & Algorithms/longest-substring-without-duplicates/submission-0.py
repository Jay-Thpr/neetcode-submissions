class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        longest = 0
        cur = 1

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                cur -= 1

            seen.add(s[r])  
            longest = max(longest, cur)
            r += 1
            cur += 1

        return longest



