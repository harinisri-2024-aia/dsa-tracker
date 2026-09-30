class Solution(object):
    def reverseStr(self, s, k):
        s=list(s)
        for i in range(0,len(s),k*2):
            s[i:i+k]=s[i:i+k][::-1]
        return "".join(s)
        