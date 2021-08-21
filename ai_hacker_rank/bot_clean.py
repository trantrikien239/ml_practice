#!/usr/bin/python
# Head ends here

import functools

def cal_num_move(pos_dirt, pos_bot):
    return abs(pos_bot[0] - pos_dirt[0]) + abs(pos_bot[1] - pos_dirt[1])

def move(pos_dest, pos_bot):
    if pos_bot[0] - pos_dest[0] > 0:
        return 'UP'
    elif pos_bot[0] - pos_dest[0] < 0:
        return 'DOWN'
    elif pos_bot[1] - pos_dest[1] > 0:
        return 'LEFT'
    elif pos_bot[1] - pos_dest[1] < 0:
        return 'RIGHT'
    

def next_move(posr, posc, board):
    n = 5
    list_pos_dirt = [(x,y) for x in range(n) for y in range(n) if board[x][y] == 'd']
    cal_num_move_to_bot = functools.partial(cal_num_move, pos_bot=(posr, posc))
    closet_pos_dirt = min(list_pos_dirt, key=cal_num_move_to_bot)
    num_move = cal_num_move_to_bot(closet_pos_dirt)
    if num_move == 0:
        print('CLEAN')
        return 'CLEAN'
    else:
        print(move(closet_pos_dirt, pos_bot=(posr, posc)))
        return move(closet_pos_dirt, pos_bot=(posr, posc))



# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)