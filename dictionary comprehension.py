# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

City_F = {'Nairobi': 40, 'Kisumu': 100, 'Mombasa': 105, 'Nakuru': 60}

City_C = {key: round((value-32)*(5/9)) for (key,value) in City_F.items()}  # dictionary comprehension
print(City_C)
print(' ')

# if conditional

weather = {'Nairobi': 'cold', 'Kisumu': "hot", 'Mombasa': 'hot', 'Nakuru': 'warm'}
condition = {key: value for (key,value) in weather.items() if value == 'hot'}
print(condition)
print(' ')

# if else

weather = {'Nairobi': 'cold', 'Kisumu': "hot", 'Mombasa': 'hot', 'Nakuru': 'warm'}
sunny = {key: 'Yes' if value == 'hot' else 'Nope' for (key,value) in weather.items()}
print(sunny)
print(' ')

# function
City_F = {'Nairobi': 40, 'Kisumu': 100, 'Mombasa': 105, 'Nakuru': 60}

def hot_or_not(value):
    if value >= 70:
        return 'HOT'
    elif 69 >= value >= 45:
        return 'WARM'
    else:
        return 'COLD'


condition = {key: hot_or_not(value) for (key,value) in City_F.items()}
print(condition)
