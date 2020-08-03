
# players = [{"name": "max verstappen", "numbers": {1, 2, 3, 4, 5}},
#            {"name": "alex albon", "numbers": {6, 7, 8, 9, 10}}]
#
# max = players[0]["numbers"].intersection(lottery_numbers)
# max_correct_number = len(max)
#
# alex = players[0]["numbers"].intersection(lottery_numbers)
# alex_correct_number = len(alex)
#
# max_v = players[0]["name"]
# alex_a = players[1]["name"]
#
# print(max_v + " you have guessed " + str(max_correct_number) + " correct number")
#
# print(alex_a + " you have guessed " + str(alex_correct_number) + " correct number")


# user_input = input("Please press 'p' if you want to print or press 'q' if you want to exit without printing: ")
#
# while user_input != "q":
#
#     if user_input == "p":
#         print("Hello")
#
#     user_input = input("Please press 'p' if you want to print or press 'q' if you want to exit without printing: ")



# students = [{"name": "Joey", "grade": 90},
#             {"name": "Chandler", "grade": 86},
#             {"name": "Ross", "grade": 99}
#             ]
# for i in students:
#     name = i["name"]
#     grade = i["grade"]
#     print(f"{name} has a grade of {grade}.")

# currencies = (0.8, 1.2)
# usd, eur = currencies
# print(usd)
# print(eur)


# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok", "ok"]
#
# #break
# for i in cars:
#   if i == "faulty":
#     print(f"This car is {i}. production will now stop")
#     break
#   print(f"This car is {i}")
#   print("Shipping to the dealership!")
# else:
#     print("All cars built successfully!!!")

# for i in range(2, 10):
#     for x in range(2, i):
#         if i % x == 0:
#             print(f"{i} equals {x} * {i//x}")
#             break
#     else:
#         print(f"{i} is a prime number.")

# friends = ["rofl", "jon", "anna"]
#
# for counter, friend in enumerate(friends):
#     print(counter)
#     print(friend)
# print(list(enumerate(friends)))
# print(dict(enumerate(friends)))




# import random
#
# lottery_numbers = set(random.sample(range(22), 6))
#
# players = [
#     {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
#     {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
#     {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
#     {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
# ]
#
# top_player = players[0]
#
# for player in players:
#     matched_numbers = len(player["numbers"].intersection(lottery_numbers))
#     if matched_numbers > len(
#             top_player["numbers"].intersection(lottery_numbers)):
#         top_player = player
#
#
# winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
#
# print(f"{top_player['name']} won {winnings}.")


# def greet_customer(name, number):
#     print(f"Hello {name} we have {number} apples in stock")
#
# greet_customer("joey", 4)
# greet_customer("chandler", 8)
# greet_customer("ross", 12)

# def sum(a, b):
#     print(a+b)
#
# rate = sum(5, 6)

# fruits = ["apples", "oranges", "grapes"]
# for i in fruits:
#     print(i)
# else: print ("no more fruits left")


def returnsum(a, b, c):
    return(a + b + c)

x = returnsum(10, 50, 40)
print(x)