class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        max_Ones = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_Ones = max(max_Ones, right-left)
        return max_Ones
            