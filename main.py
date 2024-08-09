#지금 부터 Tic Tac Toe 게임을 만들겠습니다. 

board = [' ' for _ in range(9)] # 보드를 일렬로 표현
#보드를 출력하는 함수
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row)+ ' |')

def player_move(board, player):
    move = int(input(f'Player {player}, choose your move (1 - 9): ')) - 1
    if board[move== ' ']:
        board[move] = player
    else:
        print("잘 못 선택 했습니다. 다시 선택해세요")
        player_move(board, player)

def check_winner(board, player):
        win_conditions = [(0,1,2),(3,4,5),(6,7,8), # 가로 승리
                        (0,3,6),(1,4,7),(2,5,8),    #세로 승리
                        (0,4,8),(2,4,6)]        #대각선승리
        for condition in win_conditions:
                if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                     return True
        return False

def tic_tac_toe():
    board = [' 'for _ in range(9)]
    current_player = 'X'

    for _ in range(9):
        print_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
               print_board(board)
               print(f'Player {current_player} wins!')
               return
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print("It's a tie")

if __name__ == "__main__":
     tic_tac_toe()

