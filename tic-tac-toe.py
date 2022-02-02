#This function is used to draw the board's current state every time the user turn arrives. 
def ConstBoard(board):
    print("Current State Of Board : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(board[i]==0):
            print("- ",end=" ");
        if (board[i]==1):
            print("O ",end=" ");
        if(board[i]==-1):    
            print("X ",end=" ");
    print("\n\n");

#This function takes the user move as input and make the required changes on the board.
def UserTurn(board):
    pos=input("Enter X's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0) ;
    board[pos-1]=-1;

#MinMax function.
def minimax(board,player):

    # Check for terminal states (base case)
    winner = check_for_winner(board);
    if(winner!=0): return (winner*player);

    # Initialize best value
    value=-2; # can be 1 or -1

    # Check for all possible moves and update best value and position
    for i in range(0,9):
        if(board[i]==0):
            # Make the move to current position 
            board[i]=player;

            # Call minimax recursively for alternate player
            score=-minimax(board,(player*-1));

            # Update best value 
            if(score>value): value=score;

            # Reset the current cell
            board[i]=0;

    # Return best value 
    if(value==-2): return 0;
    return value;
    
#This function makes the computer's move using minmax algorithm.
def CompTurn(board):
    pos=-1;
    value=-2; # can be 1 or -1
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
    board[pos]=1;


#This function is used to analyze a game.
def check_for_winner(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]];
    return 0;

if __name__ == "__main__":
    #Initializing the board.
    board=[0,0,0,0,0,0,0,0,0];

    # This loop is used to play the game.
    print("Computer : O Vs. You : X");
    for i in range (0,9):
        if(check_for_winner(board)!=0):
            break;
        if(i%2==0):
            CompTurn(board);
        else:
            ConstBoard(board);
            UserTurn(board);

    # output the result
    winner = check_for_winner(board);
    ConstBoard(board);
    if(winner==0): print("Draw!!!")
    if(winner==-1): print("You Win !!!")
    if(winner==1): print("Computer Wins !!!!")
