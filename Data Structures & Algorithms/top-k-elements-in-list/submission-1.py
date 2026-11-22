class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maxheap
        counter = Counter(nums)
        heap = []

        for n, f in counter.items():
            heapq.heappush_max(heap, (f, n))
        
        ret = []
        for i in range(k):
            f, n = heapq.heappop_max(heap)
            ret.append(n)

        return ret