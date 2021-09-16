# sort() method   = used with lists
# sort() function = used with iterables

# lists
friends = ['Shirley','Olyvia','Jacky','Tess','Eve']

friends.sort()

for i in friends:
    print(i)

print(' ')

# other iterables

buddies = ('Shirley','Diana','Mildred','Angie','Sally')

Buddies = sorted(buddies,reverse=True)

for i in Buddies:
    print(i)
print(' ')

# list of tuples

family = [('Karen','31','Girl'),
          ('Shirley','28','Girl'),
          ('Jim','24','Boy'),
          ('Rodney','20','Boy'),
          ('Russel','20','Boy')]

# family.sort(reverse=True)

age = lambda ages:ages[1]
family.sort(key=age)

for i in family:
    print(i)
print(' ')

# tuple of tuples

family = (('Karen','31','Girl'),
          ('Shirley','28','Girl'),
          ('Jim','24','Boy'),
          ('Rodney','20','Boy'),
          ('Russel','20','Boy'))

age = lambda ages:ages[1]
Family = sorted(family,key=age,reverse=True)

for i in Family:
    print(i)