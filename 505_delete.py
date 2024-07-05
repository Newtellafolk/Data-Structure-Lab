class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class SinglyLinkedList:
    def __init__(self, count=0):
        self.count = count
        self.head = None
 
    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_head = self.head
            while current_head.next != None:
                current_head = current_head.next
            current_head.next = new_node
        self.count += 1
 
    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
 
    def delete(self, data):
        current_head = self.head
        temp_head = None
        if current_head == None:
            print("Cannot delete, %s does not exist." % data)
        else:
            while True:
                if current_head.data == data:
                    current_head.data = ""
                    if temp_head == None:
                        self.head = current_head.next
                    elif current_head.next != None:
                        temp_head.next = current_head.next
                    self.count -= 1
                    break
                temp_head = current_head
                if current_head.next == None:
                    print("Cannot delete, %s does not exist." % data)
                    break
                current_head = current_head.next
 
    def insert_before(self, node, data):
        new_node = DataNode(data)
        current_head = self.head
        temp_head = None
        if current_head == None:
            print("Cannot insert, %s does not exist." % (node))
        else:
            while True:
                if current_head.data == node:
                    new_node.next = current_head
                    if temp_head == None:
                        self.head = new_node
                    else:
                        temp_head.next = new_node
                    self.count += 1
                    break
                temp_head = current_head
                if current_head.next == None:
                    print("Cannot insert, %s does not exist." % (node))
                    break
                current_head = current_head.next
 
 
    def traverse(self):
        mylist = ""
        counter = 0
        current_head = self.head
        while current_head != None:
            mylist += str(current_head.data)
            if counter != (self.count - 1):
                mylist += " -> "
                counter += 1
            current_head = current_head.next
        if self.count == 0:
            mylist = "This is an empty list."
        print(mylist)
 
 
def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
 
main()