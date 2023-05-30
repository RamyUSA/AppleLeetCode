class MyHashSet:
    # Using set implementation
    def __init__(self):
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.s:
            return True
        return False
      
myHashSet = MyHashSet()
myHashSet.add(1);      # set = [1]
myHashSet.add(2);      # set = [1, 2]
myHashSet.contains(1); # return True
myHashSet.contains(3); # return False, (not found)
myHashSet.add(2);      # set = [1, 2]
myHashSet.contains(2); # return True
myHashSet.remove(2);   # set = [1]
myHashSet.contains(2); # return False, (already removed)
