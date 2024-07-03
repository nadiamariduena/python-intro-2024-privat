strings = [ "apple", "banana", "cherry", "date", "elderberry"]

reversed_strings = list(map(lambda s: s[::-1], strings))
#[::-1] is a slicing notation used to reverse a sequence (string, list, tuple, etc.).

print(reversed_strings)
#RESULT
# #['elppa', 'ananab', 'yrrehc', 'etad', 'yrrebredle']