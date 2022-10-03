# This code extracts all of the 6,792 names in the file names.txt
# and puts them into a list called "names". This project revolves
# around working with this list to do various things.
my_file = open("data/names.txt", "r")
content = my_file.read()
names = content.split(",")
my_file.close()

# To confirm my comment on line 1, print out a brief sentence describing
# how many elements are in names (include a thousands separator!)
print(f"There are {len(names):,} names in the list.")

# Loop through the list and print a short statement about whether or not
# your name is in there.
john = False
for name in names:
    if name == "John":
        john = True
        break
if john:
    print("John is in the list!")
else:
    print("John was not in the list!")

# Loop through the list and print a short statement describing where your
# name is in the list (position/index)
for position, name in enumerate(names):
    if name == "John":
        print(f"{name} is in the list at position {position}!")
        break

# Create a function that checks if a provided name (in the form of a
# string) is in the list of names. This function should return True
# or False.
def namecheck(chkname):
    for name in names:
        if chkname == name:
            return True
    return False


# Using the function you just created, check if one of your friends' names
# is in the list, and if it isn't, add it. Make a statement either way to
# show what is happening (i.e. "Their name was there already")
friendname = "Allison"
if namecheck(friendname):
    print(f"{friendname} is already in the list!")
else:
    names.append(friendname)
    print(f"{friendname} was not in the list, but is now!")

# Again using the function, have the user enter a name, and use the
# function to check if the name is in the list, and if it isn't, add
# it. Make a statement either way to show what is happening (i.e.
# "Their name was there already")
username = input("Enter a name to check for: ")
if namecheck(username):
    print(f"{username} is already in the list!")
else:
    names.append(username)
    print(f"{username} was not in the list, but is now!")

# Create a function that counts the number of names in the list start
# with a character, and return that count to the user. It should take
# in the the character to check for as a string parameter, and go
# through the whole list checking to see if it matches the first
# character in each name (adding to the counter if it does)
def startletter(letter):
    count = 0
    for name in names:
        if name[0] == letter:
            count += 1
    return count


# Print out statements about how many names start with each of two
# different characters by calling your function above. Then print out
# which of the two characters had more names
letter1 = "A"
print(
    f"{startletter(letter1)} names appear in the list that start",
    f"with the letter {letter1}.",
)
letter2 = "B"
print(
    f"{startletter(letter2)} names appear in the list that start",
    f"with the letter {letter2}.",
)

# Create another function that takes in two string (character)
# parameters and counts the number of names that start with the first
# character *and* end with the second character, returning the count
def startandend(start, end):
    count = 0
    for name in names:
        if name[0] == start and name[-1] == end:
            count += 1
    return count


# Print out a statement about how many names start/end with two
# characters you choose
start1 = "A"
end1 = "b"
print(f"{startandend(start1, end1)} names start with {start1} and end with {end1}")

# Create another function that takes in two string (character)
# parameters and counts the number of names that start with the first
# character or start with the second character, returning the count
def startorstart(start1, start2):
    count = 0
    for name in names:
        if name[0] == start1 or name[-1] == start2:
            count += 1
    return count


# Print out a statement about how many names started with the two
# characters you choose
start2 = "H"
print(f"{startorstart(start1, start2)} names start with {start1} or {start2}")

# Create another function that takes in one string parameter, which
# will be made up of two characters, and counts the number of names
# that start with those two characters in the same order, returning
# the count (this requires slicing!)
def startstring(start):
    count = 0
    for name in names:
        if name[:2] == start:
            count += 1
    return count


# Create another function that takes in one string parameter, which
# will be made up of two characters, and counts the number of names
# that end with those two characters in the same order, returning
# the count (this requires slicing!)
def endstring(end):
    count = 0
    for name in names:
        if name[-2:] == end:
            count += 1
    return count


# Choose two characters to check for. Print the number of names that
# start with those two characters, and then print the number of names
# that end with those two characters in lowercase.
startstr = "Ac"
endstr = "ac"
print(f"{startstring(startstr)} names started with {startstr}.")
print(f"{endstring(endstr)} names ended with {endstr}.")
