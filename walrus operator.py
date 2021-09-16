
#foods = list()
#while True:
 #   food = input('Which food do you like?: ')
  #  if food == 'quit'.lower():
   #     break
    #foods.append(food)
#for i in foods:
 #   print(i)

# with walrus operator

foods = list()

while (food := input('Which food do you like?: ')) != 'quit':
    foods.append(food)

for i in foods:
    print(i)