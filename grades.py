# This code extracts all of the 10,000 grades in the file grades.txt
# and puts them into a tuple called "grades". This project revolves
# around working with this tuple to do various things.
my_file = open("data/grades.txt", "r")
content = my_file.read()
grades = tuple(map(int, content.split(",")))
my_file.close()

# To confirm my comment on line 1, print out a brief sentence describing
# how many elements are in grades (include a thousands separator!).


# Create a function to calculate the average overall grade from the data
# To calculate an average, we need to add up all of the provided grades
# (use a loop) and then divide by the total number of grades. This
# function does not need a parameter, but should return the average.


# Print a statement about the average grade using your function.
# Limit the average to 2 decimal places.


# Create a similar function that only averages the grades above
# a parameter score.


# Print a statement about the average grades above 50 using your
# function. Limit the average to 2 decimal places.


# Create a function that counts the number of grades above a provided
# number (as a parameter), and returns that count to the user. For
# example, providing 83 as a parameter would count the number of grades
# that are 84 or above (above 83) and return that number.


# Call your function with two different grades and print
# statements about each output.


# [HARD] Create a function that creates and returns a dictionary
# whose keys are grade letters (A, B, C, D, F) and whose values
# are the number of grades that fall into that grade category.


# Call your function and assign the returned value to a new dictionary
# Print out the number of each letter grade by printing the dictionary


# Create a function that checks the number of grades between two
# provided parameters, and returns True if more than 10% of grades
# are within the parameters, and False if not


# Call your function twice, with different parameters both times and
# make a statement about whether those ranges had at least 10% of scores


# [HARD] Create a function that calculates the percentage of students
# above a certain score, passed in as a parameter. To do this, utilize
# the function we made earlier which counted the number of scores above
# a given score and divide the result by the total number of scores.
# Return this result.


# Call the function with a score value provided and print the result
# using our type formatting to display it as a percentage with 2 decimal
# places!
