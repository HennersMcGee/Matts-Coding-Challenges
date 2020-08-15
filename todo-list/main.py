# -*- coding: utf-8 -*-
'''
    File name: main.py
    Author: Henry Letton
    Date created: 2020-08-14
    Python Version: 3.7
    Desciption: This program manages a user todo list, using CLI.
'''

# Import required modules
from datetime import datetime # For dealing with due dates
import pickle # For saving list to disc
import os # For moving working directory

# Make sure the wording directory is the same location as these (example below)
# os.getcwd()
# os.chdir('C:\\Users\\Henry\\OneDrive\\Documents\\Python\\Matts-Coding-Challenges\\todo-list')


# Import functions and objects from other file
from fn_and_obj import load_prev_list, save_list_to_disc, ToDoList, ToDoItem


# New to do list or can use previous
your_todo_list = load_prev_list()


# Create while loop to ask for user input repeatably until the user is finished
user_editing = True # Break variable, when set to false will end while loop

while user_editing:
    
    print('\nYour options are:')
    print('1 - Add a new to do item')
    print('2 - Delete an item')
    print('3 - Edit item description')
    print('4 - Edit item due date')
    print('5 - Mark item as completed')
    print('6 - See all incomplete items')
    print('7 - See all complete items')
    print('8 - See all items')
    print('9 - See all overdue items')
    print('10 - Search in items')
    print('99 - Exit. This will close edit and save your list.')

    change = input("Please enter a number corresponding to the change you would like to make: ")

    if change == '1':
        item_name = input("What is the item description? ")
        due_date = input("When is the due date? (This must be in the format DD/MM/YYYY) ")
        
        # Error handling, in case the date is not entered correctly
        no_date = True
        while no_date:
            try:
                your_todo_list.add_item(ToDoItem(item_name, due_date))
                no_date = False
            except:
                due_date = input("The format must be DD/MM/YYYY. Pleae enter again: ")

    elif change == '2':
        item_name = input("What is this item description? ")
        your_todo_list.remove_item(item_name)

    # For any todo item edits, they are first checked to exist
    elif change == '3':
        item_name = input("What is this item description? ")
        if your_todo_list.item_exist(item_name):
            item_new_name = input("What is this new item description? ")
            idx = your_todo_list.find_item(item_name)
            your_todo_list.actual_list[idx].edit_description(item_new_name)
        else:
            print('Item does not exist')
        
    elif change == '4':
        item_name = input("What is this item description? ")
        if your_todo_list.item_exist(item_name):
            item_new_date = input("What is this new item due date? ")
            idx = your_todo_list.find_item(item_name)
            your_todo_list.actual_list[idx].edit_date(item_new_name)
        else:
            print('Item does not exist')
        
    elif change == '5':
        item_name = input("What is this item description? ")
        if your_todo_list.item_exist(item_name):
            idx = your_todo_list.find_item(item_name)
            your_todo_list.actual_list[idx].mark_as_complete()
        else:
            print('Item does not exist')
        
    elif change == '6':
        your_todo_list.print_incomp_items()
        
    elif change == '7':
        your_todo_list.print_comp_items()

    elif change == '8':
        your_todo_list.print_items()

    elif change == '9':
        your_todo_list.print_overdue_items()

    elif change == '10':
        search = input("Enter a word or phrase to search (capitals do not matter) ")
        your_todo_list.print_search_items(search)

    elif change == '99':
        user_editing = False
        
    else:
        print('Your input was not recognised.')


print('You have exited list edit.\nYour list will now be saved on disc.')
save_list_to_disc(your_todo_list)



