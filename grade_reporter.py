scores = [72, 45, 90, 61, 38]

# Initialize tracking variables
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score to evaluate grades and tally results
for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    # Print score and grade
    print(f"Score: {score} - Grade: {grade}")

    # Track pass/fail counts
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

    # Add to cumulative sum for average calculation
    total_score += score

# Calculate and round the average
average = round(total_score / len(scores), 1)

# Print final summary stats
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {average}")