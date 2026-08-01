class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for w in strs:
            letters = [0] * 26
            for l in w:
                letters[ord(l) - ord('a')] += 1
            d[tuple(letters)].append(w)

        return list(d.values())
