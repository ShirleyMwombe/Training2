#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):  # accepts loud function as func # higher order function
    text = func('Hello')  # loud renamed to func, accepts Hello as an argument
    print(text)

hello(loud)  # calling the hello function with loud function as an argument
hello(quiet)  # calling the hello function with quiet function as an argument

# example 2

def divisor(x):
    def dividend(y):  # function skipped at first because it's not called yet
        return y/x
    return dividend  # divisor accepts value of x and returns dividend function

divide = divisor(3)  # calls divisor functions and assigns value of 3 to x (value of x is 3)
                    # divisor returns dividend function, which is hence assigned to dividend variable
                    # therefore divide=dividend()

print(divide(15))  # same value as print(dividend(10) # assigns 15 to y

