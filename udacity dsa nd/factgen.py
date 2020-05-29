#factorial using generators
"""
In this exercise, you will define prod(a, b) which returns the product of numbers a and b.
You will also define fact_gen() which yields the next factorial number.
"""



def prod(a,b):
    return a*b


def fact_gen():
    i = 1
    n = i

    while True:
        output = prod(n,i)
        yield output

        #update n and i
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120