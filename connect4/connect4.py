class Board:
    def __init__(self, rows: int, colms: int) -> None:
        self.rows = rows
        self.colms = colms
        self.board = [[' ' for _ in range(colms)] for _ in range(rows)]
        
    def display(self) -> None:
        print("+" * ((3 * self.colms) +3))
        self.board = [['  ' for _ in range(self.colms)] for _ in range(self.row)]
        for row in self.board:
            print(("+ ")+('|').join(row)+(" +"))
            print("+" * ((3 * self.colms) +3))

    def place_marker(self):
        if self.board[]

























def main():
    board = board(3,3)

if __name__ == "__main__":
    main()