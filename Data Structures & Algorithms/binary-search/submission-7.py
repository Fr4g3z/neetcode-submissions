class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1    
        else:
            i = int(len(nums)/2)
        r = len(nums)+1
        l = -1
        while (i!=r and i!=l) and (i>=0 and i < len(nums)): 
            if nums[i] == target:
                return i
            elif nums[i] > target:
                if r > i:
                     r = i
                i = int(r/2)
            else:
                if l < i:
                     l = i
                i = int((l+r)/2)
        return -1 
        