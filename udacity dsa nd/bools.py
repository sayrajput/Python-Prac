#Good and Bad Examples
#Here are some things to keep in mind while writing boolean expressions for your if statements.

# 1. Don't use True or False as conditions
# Bad example
if True:
    print("This indented code will always get run.")

#While "True" is a valid boolean expression, it's not useful as a condition since it always evaluates to True, so the indented code will always get run. Similarly,
#if False is not a condition you should use either - the statement following this if statement would never be executed.

# Another bad example
if is_cold or not is_cold:
    print("This indented code will always get run.")

#Similarly, it's useless to use any condition that you know will always evaluate to True, like this example above. A boolean variable can only be True or False, so either is_cold or not is_cold is always True, and the indented code will always be run.


#2. Be careful writing expressions that use logical operators
#Logical operators and, or and not have specific meanings that aren't quite the same as their meanings in plain English. Make sure your boolean expressions are being evaluated the way you expect them to.

# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")


# Bad example
if is_cold == True:
    print("The weather is cold!")
    
# Good example
if is_cold:
    print("The weather is cold!")
    
    

"""
Truth Value Testing
If we use a non-boolean object as a condition in an if statement in place of the boolean expression, 
Python will check for its truth value and use that to decide whether or not to run the indented code.
By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

Here are most of the built-in objects that are considered False in Python:

constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)
Example:
"""
errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")


#In this code, errors has the truth value True because it's a non-zero number, so the error message is printed.
#This is a nice, succinct way of writing an if statement.




#refer to   .py

points = 174

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)
