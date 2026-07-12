class Solution(object):
    def mergeAlternately(self, word1, word2):
        MainWord=''
        len1,len2=len(word1),len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                MainWord += word1[i]
            if i < len2:
                MainWord += word2[i]
        return MainWord
        