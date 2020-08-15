# -*- coding: utf-8 -*-
'''
    File name: fn_and_obj.py
    Author: Henry Letton
    Date created: 2020-08-14
    Python Version: 3.7
    Desciption: This program creates functions and objects required for main.py
'''

# Import any required modules
from datetime import datetime
import pickle


# Using the pickle module, a to do list can be saved to disc (in wd)
def save_list_to_disc(todo_list):

    outfile = open('ToDoListSave','wb')
    pickle.dump(todo_list,outfile)
    outfile.close()


# If a previous list exists (in wd), the user can decide whether to use it or start afresh
def load_prev_list():
    
    try:
        infile = open('ToDoListSave','rb')
        todo_list = pickle.load(infile)
        infile.close()
        use_old_list = input("Previous list found. Do you want to load? (Y/N) ")
        if use_old_list[0].lower() == 'y':
            return todo_list
        else:
            return ToDoList()
        
    except:
        print('No previous list found. Staring with empty to do list.')
        return ToDoList()
    

# Create class for list of ToDoItem, with required functionality
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
        print('Item does not exist')
                
    # This function can inform whether an ToDoItem can be editted or if it doesn't exist
    def item_exist(self, item_e):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].description == item_e:
                return True
        return False 
    
    # Finding the index of a ToDoItem allows us to then call any item method.
    # Otherwise each ToDoItem method would require a separate ToDoList method.
    def find_item(self, item_f):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].description == item_f:
                return i
        
    # Each print option has a separate method (not condensed due to different printing)
    def print_items(self):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].complete:
                completed_str = ' is completed'
            else:
                completed_str = ' is not completed'
            print(self.actual_list[i].description + ' due on ' + 
                      self.actual_list[i].date_str + completed_str)
            
    def print_incomp_items(self):
        for i in range(len(self.actual_list)):
            if not self.actual_list[i].complete:
                print(self.actual_list[i].description + ' due on ' + 
                      self.actual_list[i].date_str)
    
    def print_comp_items(self):
        for i in range(len(self.actual_list)):
            if self.actual_list[i].complete:
                print(self.actual_list[i].description + ' due on ' + 
                      self.actual_list[i].date_str)

    def print_overdue_items(self):
        for i in range(len(self.actual_list)):
            if (not self.actual_list[i].complete) and datetime.now() > self.actual_list[i].date_obj:
                print(self.actual_list[i].description + ' due on ' + 
                      self.actual_list[i].date_str)

    def print_search_items(self, search):
        for i in range(len(self.actual_list)):
            if search.lower() in self.actual_list[i].description.lower():
                if self.actual_list[i].complete:
                    completed_str = ' is completed'
                else:
                    completed_str = ' is not completed'
                print(self.actual_list[i].description + ' due on ' + 
                          self.actual_list[i].date_str + completed_str)


# Create class for to do item
class ToDoItem:
    
    def __init__(self, description, date):
        self.description = description
        self.complete = False # Items are always created as incomplete
        self.date_str = date
        self.date_obj = datetime.strptime(date, '%d/%m/%Y')
        
    # Date is stored as string and date format for printing and filtering
    def edit_date(self, date):
        self.date_str = date
        self.date_obj = datetime.strptime(date, '%d/%m/%Y')
        
    def mark_as_complete(self):
        self.complete = True
        
    def edit_description(self, new_description):
        self.description = new_description

