class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.lst=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.dic[val]=len(self.lst)
            self.lst.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            self.dic[self.lst[-1]]=self.dic[val]
            self.lst[self.dic[val]]=self.lst[-1]
            
            self.lst.pop()
            self.dic.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
