class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        top = 0

        for n in nums:
            counter[n] += 1
            top = max(top, counter[n])
        
        counter = sorted(counter.items(), key=lambda item:item[1], reverse = True)

        l = []
        i = 0

        while k > 0:
            l.append(counter[i][0])
            i += 1
            k -= 1
        
        return l
        


