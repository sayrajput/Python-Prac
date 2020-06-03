#basic
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
##########################    #########                    ####                 #################################
"""
Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored,
which is stored in the integer variable points.

Points	Prize
1 - 50	wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin
"""

#sol1 
points = 174  # use this input to make your submission

a = "wooden rabit"
b = "wafer-thin mint"
c = "penguin"
rs = "Congratulations! You won a {}!"

# write your if statement here
if 1<=points<=50:
    result = rs.format(a)
elif 51<=points<=150:
    result = "Oh dear, no prize this time."
elif 151<=points<=180:
    result = rs.format(b)
elif 181<=points<=200:
    result = "Congratulations! You won a {}!".format(c)
else:
    result = "Oh dear, no prize this time."

print(result)


#sol2 cleaner

points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)


"""ExplanationWe use <= instead of the < operator, since it was stated that the upper bound is inclusive.
Notice that in each condition, we check if points is in a prize bracket by checking if points is less than or equal to the upper bound; we didn't have to check if it was greater than the lower bound. 
Let's see why this is the case.

When points = 174, it first checks if points <= 50, which evaluates to False.
We don't have to check if it is also greater than 0, since it is stated in the problem that points will always be a positive integer up to 200.

Since the first condition evaluates to False, it moves on to check the next condition, points <= 150.
We don't need to check if it is also greater than 50 here! We already know this is the case because the first condition has to have evaluated to False in order to get to this point.
If we know points <= 50 is False, then points > 50 must be True!

Finally, we check if points <= 180, which evaluates to True. We now know that points is in the 151 - 180 bracket.

The last prize bracket, 181-200, is caught in the else clause, since there is no other possible value of the prize after checking the previous conditions.

"""


