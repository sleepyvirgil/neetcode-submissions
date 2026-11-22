class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        counter = Counter(nums)
        freq_array = [[] for i in range(len(nums) + 1)]

        for n, f in counter.items():
            freq_array[f].append(n)
        
        ret = []
        for i in range(len(nums), -1, -1):
            if len(ret) < k:
                ret.extend(freq_array[i])
            
        return ret

        '''
            if freq_array[i]:
                ret.extend(freq_array[i])

            if len(ret) == k:
                return ret
            '''