class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        while l < r: 
            i = int((l + r)/2)
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i
            else:
                l = i+1
        return -1 
        