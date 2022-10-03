# This code extracts all of the 10,000 grades in the file grades.txt
# and puts them into a tuple called "grades". This project revolves
# around working with this tuple to do various things.
my_file = open("data/grades.txt", "r")
content = my_file.read()
grades = tuple(map(int, content.split(",")))
my_file.close()

# To confirm my comment on line 1, print out a brief sentence describing
# how many elements are in grades (include a thousands separator!).
print(f"This tuple has {len(grades):,} grades in it")

# Create a function to calculate the average overall grade from the data
# To calculate an average, we need to add up all of the provided grades
# (use a loop) and then divide by the total number of grades. This
# function does not need a parameter, but should return the average.
def average():
    sum = 0
    for grade in grades:
        sum += grade
    return sum / len(grades)


# Print a statement about the average grade using your function.
# Limit the average to 2 decimal places.
print(f"The average grade is {average():.2f}.")

# Create a similar function that only averages the grades above
# a parameter score.
def averageif(cutscore):
    count = 0
    sum = 0
    for grade in grades:
        if grade > cutscore:
            sum += grade
            count += 1
    return sum / count


# Print a statement about the average grades above 50 using your
# function and limit the number to 2 decimal places
print(f"The average grade above 50 is {averageif(50):.2f}.")

# Create a function that counts the number of grades above a provided
# number (as a parameter), and returns that count to the user. For
# example, providing 83 as a parameter would count the number of grades
# that are 84 or above (above 83) and return that number.
def abovegrade(cutscore):
    count = 0
    for grade in grades:
        if grade > cutscore:
            count += 1
    return count


# Call your function with two different grades and print
# statements about each output.
grade1 = 80
print(f"There are {abovegrade(grade1)} grades above {grade1}.")
grade2 = 75
print(f"There are {abovegrade(grade2)} grades above {grade2}.")

# [HARD] Create a function that creates and returns a dictionary
# whose keys are grade letters (A, B, C, D, F) and whose values
# are the number of grades that fall into that grade category.
def gradeletters():
    gradelettercounts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        if grade >= 90:
            gradelettercounts["A"] += 1
        elif grade >= 80:
            gradelettercounts["B"] += 1
        elif grade >= 70:
            gradelettercounts["C"] += 1
        elif grade >= 60:
            gradelettercounts["D"] += 1
        else:
            gradelettercounts["F"] += 1
    return gradelettercounts


# Call your function and assign the returned value to a new dictionary
# Print out the number of each letter grade by printing the dictionary
letters = gradeletters()
print(letters)

# Create a function that checks the number of grades between two
# provided parameters, and returns True if more than 10% of grades
# are within the parameters, and False if not
def between(low, high):
    count = 0
    for grade in grades:
        if low < grade and grade < high:
            count += 1
    percent = count / len(grades)
    if percent > 0.1:
        return True
    else:
        return False


# Call your function twice, with different parameters both times and
# make a statement about whether those ranges had at least 10% of scores
range1low = 60
range1high = 70
print(
    f"At least 10% of scores are below {range1high} and above {range1low}: {between(range1low, range1high)}"
)
range2low = 75
range2high = 80
print(
    f"At least 10% of scores are below {range2high} and above {range2low}: {between(range2low, range2high)}"
)

# [HARD] Create a function that calculates the percentage of students
# above a certain score, passed in as a parameter. To do this, utilize
# the function we made earlier which counted the number of scores above
# a given score and divide the result by the total number of scores.
# Return this result.
def abovepercentage(cutscore):
    return abovegrade(cutscore) / len(grades)


# Call the function with a score value provided and print the result
# using our type formatting to display it as a percentage with 2 decimal
# places!
cutgrade = 82
print(f"{abovepercentage(cutgrade):.2%} of students scored above {cutgrade}.")
