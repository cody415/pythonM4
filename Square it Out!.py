# Define the range
start = 1
end = 10

# Empty lists for squares, odd squares, and even squares
squares = []
odd_squares = []
even_squares = []

# Generate squares and separate odd/even
for n in range(start, end+1):
    sq = n * n
    squares.append(sq)
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Print results
print("Squares from", start, "to", end, ":", squares)
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)
