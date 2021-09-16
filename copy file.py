# copyfile() == copies contents of a file
# copy() == copyfile()+ permission mode + destination can be a directory
# copy2() == copy() + copies metadata

import shutil

# shutil.copyfile('D:\\Linux\\write.txt','copy.txt')

#with open('copy.txt') as file:
 #   print(file.read())


shutil.copy2('D:\\Linux\\write.txt','copy.txt')