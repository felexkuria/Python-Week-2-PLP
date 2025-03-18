
# Lists 
# * can be indexed sorted reversed inserted  and removed
# * can be nested
shoppping_list=[
    "apples",
    "bananas",
    "oranges",
    "milk",
    "bread",
    "eggs"
]
# ❓ Q1: How would you remove the last item from fruits = ["apple", "banana"]?
fruits = ["apple", "banana"]
fruits.pop()
print(fruits)
fruits.remove("banana")
print(fruits)
# Reverse this list using a method: nums = [1, 2, 3]
nums=[1,2,3]
nums.reverse()
print(nums)
for item in shoppping_list:
    print(item)
#can be indexed
print(shoppping_list[2])
#can be sorted
print(sorted(shoppping_list))
#can be reversed
print(list(reversed(shoppping_list)))

# .reverse() modifies the list in place and returns None
# To see the reversed list, either:
# 1. Print the list after calling .reverse(), or
# 2. Use reversed() which returns a new reversed iterator
shoppping_list.sort()
print(shoppping_list)
#can be inserted
shoppping_list.insert(0,"cheese")
shoppping_list.append("cheese")


no_of_chheese=shoppping_list.count("cheese")
print(no_of_chheese)

#can be removed
shoppping_list.remove("cheese")
print(f"{shoppping_list} Is Removed")
print(f"{shoppping_list.pop(0)}  Is Popped at bottom")
print(f"{shoppping_list.pop()} Is Popped at bottom")
print(shoppping_list)

