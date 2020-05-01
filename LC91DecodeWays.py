class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp=[1]+[0]*len(s)
        
        for i in range(1,len(s)+1):
            if s[i-1]!='0':
                dp[i]+=dp[i-1]
            if i>=2 and 10<=int(s[i-2:i])<=26:
                dp[i]+=dp[i-2]
            
        return dp[len(s)]
        
