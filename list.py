# Create a calendar dictorary wiht events  and days of week and time this event are schedueled
calendar={
    "Monday": {"12:00": "Lunch with friends", "14:00": "Meeting with boss"},
    "Tuesday": {"10:00": "Gym session", "16:00": "Dinner with family"},
    "Wednesday": {"09:00": "Work project", "18:00": "Movie night"},
    "Thursday": {"11:00": "Yoga class", "20:00": "Family dinner"},
    "Friday": {"08:00": "Coffee with friends", "22:00": "Party with friends"},
    "Saturday": {"13:00": "Dinner with friends", "19:00": "Gym session"},
    "Sunday": {"14:00": "Family movie night", "21:00": "Dinner with family"}

}
# print(calendar["Monday"]["12:00"])

students_={
    2541:"Admin Number"


}

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

