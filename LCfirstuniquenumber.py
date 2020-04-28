class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.dic={}
        for i in nums:
            if i not in self.dic:
                self.dic[i]=1
            else:
                self.dic[i]+=1
            
    def showFirstUnique(self) -> int:
        
        for k,v in self.dic.items():
            if v==1:
                return k
        return -1
        
    def add(self, value: int) -> None:
        
        
        if value in self.dic:
            self.dic[value]+=1
        else:
            self.dic[value]=1
