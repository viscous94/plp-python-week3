count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement. Added ':' to fix the SyntaxError.
# BUG: Off-by-one condition 'count < 5' excluded 5 from the total (loop stopped at 4). Changed to 'count <= 5' to correctly include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Concatenating a string and integer with '+' caused a TypeError. Converted 'total' to a string using str(total).
print("Sum of 1 to 5 is: " + str(total))