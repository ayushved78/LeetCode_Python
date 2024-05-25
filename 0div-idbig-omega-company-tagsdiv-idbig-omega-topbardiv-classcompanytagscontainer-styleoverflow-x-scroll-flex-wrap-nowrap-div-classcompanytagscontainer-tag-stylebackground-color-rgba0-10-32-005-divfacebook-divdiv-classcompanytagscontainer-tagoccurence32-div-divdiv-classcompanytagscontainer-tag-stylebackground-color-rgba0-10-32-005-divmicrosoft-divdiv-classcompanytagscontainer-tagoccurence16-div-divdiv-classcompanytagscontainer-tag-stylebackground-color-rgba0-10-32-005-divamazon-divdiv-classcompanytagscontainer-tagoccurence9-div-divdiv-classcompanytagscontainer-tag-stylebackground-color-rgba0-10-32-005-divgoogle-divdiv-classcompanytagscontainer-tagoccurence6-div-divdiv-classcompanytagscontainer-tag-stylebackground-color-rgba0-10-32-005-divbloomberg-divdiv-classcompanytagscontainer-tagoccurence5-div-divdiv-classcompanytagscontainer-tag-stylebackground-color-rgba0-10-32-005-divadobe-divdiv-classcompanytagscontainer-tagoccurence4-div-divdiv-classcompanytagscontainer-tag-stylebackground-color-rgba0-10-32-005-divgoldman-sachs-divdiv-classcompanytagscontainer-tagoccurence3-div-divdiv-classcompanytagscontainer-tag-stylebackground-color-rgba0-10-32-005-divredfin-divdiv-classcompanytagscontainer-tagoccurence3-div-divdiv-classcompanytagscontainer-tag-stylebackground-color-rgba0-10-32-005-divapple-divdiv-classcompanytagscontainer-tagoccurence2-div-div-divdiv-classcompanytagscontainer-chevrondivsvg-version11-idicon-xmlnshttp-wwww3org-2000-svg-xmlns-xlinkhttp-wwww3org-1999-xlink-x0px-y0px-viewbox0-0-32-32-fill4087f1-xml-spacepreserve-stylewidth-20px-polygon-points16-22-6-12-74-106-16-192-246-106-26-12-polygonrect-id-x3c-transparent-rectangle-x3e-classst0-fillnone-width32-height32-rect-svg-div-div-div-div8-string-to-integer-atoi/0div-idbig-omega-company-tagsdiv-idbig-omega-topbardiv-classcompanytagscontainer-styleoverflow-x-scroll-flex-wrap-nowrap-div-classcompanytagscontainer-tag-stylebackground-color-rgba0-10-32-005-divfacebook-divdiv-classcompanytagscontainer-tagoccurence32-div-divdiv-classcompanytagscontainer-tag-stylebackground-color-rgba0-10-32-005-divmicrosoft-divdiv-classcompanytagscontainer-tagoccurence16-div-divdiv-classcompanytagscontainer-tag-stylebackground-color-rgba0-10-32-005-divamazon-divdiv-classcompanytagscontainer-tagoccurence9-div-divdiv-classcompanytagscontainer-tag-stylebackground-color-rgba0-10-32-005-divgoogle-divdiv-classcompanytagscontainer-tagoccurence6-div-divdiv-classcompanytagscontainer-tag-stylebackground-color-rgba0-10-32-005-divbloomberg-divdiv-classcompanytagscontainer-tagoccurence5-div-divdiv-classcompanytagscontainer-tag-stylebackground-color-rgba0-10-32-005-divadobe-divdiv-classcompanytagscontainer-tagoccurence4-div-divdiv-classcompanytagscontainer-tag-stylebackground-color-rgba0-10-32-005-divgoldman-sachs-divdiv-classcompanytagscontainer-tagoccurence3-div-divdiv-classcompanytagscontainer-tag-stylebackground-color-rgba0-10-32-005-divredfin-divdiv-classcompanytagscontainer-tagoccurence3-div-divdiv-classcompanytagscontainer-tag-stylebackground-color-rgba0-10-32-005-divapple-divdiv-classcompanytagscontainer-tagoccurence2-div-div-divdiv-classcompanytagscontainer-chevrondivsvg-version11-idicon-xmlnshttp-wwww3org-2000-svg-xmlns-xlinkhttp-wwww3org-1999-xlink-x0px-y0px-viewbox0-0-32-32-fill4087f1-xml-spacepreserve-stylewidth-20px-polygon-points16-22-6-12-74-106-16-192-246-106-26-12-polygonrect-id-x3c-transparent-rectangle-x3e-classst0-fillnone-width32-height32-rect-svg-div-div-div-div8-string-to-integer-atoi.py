class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        index=0
        sign=1
        if s[index] in ["-","+"]:
            if s[index]=="-":
                sign=-1
            else:
                sign=1
            index+=1
        res=0
        for i in range(index,len(s)):
            if not (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
                break
            res=res*10+ (ord(s[i])-ord("0"))
        res*=sign
        if res>2**31-1:
            return 2**31-1
        if res<-2**31:
            return -2**31
        else:
            return res