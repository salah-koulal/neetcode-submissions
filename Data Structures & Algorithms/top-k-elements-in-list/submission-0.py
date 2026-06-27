class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}

        for n in nums:
            frq[n] = frq.get(n, 0) + 1
        
        sorted_items = sorted(frq.items(), key=lambda item:item[1], reverse=True)
        
        res = []
        for n, count in sorted_items[:k]:
            res.append(n)
        return res