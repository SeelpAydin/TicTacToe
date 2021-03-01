#!/usr/bin/python3

from os import system
from platform import system as platform

# Defining Function and Variables


def clear():
    if platform() == 'Windows':
        system('cls')
    else:
        system('clear')


def checkList(li):
    # Status 0 Means TIE

    status = 0

    # Status 1 Means Game is On

    for item in li:
        if type(item) == int:
            status = 1

    # Status 2 Means We Have a Winner

    if li[0] == li[1] == li[2] or li[3] == li[4] == li[5] or li[6] == li[7] == li[8] or li[2] == li[4] == li[6] or li[0] == li[4] == li[8] or li[0] == li[3] == li[6] or li[1] == li[4] == li[7] or li[2] == li[5] == li[8]:
        status = 2

    return status


def gameBoard(player1Name, player2Name):
    clear()
    print(f"{player1Name}'s' Mark is X\n\n{player2Name}'s' Mark is O")
    print(" _______________________")
    print("|       |       |       |")
    print(
        f"|   {numberList[0]}   |   {numberList[1]}   |   {numberList[2]}   |")
    print("|_______|_______|_______|")
    print("|       |       |       |")
    print(
        f"|   {numberList[3]}   |   {numberList[4]}   |   {numberList[5]}   |")
    print("|_______|_______|_______|")
    print("|       |       |       |")
    print(
        f"|   {numberList[6]}   |   {numberList[7]}   |   {numberList[8]}   |")
    print("|_______|_______|_______|\n")


def playerChoice(playerName, mark):
    while True:
        try:
            playerChoice = int(input(f"{playerName}'s turn : "))
            break
        except:
            gameBoard(player1Name, player2Name)

    while True:
        if type(numberList[playerChoice-1]) != int:
            gameBoard(player1Name, player2Name)
            playerChoice = int(
                input('This Place is Already Taken !\n\nPlease Enter another Number : '))

        elif playerChoice not in range(1, 10):
            gameBoard(player1Name, player2Name)
            playerChoice = int(
                input('Please Enter a Number Beetwen 1 and 9 : '))
        else:
            break

    numberList[playerChoice-1] = mark


# Main Game Logic


clear()

print('Welcome To The TikTakToe Game !\n')

player1Name = input('Enter Player 1 Name : ')
player2Name = input('Enter Player 2 Name : ')

gameOn = True

while gameOn:

    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        clear()

        #################################

        roundOn = checkList(numberList)
        if roundOn == 0:
            gameBoard(player1Name, player2Name)
            print('Tie !\n\nWe dont Have a Winner :(')
            break

        elif roundOn == 2:
            gameBoard(player1Name, player2Name)
            print(f'{player2Name} Has Won The Game !')
            break
        else:
            pass

        gameBoard(player1Name, player2Name)

        playerChoice(player1Name, 'X')

        #################################

        roundOn = checkList(numberList)
        if roundOn == 0:
            gameBoard(player1Name, player2Name)
            print('Tie !\n\nWe dont Have a Winner :(')
            break

        elif roundOn == 2:
            gameBoard(player1Name, player2Name)
            print(f'{player1Name} Has Won The Game !')
            break
        else:
            pass

        gameBoard(player1Name, player2Name)

        playerChoice(player2Name, 'O')

    while True:

        game = input('\nWanna Play Again ? [y,n] ')

        if game.lower() == 'y':
            gameOn = True
            break

        elif game.lower() == 'n':
            print('Ok ! Goodbye :)')
            gameOn = False
            break
        else:
            print("Please Answer With 'y' or 'n'")
            clear()
