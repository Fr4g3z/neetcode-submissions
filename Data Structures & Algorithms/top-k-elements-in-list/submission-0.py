class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        c = {}
        for num in nums:
            c[num] = c.get(num, 0) + 1
        buckets = [[] for _ in range(l+1)]
        for num, freq in c.items():
            buckets[freq].append(num)
        result = []
        for freq in range(l, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result