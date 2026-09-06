class Solution(object):
    def maxOperations(self, nums, k):
        
        left = 0 
        right = len(nums) - 1
        total = 0
        nums = sorted(nums) 

        while right > left:

            if nums[right] + nums[left] == k:
                right -= 1
                left += 1
                total += 1
                continue 
            elif nums[right] + nums[left] > k:
                right -= 1
            else:
                left += 1

        return total
