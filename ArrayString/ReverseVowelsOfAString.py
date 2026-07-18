class Solution(object):
    def reverseVowels(self, s):
        vowels = ("a","e","i","o","u","A","E","I","O","U")
        stringList = list(s)
        left = 0
        right = len(s) -1
    
        while left < right:
            if stringList[left] not in vowels:
                left += 1 
                continue

            if stringList[right] not in vowels:
                right -= 1
                continue

            if stringList[left] in vowels and stringList[right] in vowels:
                stringList[left], stringList[right] = stringList[right], stringList[left]
                right -= 1
                left +=1
                continue 
            
        return ''.join(stringList)