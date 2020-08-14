# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 07:20:11 2020

@author: Henry
"""

# Import any required modules
from datetime import datetime




# Create class for list of to-do items
class ToDoList:
    
    def __init__(self):
        self.actual_list = []
        
    def add_item(self, item):
         self.actual_list.append(item)
        
    def remove_item(self, item_r):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].description == item_r:
                del self.actual_list[i]
                break
                
    def find_item(self, item_f):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].description == item_f:
                return i
                break
            
    def print_items(self):
        for i in range(len(self.actual_list)):
            print(self.actual_list[i].description)


# Create class for to do item
class ToDoItem:
    
    def __init__(self, description):
        self.description = description
        self.complete = False
        
    def add_date(self, date):
        self.date_str = date
        self.date_obj = datetime.strptime(date, '%d/%m/%Y')
        
    def mark_as_complete(self):
        self.complete = True
        
    def edit_description(self, new_description):
        self.description = new_description

# Create while loop to ask for user input repeatably until the user is finished
user_editing = True
your_todo_list = ToDoList()


while user_editing:
    
    print('Your options are:\n')
    print('1 - Add a new to do item\n')
    print('2 - See all items\n')
    print('3 - Delete an item\n')
    print('9 - Exit. This will close edit and save your list.\n')
    
    change = input("Please enter a number corresponding to the change you would like to make:")
    # Catch any erroneous entries here

    if change == '1':
        item_name = input("What is the new item called:")
        your_todo_list.add_item(ToDoItem(item_name))

    if change == '2':
        your_todo_list.print_items()
        
    if change == '3':
        item_name = input("What is this item called:")
        your_todo_list.remove_item(item_name)

    if change == '9':
        user_editing = False


# Test they work 
test_list = ToDoList()
test_list.add_item(ToDoItem("Item 1"))
test_list.add_item(ToDoItem("Item 2"))
test_list.add_item(ToDoItem("Item 3"))
test_list.print_items()
test_list.remove_item("Item 2")
test_list.print_items()
idx = test_list.find_item("Item 3")
test_list.actual_list[idx].add_date('01/02/2003')
test_list.actual_list[idx].date_obj
test_list.actual_list[idx].edit_description('Item 3.3')
test_list.actual_list[idx].mark_as_complete()
test_list.actual_list[idx].complete
test_list.print_items()




