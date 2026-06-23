# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Method 1: Using ^ operator
sym_diff1 = set1 ^ set2

# Method 2: Using symmetric_difference() method
sym_diff2 = set1.symmetric_difference(set2)

# Print results
print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference (using ^):", sym_diff1)
print("Sym
