# Day 1: Build a shopping list app (add/remove items).
# Create a shopping list app that allows a user to add and remove items from a shopping list.
# The shopping list should be a list of strings.
# The user should be able to add items to the list and remove items from the list.
# The user should also be able to view the current shopping list.
# The user should be able to enter a command to perform an action.
# For example, the user could enter "add eggs" to add eggs to the shopping list.
# The user could enter "remove eggs" to remove eggs from the shopping list.
# The user could enter "view list" to view the current shopping list.

# Day 2: Add a feature to check if an item is already in the list.      
# Add a feature to check if an item is already in the list before adding it.

# Day 3: Add a feature to clear the list.
# Add a feature to clear the list.




# 

# Problem 1: shopping_list.insert(0,shopping_list) is inserting the list into itself, causing infinite nesting
# Problem 2: shopping_list.append(shopping_list) is appending the list to itself, causing infinite nesting 
# Problem 3: The shopping_item input is never actually added to the list
# Problem 4: No command handling for add/remove/view functionality

shopping_list = ["sugar"]

shopping_item = input(" Enter What You are going to shop🏬: ")

# Should be:
# if shopping_item not in shopping_list:
def add_item(shopping_item):
    if shopping_item in shopping_list:
        print(f'{shopping_item} already in shopping list')
        return
    shopping_list.append(shopping_item)
    print(f'{shopping_item} added to shopping list.... {shopping_list}')

for items in shopping_list:
    print(items)

add_item(shopping_item)
