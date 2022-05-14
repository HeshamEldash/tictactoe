class Board:

    def __init__(self):

        self.display_board = {
            "first_row": ["   ", "|", "   ", "|", "   "],
            "sec_row": ["   ", "|", "   ", "|", "   "],
            "third_row": ["   ", "|", "   ", "|", "   "]
        }
        self.logic_board = {
            "1": ["", "", ""],
            "2": ["", "", ""],
            "3": ["", "", ""]
        }
        self.o_locations = []
        self.x_locations = []
        self.wining_locations = [
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(3, 0), (3, 1), (3, 2)],
            [(1, 0), (2, 1), (3, 2)],
            [(1, 2), (2, 1), (3, 0)],
            [(1, 0), (2, 0), (3, 0)],
            [(1, 1), (2, 1), (3, 1)],
            [(1, 2), (2, 2), (3, 2)],
        ]

    def print_board(self):
        print("".join(self.display_board["first_row"]))
        print("-----------")
        print("".join(self.display_board["sec_row"]))
        print("-----------")
        print("".join(self.display_board["third_row"]))

    @staticmethod
    def get_row_num(row_number):
        if row_number == 1:
            return "first_row"
        if row_number == 2:
            return "sec_row"
        if row_number == 3:
            return "third_row"

    @staticmethod
    def get_column_num(column_number):
        if column_number == 1:
            return 0
        elif column_number == 2:
            return 2
        elif column_number == 3:
            return 4

    def fill_board(self, player_input, row_number, column_number):
        """ Takes a string input, an int row number and an int column number. If the slot is take, returns False"""
        if self.logic_board[str(row_number)][column_number - 1] == "":
            self.display_board[self.get_row_num(row_number)][
                self.get_column_num(column_number)] = " " + player_input + " "

            self.logic_board[str(row_number)][column_number - 1] = player_input
            return True
        else:
            print("This slot is already taken, play again!")
            return False

    def check_locations(self):
        """ Add the locations of O & X to their lists"""
        self.o_locations.clear()
        self.x_locations.clear()
        for key, value in self.logic_board.items():
            for count, slot in enumerate(value):

                if slot == "O":
                    o_location = (int(key), count)
                    self.o_locations.append(o_location)

                elif slot == "X":
                    x_location = (int(key), count)
                    self.x_locations.append(x_location)

    def check_winner(self):

        for item in self.wining_locations:
            wining_set = set(item)
            o_set = set(self.o_locations)
            x_set = set(self.x_locations)
            if wining_set.issubset(x_set):
                return "Player One Won"
            if wining_set.issubset(o_set):
                return "Player Two Won"
        return "no winner"


def check_input(player_input):
    try:
        int(player_input)
    except ValueError:
        print("you have not entered a valid number")
        return False
    else:
        if int(player_input) > 3:
            print("you have entered a number >3, Try again!")
            return False
        else:
            return True


def play():
    def play_again():
        to_play_again = input("do you want to play again? Y/N\n").lower()
        if to_play_again == "y":
            return play()
        else:
            print("Thanks for playing!")
            return False

    print("Time to play a Tic Tac Toe game!")
    board = Board()
    times_played = 0
    board.print_board()
    game_is_on = True
    while game_is_on:

        times_played += 1

        player_one_turn = True
        while player_one_turn:
            print("Player one turn 'x'")
            row = input("Select a row (1, 2 or 3)\n")
            while not check_input(row):
                row = input("Select a row (1, 2 or 3)\n")

            column = input("Select a column (1, 2 or 3)\n")
            while not check_input(column):
                column = input("Select a column (1, 2 or 3)\n")

            # fills the board, if the slot is already taken, the while loop will play again
            if not board.fill_board("X", int(row), int(column)):
                pass
            else:

                break

        board.print_board()
        board.check_locations()
        # check if player one won
        if board.check_winner() == "Player One Won":
            print("Player One Won")
            if play_again() == False:
                break
        # check if Draw
        print(times_played)
        if times_played == 5 and board.check_winner() == "no winner":
            print("It's a draw")
            if play_again() == False:
                break

        player_two_turn = True
        while player_two_turn:
            print("Player Two turn 'o'")
            row = input("Select a row (1, 2 or 3)\n")
            while not check_input(row):
                row = input("Select a row (1, 2 or 3)\n")

            column = input("Select a column (1, 2 or 3)\n")
            while not check_input(column):
                column = input("Select a column (1, 2 or 3)\n")

            # fills the board, if the slot is already taken, the while loop will play again
            if not board.fill_board("O", int(row), int(column)):
                pass
            else:
                break

        board.print_board()
        board.check_locations()

        # check if player two won
        if board.check_winner() == "Player Two Won":
            print("Player Two Won")
            game_is_on = False


play()
