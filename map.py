# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [('Shoes',800),
         ('Tops',300),
         ('Jeans',700),
         ('Dress',500)]

tax = lambda data: (data[0],data[1]*0.16)

store_tax = map(tax,store)

for i in store_tax:
    print(i)