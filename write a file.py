
# create new file/overwrite text in existing file

text = 'Hey Girl\nHave a nice day\nAnd and awesome week\n'
with open('D:\\Linux\\write.txt','w') as file: # w overwrites
    file.write(text)

# append text

text = 'Hey Boy\nHave a nice day\n'
with open('D:\\Linux\\write.txt','a') as file: # a appends
    file.write(text)
