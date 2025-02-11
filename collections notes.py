# create list (bucket of fruit)
fruitList = ["Apple", "Banana", "Orange", "Grapes"]
#print the entire list
print(fruitList)
#print a specific item in the list
print(fruitList[1])
#update an item in the list
fruitList[1] = "Cherry"
print(fruitList)
#print the length of the list (How many items are in the list)
print(len(fruitList))
# Python will allow different data types in their lists.
differentList = ["Taco", 5]
print(differentList)
#print different ranges within our list.
#[index:offset] index starts with 0, offset starts with 1
print(fruitList[2:3])
print(fruitList[:3])
print(fruitList[2:])
#Add to our list
fruitList.append("Pear")
print(fruitList)
#insert into our list
fruitList.insert(2, "Lime")
print(fruitList)
#delete items from list
fruitList.remove("Cherry")
print(fruitList)
fruitList.pop(4)
print(fruitList)

#Creating a Tuple, parentheses, not brackets
veggieTuple = ("Carrots", "Peas", "Lettuce")
print(veggieTuple)
#tuples, unlike lists, are immutable, meaning it cannot be changed
print(len(veggieTuple))

