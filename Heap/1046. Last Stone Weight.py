class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] #change all values to negative
        heapq.heapify(stones) #max heap
        while len(stones) > 1:
            h1 = heapq.heappop(stones) #heaviest stone
            h2 = heapq.heappop(stones) #2nd heaviest stone
            if h1 != h2:
                heapq.heappush(stones, h1-h2)

        if len(stones) == 1:
            return -stones[0]
        return 0

#O(n logn) time, logn to sort into heap and n to find all the heaviest stones