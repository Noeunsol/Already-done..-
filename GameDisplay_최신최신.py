import pygame 
import random
import mine_sweeper as ms
import tkinter as tk
from tkinter import messagebox


pygame.init()

screen_size = [450,450] 
width = 40
height = 40
cube = 9
white = (255,255,255)
black = (0,0,0)
gray = (178,190,181)
done = False
done2 = False
bomb_cnt = 0

p1 = pygame.image.load('p1.png')
p1 = pygame.transform.scale(p1, (320, 250))

p2 = pygame.image.load('p2.png')
p2 = pygame.transform.scale(p2, (320, 250))

p3 = pygame.image.load('p3.png')
p3 = pygame.transform.scale(p3, (320, 250))

p4 = pygame.image.load('p4.png')
p4 = pygame.transform.scale(p4, (320, 250))

p5 = pygame.image.load('p5.png')
p5 = pygame.transform.scale(p5, (320, 250))

p6 = pygame.image.load('p6.png')
p6 = pygame.transform.scale(p6, (320, 250))

p7 = pygame.image.load('p7.png')
p7 = pygame.transform.scale(p7, (320, 250))

p8 = pygame.image.load('p8.png')
p8 = pygame.transform.scale(p8, (320, 250))

p9 = pygame.image.load('p9.png')
p9 = pygame.transform.scale(p9, (320, 250))

problem_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
problem_correct = [1, 2, 3, 4, 5, 1, 2, 3, 4]


clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode(screen_size)
pygame.display.set_caption(" 지뢰찾기 ")

flag = pygame.image.load('flag.png')
flag = pygame.transform.scale(flag, (width, height))

bomb = pygame.image.load('Bomb.png')
bomb = pygame.transform.scale(bomb, (width, height))

one = pygame.image.load('1.png')
one = pygame.transform.scale(one, (width, height))

two = pygame.image.load('2.png')
two = pygame.transform.scale(two, (width, height))

thr = pygame.image.load('3.png')
thr = pygame.transform.scale(thr, (width, height))

fou = pygame.image.load('4.png')
fou = pygame.transform.scale(fou, (width, height))

fiv = pygame.image.load('5.png')
fiv = pygame.transform.scale(fiv, (width, height))

six = pygame.image.load('6.png')
six = pygame.transform.scale(six, (width, height))

sev = pygame.image.load('7.png')
sev = pygame.transform.scale(sev, (width, height))

eig = pygame.image.load('8.png')
eig = pygame.transform.scale(eig, (width, height))

cell, mine_index = ms.make_board()

def sep_num(x, y): #숫자 구별
    if cell[x][y] == 1:
        return one
    elif cell[x][y] == 2:
        return two
    elif cell[x][y] == 3:
        return thr
    elif cell[x][y] == 4:
        return fou
    elif cell[x][y] == 5:
        return fiv
    elif cell[x][y] == 6:
        return six
    elif cell[x][y] == 7:
        return sev
    elif cell[x][y] == 8:
        return eig
    elif cell[x][y] == 9:
        return bomb
    else:
        isitempty(x,y)
        return flag

    
def rumsec():
    pro_num = random.randrange(0, 9)
    print(pro_num)
    runGame(pro_num)
    
    pygame.quit()


def isitempty(row,col):
    if cell[row][col] == 0:#그 칸이 비어있는 경우
        empty=True
    else:#칸이 채워진 경우
        empty=False
    return empty

moveX = [-1,0,1,-1,1,-1,0,1]
moveY = [-1,-1,-1,0,0,1,1,1]

def removeEmptyCellSquare(y,x):
    grid[y][x] = 3 #검사 이미 완료 
    if not isitempty(y,x):
        return
    print("y : ", y, ", x : ", x)


    for i in range(0, len(moveX)):
        if 0<=y+moveY[i]<9 and 0<=x+moveX[i]<9 and grid[y+moveY[i]][x+moveX[i]]==0:
            removeEmptyCellSquare(y+moveY[i], x+moveX[i])

def letitgo(row,col,empty):
    global bomb_cnt
    global done2
    if cell[row][col] == 9:
        bomb_cnt += 1
        if(bomb_cnt < 10):
            # color = gray #그 칸만 보여주기
            # gameDisplay.blit(sep_num(row, col),[40*col+9*(col+1),40*row+9*(row+1)])#해당 칸만 보여주는 코드 작성
            grid[row][col] = 3
            done2 = False
            pro_num = random.randrange(0, 9)
            print(pro_num)
            runGame(pro_num)
    elif empty==False: #칸에 숫자가 채워져있는 경우
        color = gray #그 칸만 보여주기
        gameDisplay.blit(sep_num(row, col),[40*col+9*(col+1),40*row+9*(row+1)])#해당 칸만 보여주는 코드 작성
    else:#칸이 비어있는 경우 주변 8칸 검사후 빈칸의 경우 재귀로 돌리기
        color = gray #그 칸만 보여주기
        removeEmptyCellSquare(row, col)


grid = []
for row in range(9):
    grid.append([])
    for _ in range(9):
        grid[row].append(0) 

gameDisplay.fill(black)


game_end = "Your score is F"

pygame.display.set_caption(" 끝난줄 알았지..? ")
game_font = pygame.font.Font(None, 40)



 # 게임 오버 메시지
msg = game_font.render(game_end, True, black)
msg_rect = msg.get_rect(center=(100, 100))


def message_box(subject, content):
    pygame.time.delay(500)
    messagebox.showinfo(subject, content)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def endGame():
    #message_box("gameover","Yore Score is F")
    done = True
    done2 = True



class button:  # 버튼 생성
    def __init__(self, x, y, width, height, color, buttonText='Button', action=None, done=False):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표
        click = pygame.mouse.get_pressed()  # 클릭여부
        #print(click)
        
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            if click[0] == 1 and action != None:
                pygame.time.delay(500)
                action()
        else:
            pygame.draw.rect(gameDisplay, color, (x,y,width,height))

        smallText = pygame.font.SysFont('arial', 20)
        textSurf, textRect = text_objects(buttonText, smallText)
        textRect.center = ((x+(width/2)), (y+(height/2)))
        gameDisplay.blit(textSurf, textRect)

def CountinueGame():
    message_box("Clear", "정답입니다!")
    endGame()


def runGame(pro_num):
    global done2, bomb
    x = 100
    y = 200
    start_ticks = pygame.time.get_ticks() 
    while not done2:
        
        clock.tick(20)
        gameDisplay.fill(white)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        gameDisplay.blit(bomb, (x, y))

        #버튼 생성할 때 문제 같이 띄워주고 문제에 따라 버튼의 action을 다르게 할 것.


        gameDisplay.blit(problem_list[pro_num], (50, 70))

        
        button(75, 325, 100, 50, gray, "yeonju", endGame, True)
        button(175, 325, 100, 50, gray, "subin", endGame, True)
        button(275, 325, 100, 50, gray, "eunsol", endGame, True)
        button(125, 375, 100, 50, gray, "yeonghee", endGame, True)
        button(225, 375, 100, 50, gray, "cheolsu", endGame, True)

        if (problem_correct[pro_num] == 1):
            button(75, 325, 100, 50, gray, "yeonju", CountinueGame, False)
        elif(problem_correct[pro_num] == 2):
            button(175, 325, 100, 50, gray, "subin", CountinueGame, False)
        elif(problem_correct[pro_num] == 3):
            button(275, 325, 100, 50, gray, "eunsol", CountinueGame, False)
        elif(problem_correct[pro_num] == 4):
            button(125, 375, 100, 50, gray, "yeonghee", CountinueGame, False)
        else:
            button(225, 375, 100, 50, gray, "cheolsu", CountinueGame, False)
        
        
        total_time = 10

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
        timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, black)
        gameDisplay.blit(timer, (175, 30))

        # 시간 초과했다면
        if total_time - elapsed_time <= 0:
            game_end = "Time Over"
            gameDisplay.blit(msg, msg_rect)
            pygame.display.update()
            # 2초 대기
            pygame.time.delay(2000)
            endGame()
            done2 = True

        pygame.display.update()


def runBomb():
    global done 
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                col = mouse[0] // (width + cube)
                row = mouse[1] // (height + cube)
                if event.button == 1:
                    if (grid[row][col] == 0):
                        grid[row][col] = 1
                    
                elif event.button == 3:
                    k = 0
                    for k in range(0, 9):
                        print(mine_index[k])
                    print(row)
                    print(col)

                    if (grid[row][col] == 2):
                        grid[row][col] = 0
                    else:
                        grid[row][col] = 2
                        
                        
        gameDisplay.fill(black)
        for row in range(9):
            for col in range(9):
                color = white
                pygame.draw.rect(gameDisplay,
                                color,
                                [(cube + width) * col + cube,
                                (cube + height) * row + cube,
                                width,
                                height])
                if grid[row][col] == 1: #mousebuttondown
                    letitgo(row,col,isitempty(row,col))
                if grid[row][col] == 2: #right mousebuttondown
                    color = gray
                    gameDisplay.blit(flag,[40*col+9*(col+1),40*row+9*(row+1)])
                if grid[row][col] == 3: #재귀로 확인을 거친 아이
                    if cell[row][col] == 0:
                        color = gray
                        pygame.draw.rect(gameDisplay,
                                        color,
                                        [(cube + width) * col + cube,
                                        (cube + height) * row + cube,
                                        width,
                                        height])
                    else:

                        gameDisplay.blit(sep_num(row,col), [40 * col + 9 * (col + 1), 40 * row + 9 * (row + 1)])
                        
        clock.tick(50)
        pygame.display.flip()
runBomb()
pygame.quit()

