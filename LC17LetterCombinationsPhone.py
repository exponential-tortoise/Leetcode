class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)==0:
            return []
        
        dic={'2':'abc',
             '3':'def',
             '4':'ghi',
             '5':'jkl',
             '6':'mno',
             '7':'pqrs',
             '8':'tuv',
             '9':'wxyz'
        }
        
        res=[]
        
        def dfs(dic,res,digits,path,index):
            
            if len(path)==len(digits):
                res.append(path)
                return
            for j in dic[digits[index]]: #Lookup . ex : digits[0]=2 . dic[2]='abc' , add a,b,c to path 
                dfs(dic,res,digits,path+j,index+1)
                
        #calling the function       
        dfs(dic,res,digits,'',0)
        return res
        
