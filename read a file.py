
# Without handling exceptions

#with open('D:\\Linux\\test.xt') as file:
    #print(file.read())

#print(file.closed) # shows if the file was closed after reading
                    # with open closes the file after reading

# handle exceptions

try:
    with open('D:\\Linux\\test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print('File Not Found')