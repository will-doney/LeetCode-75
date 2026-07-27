class Solution(object):
    def productExceptSelf(self, nums):
    
        n = len(nums)
        answer = []
        pre = 1
        post = 1

        for i in range(n):
            answer.append(pre)
            pre *= nums[i]

        
        for i in reversed(range(n)):
            answer[i] *= post
            post *= nums[i]