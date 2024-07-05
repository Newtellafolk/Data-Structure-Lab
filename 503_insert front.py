class DataNode: 
    def __init__(self, data=""):
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

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    
    def insert_last(self, data):
        newNode = DataNode(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.count += 1
    
    def insert_front(self, data):
        newnode = DataNode(data)
        newnode.next = self.head
        self.head = newnode



    def traverse(self):
        current = self.head
        if current is None:
            print("This is an empty list.")
        else:
            while current:
                print(current.data, end='')
                current = current.next
                if current is not None:
                    print(" -> ", end='') 

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()


main()
