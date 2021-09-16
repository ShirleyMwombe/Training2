# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ['Jean','Roy','Nicky']
password = ('Hey@345','P@ssword','Sahara#123')
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

users = (zip(usernames,password))  # stored in tuples
print(type(users))
users = list((zip(usernames,password)))  # cast the tuple into a list

for i in users:
    print(i)

print(type(users))

users = dict((zip(usernames,password))) # cast into a dictionary

for key,value in users.items():
    print(key+' : '+value)

users = (zip(usernames,password,login_dates))

for i in users:
    print(i)