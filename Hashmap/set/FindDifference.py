class Solution(object):
    def findDifference(self, nums1, nums2):
        answer1 = list(set(nums1) - set(nums2))
        answer2 = list(set(nums2) - set(nums1))
        return [answer1, answer2]
        