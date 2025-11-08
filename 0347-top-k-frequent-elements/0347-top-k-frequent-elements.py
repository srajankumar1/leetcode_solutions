import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        heap = []
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heapreplace(heap, (count, num))
        return [num for (_, num) in heap]