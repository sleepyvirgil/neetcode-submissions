class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #minheap
        counter = Counter(nums)
        heap = []
        for n, f in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (f, n))
            else:
                heapq.heappushpop(heap, (f, n))
        '''
        ret = []
        for h in heap:
            ret.append(h[1])

        return ret
        '''
        return [h[1] for h in heap]