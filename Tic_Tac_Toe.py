from project import draw_board, check_turn, check_for_win
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("player " + str((turn % 2) + 1) + "st turn: pick your spot or press q to quit the game.")

    # get Input from the player
    choice = input()
    if choice == 'q':
        playing = False

    # check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:

        # check if the spot has already been taken
        if not spots[int(choice)] in {"x", "o"}:

            # valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    if check_for_win(spots): playing, complete = False, True
    if turn <= 8: playing = True

    # if there was a winner, say who win
    if complete:

        if check_turn(turn) == 'x':
            print("player 1 win!")
        else:
            print("player 2 win!")
        playing = False
    else:
        # tie game
        print("No Winner")

    print("Thank you for playing!")
    print("Enjoy your day!")
