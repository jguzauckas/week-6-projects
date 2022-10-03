# This code extracts all of the 6,792 names in the file names.txt
# and puts them into a list called "names". This project revolves
# around working with this list to do various things.
my_file = open("data/names.txt", "r")
content = my_file.read()
names = content.split(",")
my_file.close()

# To confirm my comment on line 1, print out a brief sentence describing
# how many elements are in names  (include a thousands separator!)


# Loop through the list and print a short statement about whether or not
# your name is in there.


# Loop through the list and print a short statement describing where your
# name is in the list (position/index)


# Create a function that checks if a provided name (in the form of a
# string) is in the list of names. This function should return True
# or False.


# Using the function you just created, check if one of your friends' names
# is in the list, and if it isn't, add it. Make a statement either way to
# show what is happening (i.e. "Their name was there already")


# Again using the function, have the user enter a name, and use the
# function to check if the name is in the list, and if it isn't, add
# it. Make a statement either way to show what is happening (i.e.
# "Their name was there already")


# Create a function that counts the number of names in the list start
# with a character, and return that count to the user. It should take
# in the the character to check for as a string parameter, and go
# through the whole list checking to see if it matches the first
# character in each name (adding to the counter if it does)


# Print out statements about how many names start with each of two
# different characters by calling your function above. Then print out
# which of the two characters had more names


# Create another function that takes in two string (character)
# parameters and counts the number of names that start with the first
# character *and* end with the second character, returning the count


# Print out a statement about how many names start/end with two
# characters you choose


# Create another function that takes in two string (character)
# parameters and counts the number of names that start with the first
# character or start with the second character, returning the count


# Print out a statement about how many names started with the two
# characters you choose


# Create another function that takes in one string parameter, which
# will be made up of two characters, and counts the number of names
# that start with those two characters in the same order, returning
# the count (this requires slicing!)


# Create another function that takes in one string parameter, which
# will be made up of two characters, and counts the number of names
# that end with those two characters in the same order, returning
# the count (this requires slicing!)


# Choose two characters to check for. Print the number of names that
# start with those two characters, and then print the number of names
# that end with those two characters.
