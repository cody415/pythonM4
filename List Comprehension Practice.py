# Test dictionary
test_dict = {'a': 4, 'b': 2, 'c': 4, 'd': 2, 'e': 4, 'f': 6}

# Value to check
value_to_check = 4

# Count frequency using list comprehension
frequency = sum([1 for v in test_dict.values() if v == value_to_check])

print("Dictionary:", test_dict)
print(f"Frequency of {value_to_check}: {frequency}")
