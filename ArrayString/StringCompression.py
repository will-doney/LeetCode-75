class Solution(object):
    def compress(self, chars):
        
        insert = 0
        i=0
        
        while i < len(chars):
            collection = 1
            while (collection + i) < len(chars) and chars[collection + i] == chars[i]:
                collection += 1
            
            chars[insert] = chars[i]
            insert += 1

            if collection > 1:
                string = str(collection)
                chars[insert:insert+len(string)] = list(string) 
                insert += len(string)

            i += collection

        return insert
