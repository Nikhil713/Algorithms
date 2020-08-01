class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return(0)
        maxlen = 1
        size = len(s)
        dup = []
        temp = 1
        dup.append(s[0])
        i=1
        ind=0
        while(i <size):
            temp+=1
            if s[i] in dup:
                temp = 1
                ind=dup.index(s[i])
                dup = dup[ind+1:]
            if temp > maxlen :
                maxlen = temp
            if(len(dup)>maxlen):
                maxlen=len(dup)
            duplen=len(dup)
            if i<size:
                if(s[i+1] not in dup):
                    duplen=len(dup)+1
            print(maxlen,duplen)
            dup.append(s[i])
            i+=1
            # print(dup)
            # print(temp)
        
        return(maxlen)
            
            
        
        