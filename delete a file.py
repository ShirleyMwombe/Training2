import os
import shutil

path = 'folder'

try:
    #os.remove(path)  # deletes file
    #os.rmdir(path)  # deletes empty folder
    shutil.rmtree(path)  # deletes non-empty folders recursively
except FileNotFoundError as e:
    print('Not deleted')
    print(e)
except PermissionError as e:
    print('You have no permissions')
    print(e)
else:
    print(path+' was deleted')