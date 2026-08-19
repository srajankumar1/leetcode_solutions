import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif min_heap[0] < num:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]