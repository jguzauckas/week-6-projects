# This code takes the names from names.txt and assigns them to
# dictionary pairs with random amounts of money, and puts them
# into a dict called "bankaccts". This project revolves
# around working with this dict to do various things.
from hashlib import new


my_file = open("data/bank.txt", "r")
content = my_file.read()
rawaccts = content.split(",")
rawaccts.pop()
my_file.close()
bankaccts = {}
for acct in rawaccts:
    temp = acct.split(":")
    bankaccts[temp[0]] = float(temp[1])

# In this dictionary, the keys are the names and the
# values are the money held in the account.

# Using your name, determine how much money you have
# assigned to your account, limited to 2 decimal places.
name = "John"
print(f"{name} has ${bankaccts[name]:.2f}.")

# Using your name, change the amount in your account to
# a number you more prefer (probably higher).
bankaccts[name] = 1000.00

# Have the user enter a name, then have the user enter an amount
# Set the key via the name they enter to the amount they entered
# Note that we don't have to check if its already in the dict
# because dictionaries will change or create the value as needed.
username = input("Enter a name to update an account: ")
useramt = float(input("Enter an amount to assign to the balance: "))
bankaccts[username] = useramt

# Print a nice statement (using f-strings!) that tells your friend
# how much money they have, limited to two decimal places
friendname = "Emily"
print(f"{friendname} has ${bankaccts[friendname]:.2f}.")

# Choose a name and have that person spend $500. Print out their new
# balance, being sure to print a positive or negative sign to be
# clear about their amount of money
newname = "Todd"
bankaccts[newname] -= 500
print(f"{newname} now has ${bankaccts[newname]:.2f}")

# Create a function that takes a name (string), an interest rate (float)
# and a number of years (int). Have the function calculate the person's
# accrued interest over the number of years and then assign it to their
# account as the new value. To calculate interest, we do:
# original * (1 + interest rate) ^ years
def interest(name, rate, years):
    bankaccts[name] *= (1 + rate) ** years


# Call the function on you and your friend with 2% and 4% respectively
# over 10 years and make a statement about the accrued interests
# including formatted percentages and money limited to 2 decimal places
interest(name, 0.02, 10)
interest(friendname, 0.04, 10)
print(f"{name} has ${bankaccts[name]:.2f}.")
print(f"{friendname} has ${bankaccts[friendname]:.2f}.")

# Create a function that takes in two names (strings) and checks which
# one has a higher account balance, returning the "winner" as a string
def higher(name1, name2):
    if bankaccts[name1] >= bankaccts[name2]:
        return name1
    else:
        return name2


# Call the function on you and your friend to see who has the higher
# account balance and print the formatted results.
print(f"Between {name} and {friendname}, {higher(name, friendname)} has the most money")

# If you had to spend $200 per month on food, when you finally run out of
# money to afford a whole month, how much would you have left? Remainder!!
print(
    f"After buying food for {int(bankaccts[name] // 200)} months, I had ${bankaccts[name] % 200:.2f} left over."
)
