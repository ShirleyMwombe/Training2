import os

path = 'D:\\Linux\\test'

if os.path.exists(path):
    print('That path exits')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print('That location does not exist')

