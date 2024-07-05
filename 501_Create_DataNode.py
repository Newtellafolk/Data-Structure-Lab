class DataNode: 
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

pNew = DataNode(input())
print(pNew.get_data())
print(pNew.get_next())
