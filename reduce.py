# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools
name = ['L','A','M','O','N','T']

Leo = functools.reduce(lambda x,y:x+y,name)

print(Leo)

factorial = (5,4,3,2,1)
result = functools.reduce(lambda x,y:x*y,factorial)

print(result)