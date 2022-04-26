# John Beech / Tuesday 26th April 2022
name = input("What is your name? ")
print("Awful to meet you", name, "!")

colour = input("What is your favourite colour? ")
print("I hate", colour, "inverted", colour, "is my favourite colour!")

weather = input("What is the weather like today? ")
print('There\'s a 72% chance that weather will be', weather, 'on any given day!')

orderCount = int(input("How many wooden planks do you want to buy? "))
orderSize = int(input("How long (in mm) do you want each wooden plank to be? "))
print("So you want", orderCount, "planks of wood which are", orderSize, "mm each in length, totalling to", (orderCount * orderSize), "mm of wooden planks!")
