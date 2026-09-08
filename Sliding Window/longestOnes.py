class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        maxOnes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros +=1
            if nums[left] == 0 and zeros > k:
                zeros -= 1
                left += 1
            elif nums[left] == 1 and zeros > k:
                left += 1
            
            maxOnes = max(maxOnes, right-left+1)
        return maxOnes