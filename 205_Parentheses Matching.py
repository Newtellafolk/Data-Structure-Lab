class ArrayStack:
    """_"""
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """_"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """_"""
        #check underflow
        if self.data != []:
            self.size -= 1
            return self.data.pop(-1)# data on top of stack and delete it from stack
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
        
    def is_empty(self):
        """_"""
        return self.data == []

    def get_stack_top(self):
        """_"""
        if self.data != []:
            return self.data[-1]# data on top of stack
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """_"""
        return self.size

    def print_stack(self):
        """_"""
        print(self.data)

def is_parentheses_matching(text):
    stackkk = ArrayStack()
    countt_1 = text.count("(")
    countt_2 = text.count(")")
    for i in text:
        if i == "(":
            stackkk.push(i)
        elif i == ")":
            stackkk.pop()
    
    if stackkk.is_empty() == True and (countt_1 == countt_2):
        print("Parentheses in %s are matched" %text)
        print(True)
    else:
        print("Parentheses in %s are unmatched" %text)
        print(False)

is_parentheses_matching(input())