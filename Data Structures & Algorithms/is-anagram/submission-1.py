class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)==sorted(t):
        #     return True
        # else:
        #     return False
        count={}
        for i in s:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=1
        count2={}
        for i in t:
            if i in count2:
                count2[i]=count2[i]+1
            else:
                count2[i]=1
        if count==count2:
            return True
        else:
            return False