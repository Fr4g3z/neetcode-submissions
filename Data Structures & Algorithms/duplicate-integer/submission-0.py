class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        nums = set(nums)
        if a > len(nums):
            return True
        else:
            return False
        