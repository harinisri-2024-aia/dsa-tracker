class Solution(object):
    def findDuplicates(self, nums):
        frequency={}
        result=[]
        for x in nums:
            frequency[x]=frequency.get(x,0)+1
        for x in frequency:
            if frequency[x]==2:
                result.append(x)
        return result