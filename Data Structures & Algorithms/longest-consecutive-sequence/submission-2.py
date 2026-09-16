class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        maxres=0
        for i in s:
            if i-1 not in s:
                res=1
                while i+1 in s:
                    res+=1
                    i+=1
                maxres=max(res,maxres)
        return maxres