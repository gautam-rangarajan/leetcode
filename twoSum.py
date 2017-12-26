class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = dict()
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
            
        
        numbers = list()
        for num in nums_hash.keys():
            nums_hash[num] = nums_hash[num] - 1
            lookFor = target-num
            countLookFor = nums_hash.get(lookFor, 0)
            if countLookFor > 0:
                numbers.append(num)
                numbers.append(lookFor)
                break
            
        ind1 = -1
        ind2 = -1

        for i in range(len(nums)):
            if nums[i] == numbers[0] and ind1 == -1:
                ind1 = i
            if nums[i] == numbers[1] and ind1 != i:
                ind2 = i
                
        return [ind1, ind2]