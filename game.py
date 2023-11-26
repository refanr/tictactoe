from tictactoe import tictactoe
   
    
def play():
    t = tictactoe()
    t.splash()
    while True:
        
        t.print_board()

        while t.game_over != True:
            t.get_move()
        
        t.get_stats()
        
        again = input("\nWould you like to play again(y/n)? ")
        if again == "n":
            break
        t.start_again()

if __name__ == "__main__":
    
    play()