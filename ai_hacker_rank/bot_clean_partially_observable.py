#!/usr/bin/python3

import functools
from random import choice


list_pos_dirt = []

def cal_num_move(pos_dirt, pos_bot):
    return abs(pos_bot[0] - pos_dirt[0]) + abs(pos_bot[1] - pos_dirt[1])

def move(pos_dest, pos_bot):
    if pos_bot[1] - pos_dest[1] > 0:
        return 'LEFT'
    elif pos_bot[1] - pos_dest[1] < 0:
        return 'RIGHT'
    elif pos_bot[0] - pos_dest[0] > 0:
        return 'UP'
    elif pos_bot[0] - pos_dest[0] < 0:
        return 'DOWN'
    else:
        return 'CLEAN'


def next_move(posx, posy, board):
    dimx = dimy = 5
    scout_plan = {
        (1,1):(2,1),
        (2,1):(3,1),
        (3,1):(3,2),
        (3,2):(3,3),
        (3,3):(2,3),
        (2,3):(1,3),
        (1,3):(1,2),
        (1,2):(1,1),
        (2,2):(4,0)
    }
    corner_pos = [(0,0), (0,4), (4,0), (4,4)]

    pos_bot=(posx, posy)
    list_pos_dirt_map = [(x,y) for x in [0,4,1,3,2] for y in [0,4,1,3,2] if board[x][y] == 'd']
    # list_pos_dirt = list(set(list_pos_dirt + list_pos_dirt_map))
    list_pos_dirt = list_pos_dirt_map
    list_corner_dirt = [pos for pos in list_pos_dirt if pos in corner_pos]
    list_pos_unk = [(x,y) for x in range(dimx) for y in range(dimy) if board[x][y] == 'o']
    if len(list_pos_dirt) == 0:
        if pos_bot not in scout_plan:                
            print(move((2,2), pos_bot=pos_bot))
        else:
            print(move(scout_plan[pos_bot], pos_bot=pos_bot))
    elif len(list_corner_dirt) > 0:
        print(move(list_corner_dirt[0], pos_bot=pos_bot))
    else:
        cal_num_move_to_bot = functools.partial(cal_num_move, pos_bot=pos_bot)
        closet_pos_dirt = min(list_pos_dirt, key=cal_num_move_to_bot)
        num_move = cal_num_move_to_bot(closet_pos_dirt)
        if num_move == 0:
            print('CLEAN')
        else:
            print(move(closet_pos_dirt, pos_bot=pos_bot))

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)