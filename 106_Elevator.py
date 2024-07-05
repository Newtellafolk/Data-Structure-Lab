"""Elevator"""
def lift():
    """_"""
class Elevator:
    def __init__(self,max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        self.current_floor = floor
        
    def report_current_floor(self):
        print(self.current_floor)

max_floor = Elevator(int(input()))
lift_up = 0
keep = 0
while True:
    lift_up = input()
    if lift_up == "Done":
        break
    if int(lift_up) > max_floor.max_floor:
        print("Invalid Floor!")
    else:
        max_floor.go_to_floor(int(lift_up))
max_floor.report_current_floor()

lift()
