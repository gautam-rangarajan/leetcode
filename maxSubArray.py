class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        curMax = 0
        temps = 0
        tempe = 0
        for i in range(len(nums)):
            curSum = sum(nums[temps:tempe+1])
            if curSum > curMax:
                curMax = curSum
                start = temps
                end = tempe
                
            if curSum > 0:
                tempe += 1
            else:
                tempe += 1 
                temps = tempe
                
        return sum(nums[start:end+1])