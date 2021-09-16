# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

squares = []
for i in range(1, 10):
    squares.append(i*i)
print(squares)

# alternative

squares = [i*i for i in range(1, 10)]  # list comprehension
print(squares)

print(" ")

# ex 2
marks = [90, 80, 70, 60, 50, 40, 30, 20, 10]

passed = list(filter(lambda x: x >= 50, marks))
print(passed)

# alternative
passed = list((i for i in marks if i >= 50))  # list comprehension
print(passed)

scores = list((i if i >= 50 else 'FAILED' for i in marks))
print(scores)