class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binsearch(l,r):
            while l<=r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m]<target:
                    l = m + 1
                else:
                    r = m - 1
            if l>r:
                return -1
            return l
        first = last = binsearch(0,len(nums)-1)
        if first == -1:
            return [-1,-1]
        while True:
            temp = binsearch(0,first-1)
            if temp == -1:
                break
            first = temp
        while True:
            temp = binsearch(last+1,len(nums)-1)
            if temp == -1:
                break
            last = temp
        return [first,last]



        

        
        return [-1,-1]
            
            