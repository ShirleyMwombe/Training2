
def hello():
    print('Hello!')

#print(hello)  # displays the memory address

hi = hello  # assigns the address to the variable hi

hi()  # can now be used interchangeably with hello() function
hello()
