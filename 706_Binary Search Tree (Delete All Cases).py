"""Binary Search Tree (Delete All Cases)"""
class BSTNode:
    """alo"""
    def __init__(self, data):
        """alo"""
        self.data = data
        self.left = None
        self.right = None
 
    def get_data(self):
        """alo"""
        return self.data
 
    def set_data(self, data):
        """alo"""
        self.data = data
 
    def get_left(self):
        """alo"""
        return self.left
 
    def set_left(self, left):
        """alo"""
        self.left = left
 
    def get_right(self):
        """alo"""
        return self.right
 
    def set_right(self, right):
        self.right = right
 
class BST:
    def __init__(self):
        self.root = None
 
    def get_root(self):
        return self.root
 
    def set_root(self, root):
        self.root = root
 
    def insert(self, data):
        new_node = BSTNode(data)
        current_root = self.get_root()
        if self.root is None:
            self.root = new_node
            current_root = self.root
        else:
            while True:
                if data < current_root.data:
                    if current_root.left != None:
                        current_root = current_root.left
                    else:
                        current_root.left = new_node
                        break
                elif data >= current_root.data:
                    if current_root.right != None:
                        current_root = current_root.right
                    else:
                        current_root.right = new_node
                        break
 
    def preorder(self, current_root):
        if current_root != None:
            print("->", current_root.get_data(), end=" ")
            self.preorder(current_root.get_left())
            self.preorder(current_root.get_right())
 
    def postorder(self, current_root):
        if current_root != None:
            self.postorder(current_root.get_left())
            self.postorder(current_root.get_right())
            print("->", current_root.get_data(), end=" ")
 
    def inorder(self, current_root):
        if current_root != None:
            self.inorder(current_root.get_left())
            print("->", current_root.get_data(), end=" ")
            self.inorder(current_root.get_right())
 
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
 
    def find_min(self, current_root):
        if self.root is None:
            return None
        else:
            while current_root.get_left() is not None:
                current_root = current_root.get_left()
            return current_root.get_data()
 
    def find_max(self, current_root):
        if self.root is None:
            return None
        else:
            while current_root.get_right() is not None:
                current_root = current_root.get_right()
            return current_root.get_data()
 
    def delete(self, data):
        parent_node = None
        current_root = self.get_root()
        while current_root != None:
            if current_root.get_data() == data:
                if current_root.get_left() == None and current_root.get_right() == None:
                    if parent_node == None:
                        self.set_root(None)
                    elif parent_node.get_left() == current_root:
                        parent_node.set_left(None)
                    else:
                        parent_node.set_right(None)
                elif current_root.get_left() == None:
                    if parent_node == None:
                        self.set_root(current_root.get_right())
                    elif parent_node.get_left() == current_root:
                        parent_node.set_left(current_root.get_right())
                    else:
                        parent_node.set_right(current_root.get_right())
                elif current_root.get_right() == None:
                    if parent_node == None:
                        self.set_root(current_root.get_left())
                    elif parent_node.get_left() == current_root:
                        parent_node.set_left(current_root.get_left())
                    else:
                        parent_node.set_right(current_root.get_left())
                else:
                    successor_parent = current_root
                    successor = current_root.get_left()
                    while successor.get_right() != None:
                        successor_parent = successor
                        successor = successor.get_right()
 
                    current_root.set_data(successor.get_data())
                    if successor_parent == current_root:
                        successor_parent.set_left(successor.get_left())
                    else:
                        successor_parent.set_right(successor.get_left())
                return data
            else:
                if data < current_root.get_data():
                    parent_node = current_root
                    current_root = current_root.get_left()
                else:
                    parent_node = current_root
                    current_root = current_root.get_right()
 
        print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
        return None
 
    def traverse(self, root):
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder(root)
        print()
        print('Inorder: ', end='')
        self.inorder(root)
        print()
        print('Postorder: ', end='')
        self.postorder(root)
        print()
 
def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse(my_bst.get_root())
 
main()
