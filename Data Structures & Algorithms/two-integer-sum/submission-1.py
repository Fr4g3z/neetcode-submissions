class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            e = target - n
            if e in d:
                return[d[e], i]
            d[n] = i
                



        