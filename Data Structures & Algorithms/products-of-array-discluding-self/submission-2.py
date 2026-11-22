class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pr = [1] * l
        su = [1] * l
        p = 1
        for i, k in enumerate(nums):
            pr[i] = p
            p *= k
        
        p = 1
        for i in range(l-1, -1, -1):
            su[i] = p
            p *= nums[i]
        return [px * sx for px, sx in zip(pr,su)]



        