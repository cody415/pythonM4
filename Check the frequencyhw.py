# Test dictionary
test_dict = {'a': 4, 'b': 2, 'c': 4, 'd': 2, 'e': 4, 'f': 6}

# Value to check frequency
value_to_check = 4

# Count frequency
frequency = list(test_dict.values()).count(value_to_check)

# Print result
print("Dictionary:", test_dict)
print(f"Frequency of {value_to_check}: {frequency}")
