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

def main(m_group, n_student):
    stu = ArrayStack()
    keep = [[] for _ in range(0, m_group)]
    for _ in range(1, n_student+1):
        stu.push(input())

    for i in range(0, n_student):
        jumnuan = i % m_group
        keep[jumnuan].append(stu.pop())

    for i in range(len(keep)):
        print(f"Group {i+1}:", ", ".join(map(str, keep[i])))

main(int(input()), int(input()))