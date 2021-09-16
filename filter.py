# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [('Chandler',27),
           ('Joey',25),
           ('Phoebe',27),
           ('Rachel',28),
           ('Monica',30),
           ('Ross',29)]
# age = lambda ages: ages[1] > 27


def age(ages):
    return ages[1] > 27

filter(age,friends)

oldies = list(filter(age,friends))

for i in oldies:
    print(i)