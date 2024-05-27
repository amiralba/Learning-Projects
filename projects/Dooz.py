#Board

class Board:
    def __init__(self):
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
           print(" | ".join(row))
        print("\n")


    def place_marker(self, row, col, marker):
        if self.board[row][col] == '_':
            self.board[row][col] = marker
            return True
        else:
            print("Cell already taken, Try Again.")
        return False    

    def check_winner(self, marker):
        #rows
        for row in self.board:
            if all(cell==marker for cell in row):
                return True
        #col
        for col in range(3):
            if all(self.board[row][col]==marker for row in range(3)):
                return True
        #zabdari
        if all(self.board[i][i] == marker for i in range(3)):
            return True
        if all(self.board[i][2-i] for i in range(3)):
            return True
        return False
    
    def is_full(self):
        return all(cell != '_' for row in self.board for cell in row)



#PLAYERS

class Player:
    def __init__(self,name, symbol):
        self.name = name
        self.symbol = symbol

def main():
    board = Board()

    #get players name
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")

    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")        
    players= [player1, player2]
    current_player_index = 0

    board.print_board()


    while True:
        current_player = players[current_player_index]
        print(f"{current_player.name}'s turn.")

        while True:
            try:
                row = int(input("Enter row (0, 1 , 2): "))
                col = int(input("Enter col (0, 1, 2): "))
                if 0 <= row <= 2 and 0<= col <= 2:
                    if board.place_marker(row, col, current_player.symbol):
                        break
                    else:
                        continue
                else:
                    print("Invalid input. Enter a number between 0 to 2")
            except ValueError:
                print("Invalid input. Enter a number between 0 to 2")

        board.print_board()

        if board.check_winner(current_player.symbol):
            print(f"{current_player.name} wins!")
            break
        if board.is_full():
            print("It's draw!")
            break 

        #switch turns

        current_player_index = (current_player_index + 1) % 2


if __name__ == "__main__":
    main()