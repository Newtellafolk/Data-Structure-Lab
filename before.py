# Noodee
# newyorkky
# Online

# เน็ต — 01/05/2024 1:31 AM
# asdas
# """stack"""
# class ArrayStack:
#     """alo"""
#     def init(self):
#         """alo"""
#         self.size = 0
#         self.data = []
 
#     def push(self, input_data):
#         """Stack"""
#         try:
#             if input_data.isdigit():
#                 input_data = int(input_data)
#             elif input_data.replace(".", "", 1).isdigit():
#                 input_data = float(input_data)
#         except (TypeError, ValueError, ArithmeticError, AttributeError):
#             pass
#         finally:
#             self.data.append(input_data)
#             self.size += 1
 
#     def pop(self):
#         """alo"""
#         self.size -= 1
#         if self.data != []:
#             return self.data.pop(-1)
#         else:
#             print("Underflow: Cannot pop data from an empty list")
#             return None
 
#     def is_empty(self):
#         """popop"""
#         return self.data == []
 
#     def get_stack_top(self):
#         """alo"""
#         if self.data != []:
#             return self.data[-1]
#         else:
#             print("Underflow: Cannot get stack top from an empty list")
#             return None
 
#     def get_size(self):
#         """alo"""
#         return self.size
 
#     def printstack(self):
#         """alo"""
#         print(self.data)
 
# STACK = ArrayStack()
 
# STACK.push("100")
# STACK.push(100)
# STACK.push("3.14")
# STACK.push(3.14)
# STACK.push("66.4a")
# STACK.push("Ackerman")
 
# STACK_.printstack()
 
# print(STACK.getsize())
# VAR1 = STACK.pop()
# print(VAR1)
# STACK_.printstack()
# print(STACK.getsize())
 
# while not STACK.isempty():
#     print(STACK.pop())
 
# print()
# print(STACK.pop())
# print(STACK.get_stacktop())
# print(VAR1)
# dafuq
# ตัวแปรไม่ติด
# Image
# มึงไปแก้เอานะ
# มันมี Stack กับ Stack เฉยๆ ในโค้ด  มันไม่มา
# fk
# discord
# Image
# เอาเป็นว่ามึงจะเห้นมันมีอันเด้อสกอ กับไม่มี
# มึงไปแก้ตัวแปรให้มันหน้าตาเหมือนกัน
# Noodee — 01/05/2024 1:34 AM
# อันนี้กุก้อปจากโจทย์มาเลยนะ
# เน็ต — 01/05/2024 1:34 AM
# กูก๊อปมาวางไม่ติด
# อ้าวหรอ
# จมดละ
# ถ้างั้นน่าจะผ่านละถ้าก๊อปแค่ข้างบนกู
# Noodee — 01/05/2024 1:35 AM
# ไม่ผ่าน
# เน็ต — 01/05/2024 1:35 AM
# เอ้า
# ตายโหง
# Noodee — 01/05/2024 1:36 AM
# อ่อแปป
# เน็ต — 01/05/2024 1:36 AM
# """stack"""
# class ArrayStack:
#     """alo"""
#     def __init__(self):
#         """alo"""
#         self.size = 0
# Expand
# tester.py
# 2 KB
# plz
# this should pass
# Noodee — 01/05/2024 1:37 AM
# ผ่านแนะ
# เน็ต — 01/05/2024 1:37 AM
# 🙏 👌 💯
# เน็ต — Today at 12:43 PM
# """AboTio"""
# class DataNode:
#     """AboTio"""
#     def __init__(self, data=None):
#         """AboTio"""
#         self.data = data
# Expand
# 5.4.txt
# 4 KB
# """AboTio"""
# class DataNode:
#     """AboTio"""
#     def __init__(self, data=None):
#         """AboTio"""
#         self.data = data
# Expand
# lab5.txt
# 4 KB
# ﻿
# """AboTio"""
# class DataNode:
#     """AboTio"""
#     def __init__(self, data=None):
#         """AboTio"""
#         self.data = data
#         self.next = None
 
# """fk"""
# class SinglyLinkedList:
#     """fk"""
#     def __init__(self, count=0):
#         """alo"""
#         self.count = count
#         self.head = None
 
#     def insert_last(self, data):
#         """fk"""
#         new_node = DataNode(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_head = self.head
#             while current_head.next != None:
#                 current_head = current_head.next
#             current_head.next = new_node
#         self.count += 1
 
#     def insert_front(self, data):
#         """Speed this sh+t up"""
#         new_node = DataNode(data)
#         new_node.next = self.head ## เป็นการชี้ไปที่ node head เพื่อให้สามารถพ่วงกับข้อมูลเก่าที่สร้างไว้ได้ เช่น f -> a ซึ่ง a ต่อกับ b c e
#         self.head = new_node
#         self.count += 1
 
#     def insert_before(self, node, data):
#         """Speed this sh+t up"""
#         new_node = DataNode(data)
#         current_head = self.head
#         temp_head = None
#         if current_head == None:
#             print("Cannot insert, %s does not exist." % (node))
#         else:
#             while True:
#                 if current_head.data == node:
#                     new_node.next = current_head
#                     if temp_head == None:
#                         self.head = new_node
#                     else:
#                         temp_head.next = new_node
#                     self.count += 1
#                     break
#                 temp_head = current_head
#                 if current_head.next == None:
#                     print("Cannot insert, %s does not exist." % (node))
#                     break
#                 current_head = current_head.next
 
 
#     def traverse(self):
#         """fk"""
#         our_list = ""
#         counter = 0
#         current_head = self.head
#         while current_head != None:
#             our_list += str(current_head.data)
#             if counter != (self.count - 1):
#                 our_list += " -> "
#                 counter += 1
#             current_head = current_head.next
#         if self.count == 0:
#             our_list = "This is an empty list."
#         print(our_list)
 
 
# def main():
#     mylist = SinglyLinkedList()
#     for _ in range(int(input())):
#         text = input()
#         condition, data = text.split(": ")
#         if condition == "F":
#             mylist.insert_front(data)
#         elif condition == "L":
#             mylist.insert_last(data)
#         elif condition == "B":
#             mylist.insert_before(*data.split(", "))
#         # elif condition == "D":
#         #     mylist.delete(data)
#         else:
#             print("Invalid Condition!")
#     mylist.traverse()
 
 
# main()
# 5.4.txt
# 4 KB

# def delete(self, data):
#         current_head = self.head
#         tmp_head = None
#         if current_head == None:
#             print("Cannot delete, %s does not exist." %data)
#         else:

#             while True:
#                 if current_head.data == data:
#                     current_head.data = ""
#                 if tmp_head == None:
#                     self.head = current.next
def calculate_button_presses(n):
    # กรณี n = 1
    if n == 1:
        return 1
    # กรณี n > 1
    else:
        return 2 * n

# ตัวอย่างการเรียกใช้ฟังก์ชันสำหรับ n = 4
n_value = input()
presses = calculate_button_presses(n_value)
print(presses)