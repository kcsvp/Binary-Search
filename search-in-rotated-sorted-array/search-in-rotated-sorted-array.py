class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif nums[m] > nums[r]:
                if nums[m]<target or target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            else:
                if nums[m]<target<=nums[r]:
                    l = m + 1
                else:
                    r = m      
        if l==r and nums[l]==target:
            return l          
        return -1