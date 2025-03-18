# Day 7: Write a function to count unique words in a string.
def count_unique_words(string):
    words = string.split()
    unique_words = set(words)
    print(unique_words)
    return len(unique_words)
string = "Hello world! Hello Python!"
print(count_unique_words(string))