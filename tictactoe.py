import os

class tictactoe:
    
    def __init__(self) -> None:
        self.p1_turn = True
        self.game_state = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
        self.game_over = False
        self.game_history = [0,0,0]
    
    def start_again(self) -> None:
        """ Reset the game state to play again
        """
        self.p1_turn = True
        self.game_state = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
        self.game_over = False
        self.print_board()
        self.get_move()
        
    
    def clean_screen(self) -> None:
        """ Check Operating System and perform clear screen """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def print_board(self) -> None:
        """ Clear screen, then print out a representation of the game board with the current game state
        """
        self.clean_screen()
        print("-"*13)
        for y in self.game_state:
            print("|",end="")
            for x in y:
                print(" " + x + " |",end="")
            print()
            print("-"*13)
    
    def place_symbol(self,coord,symbol) -> None:
        """ Given the x,y coordinates and the symbol of the current player, place the symbol

        Args:
            coord ( int tuple): x and y coordinates
            symbol ( str ): "X" or "Y"
        """
        self.game_state[coord[0]][coord[1]] = symbol
        
        if self.check_win(symbol):
            print(symbol, "wins!\n")
            
        if not self.game_over:
            self.print_board()
        self.p1_turn = not self.p1_turn
        
    def check_win(self,symbol) -> bool:
        """ Check whether current player, represented by their symbol, has won

        Args:
            symbol ( str ): "X" or "Y"

        Returns:
            bool: Win state achieved or not
        """
        
        if symbol == "X":
            index = 1
        else:
            index = 2
            
        for y in self.game_state:
            if y == [symbol,symbol,symbol]:
                self.game_history[index] += 1
                self.game_over = True
                return True
        for i in range(3):
            if self.game_state[0][i] == symbol and self.game_state[1][i] == symbol and self.game_state[2][i] == symbol: 
                self.game_history[index] += 1
                self.game_over = True
                return True
            
        if self.game_state[0][0] == symbol and self.game_state[1][1] == symbol and self.game_state[2][2] == symbol: 
            self.game_history[index] += 1
            self.game_over = True
            return True
        
        if self.game_state[0][2] == symbol and self.game_state[1][1] == symbol and self.game_state[2][0] == symbol: 
            self.game_history[index] += 1
            self.game_over = True
            return True
        
        if self.check_draw():
            self.game_history[0] += 1
            self.game_over = True
            print("Draw\n")
        return False
    
    def get_stats(self) -> None:
        """ Print game history
        """
        print("Games played: " + str(sum(self.game_history)) + "\nX wins: " + str(self.game_history[1]) + "\nO wins: " + str(self.game_history[2]) + "\nDraws: " + str(self.game_history[0]))
            
    def get_coord(self,cell:str) -> tuple:
        """ Transform cell number in UI representation to x,y coordinates

        Args:
            cell ( str ): Number as string, representing cell number

        Returns:
            tuple: x,y coordinates for actual game state 
        """
        if cell == "1":
            return (0,0)
        elif cell == "2":
            return (0,1)
        elif cell == "3":
            return (0,2)
        elif cell == "4":
            return (1,0)
        elif cell == "5":
            return (1,1)
        elif cell == "6":
            return (1,2)
        elif cell == "7":
            return (2,0)
        elif cell == "8":
            return (2,1)
        elif cell == "9":
            return (2,2)
        else:
            print("Numbers 1-9 only please")
            return(3,3)
            
            
    def get_move(self) -> None:
        """ Getting input from user and placing the appropriate symbol in game state
        """
        symbol = "X"
        if self.p1_turn:
            print("X's turn")
        else:
            symbol = "O"
            print("O's turn")
        str_coord = input("Please enter cell number to place symbol: ")
        
        if str_coord.isnumeric():
            coord = self.get_coord(str_coord)
        else:
            print("Numbers only please")
            self.get_move()
            
        if coord[0] != 3 and self.check_legal(self.game_state[coord[0]][coord[1]]):
            self.place_symbol(coord,symbol)
        else:
            print("Illegal move bud")
            self.get_move()
        
    def check_legal(self,cell:str) -> bool:
        """ Check legality of the move

        Args:
            cell ( str ): Content of a single cell in the game state

        Returns:
            bool: returns False if the cell content is a symbol and not numeric
        """
        if cell.isnumeric():
            return True
        else: 
            return False
    
    def check_draw(self) -> bool:
        """ Checks if a draw state has been reached, no available legal cell

        Returns:
            bool: returns False if no legal move is possible
        """
        for row in self.game_state:
            for cell in row:
                if self.check_legal(cell):
                    return False
        return True
    
    def splash(self) -> None:
        """ Splash or Welcome screen with simple instructions
        """
        self.clean_screen()
        print("                        Welcome to Tic Tac Toe")
        print("\nX and O take turns placing their symbol to a cell until one player wins.")
        print("The Game board is represented like this:")
        print()
        print("-"*13)
        for y in self.game_state:
            print("|",end="")
            for x in y:
                print(" " + x + " |",end="")
            print()
            print("-"*13)
        print("\nSimply enter the cell number to place your symbol there.")
        print("As i usually the case, X always starts, have fun.")
        print()
        input("Press ANY key to begin")
                

    