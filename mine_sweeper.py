import pygame
import random


#주변에 숫자를 추가할 수 있는지 체크&더하는 함수.
def check_round(a, b, cell):
    if (a >= 0 and a <= 8 and b >= 0 and b <= 8):
        if (cell[a][b] != 9):
            cell[a][b] += 1
    

#지뢰의 인덱스와 cell 배열을 인수로 받고, 지뢰 기준 주변 8칸의 숫자를 더해주는 함수.
def add_number(cell, mine_count, mine_index):
    #리스트 모두 2차원 배열.
    j = 0
    for j in range(0, mine_count):
        x = mine_index[j][0]
        y = mine_index[j][1]
        print(j, x, y)
        try:
            check_round(x-1, y-1, cell)
            check_round(x, y-1, cell)
            check_round(x+1, y-1, cell)
            check_round(x-1, y, cell)
            check_round(x+1, y, cell)
            check_round(x-1, y+1, cell)
            check_round(x, y+1, cell)
            check_round(x+1, y+1, cell)
            
            #각...
        except:
            print('index out of range')
            print(x, y)

def make_board():
    #9x9 크기의 지뢰찾기판 정보를 저장하는 2차원 배열 생성
    cell =  [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #지뢰의 수
    mine_count = 9

    #지뢰의 인덱스를 저장할 배열
    mine_index = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    #중복된 지뢰 값 뽑기 방지
    mine_exist = False

    i = 0
    
    while (i < mine_count):
        mine_exist = False
        
        x = random.randrange(0, 9)
        y = random.randrange(0, 9)

        mine_index[i] = [x, y]

        if (i == 0):
            i += 1
            cell[x][y] = 9

        else:
            for j in range(0, i):
                if (mine_index[i] == mine_index[j]):
                    mine_exist = True
                    print("this index of mine already exist!")
                    print(mine_index[j], mine_index[i])

            if (mine_exist == False):
                i += 1
                cell[x][y] = 9
    print(mine_index)
    add_number(cell,mine_count, mine_index)
    k = 0
    for k in range(0, 9):
        print(cell[k])

    return cell, mine_index