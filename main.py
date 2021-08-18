# firstNumber = float(input("First number "))
# secondNumber = float(input("Second number "))
# total = firstNumber + secondNumber
# print("Total ", total)


# weight = float(input("Enter weight: "))
# unit = str(input("(K)g or (L)bs: "))

# if else
# if unit == "k" or unit == "K":
#     print("Weight in Kg: ", weight / 0.45)
# elif unit == "l" or unit == "L":
#     print("Weight in LBS: ", weight * 0.45)
# else:
#     print("Invalid input")

# while
# i = 1
# while i <= 100:
#     print(i * "*")
#     i += 1


# list
# names = ["Allwin", "Buck", "Muc", "Snipe", "Mick"]
#
# print(names)
# names[0] = "AllwiN_"
# print(names[0])
# print(names[-1])
# print(names[-2])
# print(names[0:3])


# list
# numbers = [0, 1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0, 6)
# numbers.remove(4)
# # numbers.clear()
# print(numbers)
# print(8 in numbers)
# print(len(numbers))  # returns element count


# for loop
# numbers = [0, 1, 2, 3, 4, 5]
#
# for item in numbers:
#     print(item)


# range
# numbers = range(5)
# numbers = range(5, 10)
# numbers = range(5, 10, 2)
#
# print(numbers)
# for number in numbers:
#     print(number)


# tuples (immutable, not changeable)
# numbers = (1, 2, 3, 3, 4, 5)
#
# print(numbers.count(3))  # count of 3
# print(numbers.index(3))  # index


# car game

commands = ["help", "start", "stop", "quit"]
userInputCommand = ""
isCarStarted = False
isCarStopped = False
while True:
    userInputCommand = str(input("> ")).lower()
    if userInputCommand == commands[0]:
        print("""
Start - to start the car
Stop - to stop  the car
Quit - exit
        """)
    elif userInputCommand == commands[1]:
        if isCarStarted:
            print("Yo, It's already running")
        else:
            isCarStarted = True
            isCarStopped = False
            print("Card started.. wroom.. wroom..")
    elif userInputCommand == commands[2]:
        if isCarStopped:
            print("Yo, It's already stopped")
        else:
            isCarStopped = True
            isCarStarted = False
            print("Car stopped")
    elif userInputCommand == commands[3]:
        print("GAME OVER")
        break
    else:
        print("Uh oh.. I don't understand the command..")
