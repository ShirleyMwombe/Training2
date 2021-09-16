import os

source = 'D:\\Linux\\test.txt'
destination = 'D:\\Python\\mv.txt'
try:
    if os.path.exists(destination):
        print('Path already exists')
    else:
        os.replace(source,destination)
        print('File Moved!')
except:
    print('File Not Moved')

# Move a Directory

source = 'D:\\Linux\\Test'
destination = 'D:\\Python\\Moved'
try:
    if os.path.exists(destination):
        print('Path already exists')
    else:
        os.replace(source,destination)
        print('Folder Moved!')
except:
    print('Folder Not Moved')