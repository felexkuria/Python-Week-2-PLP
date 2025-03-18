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
# can be acessed using index
print(calendar["Monday"]["12:00"])

# Common dictionary methods:
# .get() - safely access values with a default fallback
# calendar.get("Monday", {}) - Attempts to get the value for key "Monday". If not found, returns empty dict {}
# .get("12:00", "No event scheduled") - On the result of first get(), attempts to get value for "12:00"
#                                      If not found, returns "No event scheduled"
# This nested get() approach safely handles missing keys without raising KeyError exceptions
print(calendar.get("Monday", {}).get("12:00", "No event scheduled"))

# .items() - get key-value pairs
for day, events in calendar.items():
    print(f"{day}: {events}")

# .update() - merge or update dictionary
new_events = {"Monday": {"16:00": "New meeting"}}
calendar.update(new_events)

# .pop() - remove and return value
removed = calendar["Monday"].pop("12:00", "No such event")

# .clear() - remove all items
temp_dict = calendar.copy()  # Make a copy first
temp_dict.clear()

# Dictionaries don't have a .map() method directly
# To achieve similar functionality, use dictionary comprehension:
uppercase_events = {day: {time: event.upper() 
                  for time, event in events.items()}
                  for day, events in calendar.items()}
# can be looped
for day in calendar :
   print(day.capitalize())
#can accesed using .keys metod 
for key in calendar.keys():
   print(key)

for value in calendar.values():
   print(value)