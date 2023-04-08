# print("Welcome to the Adventure Game!")

# print("You are in a dark forest and need to find your way out.")

# direction = ""
# while direction != "q":
#     print("You can go 'north', 'south', 'east', or 'west'.")
#     direction = input("Which way do you want to go? (q to quit) ").lower()

#     if direction == "north":
#         print("You walk into a clearing and see a river.")
#         print("You can either follow the river or go back.")
#         choice = input("What do you want to do? ").lower()
#         if choice == "follow the river":
#             print("You follow the river and eventually find your way out of the forest.")
#             print("Congratulations! You have won the game.")
#             break
#         elif choice == "go back":
#             continue
#         else:
#             print("Invalid choice. Try again.")

#     elif direction == "south":
#         print("You walk into a swamp and get lost.")
#         print("You lose the game.")
#         break

#     elif direction == "east":
#         print("You walk into a dense part of the forest and get lost.")
#         print("You lose the game.")
#         break

#     elif direction == "west":
#         print("You walk into a dark cave and see a glimmer of light.")
#         print("You can either follow the light or go back.")
#         choice = input("What do you want to do? ").lower()
#         if choice == "follow the light":
#             print("You find a treasure and become rich.")
#             print("Congratulations! You have won the game.")
#             break
#         elif choice == "go back":
#             continue
#         else:
#             print("Invalid choice. Try again.")
#     else:
#         print("Invalid direction. Try again.")

# print("Thanks for playing the Adventure Game!")









# board = [" " for x in range(9)]

# def print_board():
#     row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
#     row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
#     row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

#     print()
#     print(row1)
#     print(row2)
#     print(row3)
#     print()

# def player_move(icon):
#     if icon == "X":
#         number = 1
#     elif icon == "O":
#         number = 2
#     print("Your turn player {}".format(number))
#     choice = int(input("Enter your move (1-9): ").strip())
#     if board[choice - 1] == " ":
#         board[choice - 1] = icon
#     else:
#         print()
#         print("That space is already taken!")

# def is_victory(icon):
#     if (board[0] == icon and board[1] == icon and board[2] == icon) or \
#        (board[3] == icon and board[4] == icon and board[5] == icon) or \
#        (board[6] == icon and board[7] == icon and board[8] == icon) or \
#        (board[0] == icon and board[3] == icon and board[6] == icon) or \
#        (board[1] == icon and board[4] == icon and board[7] == icon) or \
#        (board[2] == icon and board[5] == icon and board[8] == icon) or \
#        (board[0] == icon and board[4] == icon and board[8] == icon) or \
#        (board[2] == icon and board[4] == icon and board[6] == icon):
#         return True
#     else:
#         return False

# def is_draw():
#     if " " not in board:
#         return True
#     else:
#         return False

# while True:
#     print_board()
#     player_move("X")
#     print_board()
#     if is_victory("X"):
#         print("X wins! Congratulations!")
#         break
#     elif is_draw():
#         print("It's a draw!")
#         break
#     player_move("O")
#     if is_victory("O"):
#         print_board()
#         print("O wins! Congratulations!")
#         break
#     elif is_draw():
#         print("It's a draw!")
#         break

# print("Thanks for playing!")
