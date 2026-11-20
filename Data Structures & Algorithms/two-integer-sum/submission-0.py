class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]
            e = target - nums[i]
            if e in d and e!=nums[i]:
                return [d[e][0],i]
            elif e in d and len(d[e]) > 1:
                return d[e]
                



        