"""Stack and Queue แบบงงๆ"""
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
        self.size -= 1
        if self.data != []:
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

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())
    
print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)

