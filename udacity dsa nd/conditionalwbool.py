#1
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

#2
if is_raining and is_sunny:
    print("Is there a rainbow?")


#3   Let's say i want to send promotional email to a customer, if they have not requested not be taken off the email list,
# and they're in a location where they'll be able to redeem the offer
# In this type of complex situations we might need to combine ands,ors and nots together.
# However it's not that much complex ... let's make it easy
# This kind of situation needs patience and positivity and we can get a solution like...
# See how simple it is..

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")


# however simple or complex, the entire line in the if statement must be a Boolean expression that evaluates to either
# True or False
#and this value decides whether the code under 'if statement' executes or not

