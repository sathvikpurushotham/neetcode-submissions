class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        for i,n in d.items():
            res.append([n,i])
        res.sort()

        fin=[]
        while len(fin)<k:
            fin.append(res.pop()[1])

        return fin

        