class Solution(object):
    def maxVowels(self, s, k):

        vowels = ("aeiou")
        current = sum(1 for c in s[:k] if c in vowels)
        max_Vowels = current

        for right in range(k, len(s)):
            left = right - k
            if s[right] in vowels:
                current += 1
            if s[left] in vowels:
                current -= 1
            max_Vowels = max(max_Vowels, current)
            
        return max_Vowels