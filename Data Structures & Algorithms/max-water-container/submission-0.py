class Solution:
    def maxArea(self, nums: List[int]) -> int:
        res=0
        l=0
        r=len(nums)-1

        while l<r:
            res=max(res,min(nums[l],nums[r])*(r-l))
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return res
