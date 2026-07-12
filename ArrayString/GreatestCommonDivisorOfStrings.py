class Solution(object):
    def euclidean(self,a,b):
            while b:
                a, b = b, a % b
            return a

    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        maxLen = self.euclidean(len1, len2)
        divider=str1[:maxLen]
        if divider * (len1 // maxLen) == str1 and divider * (len2 // maxLen) == str2:
            return divider
        return ''