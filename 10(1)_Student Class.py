"""Student Class"""
class Student:

    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.gpa

    def print_details(self):
        print("ID:", self.std_id)
        print("Name:", self.name)
        print("GPA: {:.2f}".format(self.gpa))

def main(text_in):
    import json as j
    std_in = j.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
