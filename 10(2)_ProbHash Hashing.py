"""ProbHash Hashing"""

class Student:
    def __init__(self, std_id=0, name="", gpa=0.0):
        self.std_id = int(std_id)
        self.name = str(name)
        self.gpa = float(gpa)

    def get_std_id(self):
        return int(self.std_id)

    def get_name(self):
        return str(self.name)

    def get_gpa(self):
        return float(self.gpa)

    def print_details(self):
        print("ID: %d\nName: %s\nGPA: %.02f" %(self.get_std_id(), self.get_name(), self.get_gpa()))

class ProbHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash(self, key):
        while True:
            ikey = key % self.size
            if self.hash_table[ikey] == []:
                return int(ikey)
            else:
                return self.hash(self.rehash(key))

    def rehash(self, key):
        return int(key + 1) % self.size

    def insert_data(self, student):
        if [] in self.hash_table:
            ikey = self.hash(student.get_std_id())
            self.hash_table[ikey] = student
            print("Insert %d at index %d" %(student.get_std_id(), ikey))
        else:
            print("The list is full. %d could not be inserted." %(student.get_std_id()))

    def search_data(self, std_id):
        ikey = std_id % self.size
        count = 0
        while self.hash_table[ikey] != [] and self.hash_table[ikey].get_std_id() != std_id\
        and count <= self.size:
            ikey = self.rehash(ikey)
            count += 1
        if self.hash_table[ikey] != [] and self.hash_table[ikey].get_std_id() == std_id:
            print("Found %d at index %d" % (std_id, ikey))
            return self.hash_table[ikey]
        else:
            print("%d does not exist." % std_id)
            return None


import json
def main():
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()

