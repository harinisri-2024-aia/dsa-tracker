class Solution(object):
    def runningSum(self, nums):
        result=[]
        total=0
        n=len(nums)
        for i in range(n):
            total+=nums[i]
            result.append(total)
        return result
        