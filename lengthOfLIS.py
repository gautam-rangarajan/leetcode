class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        lens = list()
        for i in range(len(nums)):
            lens.append(0)
        for i in range(len(nums)):
            curMax = 0
            for j in range(i)[::-1]:
                if(nums[j] < nums[i] and lens[j] >= curMax):
                    lens[i] = lens[j]
                    curMax = lens[i]
            lens[i] = lens[i] + 1
                    
        return max(lens)