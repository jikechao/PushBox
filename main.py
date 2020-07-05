import pygame ,sys,random,time
import pygame.freetype

pygame.init()
size= width,height=35*9 ,35*9
speed =[1,1]
BLACK =0,0,0
screen =pygame.display.set_mode(size)
pygame.display.set_caption("PUSH BOX")

fps = 30000
fclock = pygame.time.Clock()

background1 = pygame.image.load("Level_1_background.jpg")
background2 = pygame.image.load("Level_2_background.jpg")
background3 = pygame.image.load("success.jpg")
backgroundrect1 = background1.get_rect()
backgroundrect2 = background2.get_rect()
backgroundrect3 = background3.get_rect()
wall=pygame.image.load("wall.jpg")
black=pygame.image.load("black.jpg")
grass=pygame.image.load("grass.jpg")
hole=pygame.image.load("hole.jpg")
box1 = pygame.image.load("box_1.png")
box2 = pygame.image.load("box_2.png")
box1_2 = pygame.image.load("box_1.png")
box2_2 = pygame.image.load("box_2.png")
box1_3 = pygame.image.load("box_1.png")
box2_3 = pygame.image.load("box_2.png")
box1_4 = pygame.image.load("box_1.png")
box2_4 = pygame.image.load("box_2.png")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(1)

spirite = range(4)
spirite[0]=pygame.image.load("up.png")
spirite[1]=pygame.image.load("down.png")
spirite[2]=pygame.image.load("left.png")
spirite[3]=pygame.image.load("right.png")
spirte_position=0

# init
spirite_position = spirite_width,spirite_height = 105,105
box_position = box_width,box_height = 105,105-35
box2_position = box2_width,box2_height = 105+35 , 105+35
box3_position = box3_width,box3_height = 105,105+35
box4_position = box4_width,box4_height = 105+35,105

end_position=range(4)
end_position[0] = 105 ,105-35*2
end_position[1] = 105+35 ,105+35*3
end_position[2] = 105-2*35 , 105+35
end_position[3] = 105+35*3 ,105

A=[([black] * 9) for i in range(9)]
for num in range(0, 8):
    for i in range(0, 8):
        A[num][i]=black

for x in range(0,9):
    for y in range(0, 9):
        if (x==0 and (y==2 or y==3 or y==4))\
                or(x==1 and (y==2 or y==4)) \
                or (x==2 and (y==2 or (y>=4 and y<=7)))\
                or(x==3 and (y<=2 or y==7))\
                or(x==4 and (y==0 or y==5 or y==6 or y==7))\
                or(x==5 and (y<=3 or y==5))\
                or(x==6 and (y==3 or y==5))\
                or(x==7 and (y>=3 and y<=5)):
            A[x][y]=wall
        elif (x==1 and y==3)\
                or(x==3 and y==6)\
                or(x==4 and y==1)\
                or(x==6 and y==4):
            A[x][y]=hole
        elif (x==2 and y==3)\
              or ( x==3 and (y>=3 and y<=5))\
              or(x==4 and (y>=2 and y<=4))\
                or(x==5 and y==4):
            A[x][y]=grass

def ShowBoxColor(flag2):
    for flag in end_position:
        if flag == (box_width, box_height):
            flag2[0] = 1
        elif flag == (box2_width, box2_height):
            flag2[1] = 1
        elif flag == (box3_width, box3_height):
            flag2[2] = 1
        elif flag == (box4_width, box4_height):
            flag2[3] = 1
    if flag2[0] == 1:
        screen.blit(box2, [box_width, box_height])
    else:
        screen.blit(box1, [box_width, box_height])
    if flag2[1] == 1:
        screen.blit(box2, [box2_width, box2_height])
    else:
        screen.blit(box1, [box2_width, box2_height])
    if flag2[2] == 1:
        screen.blit(box2, [box3_width, box3_height])
    else:
        screen.blit(box1, [box3_width, box3_height])
    if flag2[3] == 1:
        screen.blit(box2, [box4_width, box4_height])
    else:
        screen.blit(box1, [box4_width, box4_height])
    return
def ShowBoxColor2(flag2):
    for flag in end_position:
        if flag == (box_width, box_height):
            flag2[0] = 1
        elif flag == (box2_width, box2_height):
            flag2[1] = 1
        elif flag == (box3_width, box3_height):
            flag2[2] = 1
    if flag2[0] == 1:
        screen.blit(box2, [box_width, box_height])
    else:
        screen.blit(box1, [box_width, box_height])
    if flag2[1] == 1:
        screen.blit(box2, [box2_width, box2_height])
    else:
        screen.blit(box1, [box2_width, box2_height])
    if flag2[2] == 1:
        screen.blit(box2, [box3_width, box3_height])
    else:
        screen.blit(box1, [box3_width, box3_height])
    return
def Jieshu(jieshu):
    for i in flag2:
         if i == 0:
             jieshu = 0
    return jieshu
def Jieshu2():
    for flag in end_position:
        if flag == (box_width, box_height):
            flag2[0] = 1
        elif flag == (box2_width, box2_height):
            flag2[1] = 1
        elif flag == (box3_width, box3_height):
            flag2[2] = 1
    if flag2[0]+flag2[1]+flag2[2]==3:
        return True
    return False
def ShowSpiritDirection(spirite_position):
    if spirite_position==0:
      screen.blit( spirite[0], (spirite_width,spirite_height) )
    elif spirite_position==1:
        screen.blit(spirite[1],(spirite_width,spirite_height))
    elif spirite_position==2:
        screen.blit(spirite[2],(spirite_width,spirite_height))
    else:
        screen.blit(spirite[3],(spirite_width,spirite_height))
    return

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()

            if event.key==pygame.K_UP:
                spirite_position=0
              # print A[((spirite_width) / 35)][(spirite_height -35 ) / 35]
                if (spirite_height-35 ==box_height) & (spirite_width == box_width):
                    if A[(spirite_height-70)/35][(spirite_width)/35] == grass or A[(spirite_height-70)/35][(spirite_width)/35]==hole:
                        box_height -= 35
                        spirite_height -= 35
                elif (spirite_height-35 ==box2_height) & (spirite_width == box2_width):
                    if A[(spirite_height-70)/35][(spirite_width)/35] == grass or A[(spirite_height-70)/35][(spirite_width)/35]==hole:
                        box2_height -= 35
                        spirite_height -= 35
                elif (spirite_height-35 ==box3_height) & (spirite_width == box3_width):
                    if A[(spirite_height - 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height - 70) / 35][
                                (spirite_width) / 35] == hole:
                        box3_height -= 35
                        spirite_height -= 35
                elif (spirite_height - 35 == box4_height) & (spirite_width == box4_width):
                    if A[(spirite_height - 70) / 35][(spirite_width) / 35] == grass or \
                            A[(spirite_height - 70) / 35][(spirite_width) / 35] == hole:
                        box4_height -= 35
                        spirite_height -= 35
                # spirit move
                elif A[(spirite_height-35)/35][((spirite_width)/35)] == grass or A[(spirite_height-35)/35][((spirite_width)/35)] == hole :
                    spirite_height -= 35

            elif event.key==pygame.K_DOWN:
                spirite_position = 1
                if (spirite_height + 35 == box_height) & (spirite_width == box_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box_height += 35
                        spirite_height += 35
                elif (spirite_height + 35 == box2_height) & (spirite_width == box2_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box2_height += 35
                        spirite_height += 35
                elif (spirite_height + 35 == box3_height) & (spirite_width == box3_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box3_height += 35
                        spirite_height += 35
                elif (spirite_height + 35 == box4_height) & (spirite_width == box4_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or \
                                    A[(spirite_height + 70) / 35][(spirite_width) / 35] == hole:
                        box4_height += 35
                        spirite_height += 35
                # spirit move
                elif A[(spirite_height + 35) / 35][((spirite_width) / 35)] == grass or A[(spirite_height + 35) / 35][
                    ((spirite_width) / 35)] == hole:
                    spirite_height += 35

            elif event.key==pygame.K_LEFT:
                spirite_position=2
                if (spirite_height ==box_height) & ((spirite_width-35 )== box_width):
                    if A[(spirite_height)/35][(spirite_width-70)/35] == grass or A[(spirite_height)/35][(spirite_width-70)/35]==hole:
                        box_width -= 35
                        spirite_width -= 35
                elif (spirite_height ==box2_height) & (spirite_width-35 == box2_width):
                    if A[(spirite_height)/35][(spirite_width-70)/35] == grass or A[(spirite_height)/35][(spirite_width-70)/35]==hole:
                        box2_width -= 35
                        spirite_width -= 35
                elif (spirite_height ==box3_height) & (spirite_width-35 == box3_width):
                    if A[(spirite_height) / 35][(spirite_width-70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width-70) / 35] == hole:
                        box3_width -= 35
                        spirite_width -= 35
                elif (spirite_height == box4_height) & (spirite_width - 35 == box4_width):
                    if A[(spirite_height) / 35][(spirite_width - 70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width - 70) / 35] == hole:
                        box4_width -= 35
                        spirite_width -= 35
                # spirit move
                elif A[(spirite_height)/35][((spirite_width-35)/35)] == grass or A[(spirite_height)/35][((spirite_width-35)/35)] == hole :
                    spirite_width -= 35



            elif event.key==pygame.K_RIGHT:
                spirite_position=3
                if (spirite_height ==box_height) & ((spirite_width+35 )== box_width):
                    if A[(spirite_height)/35][(spirite_width+70)/35] == grass or A[(spirite_height)/35][(spirite_width+70)/35]==hole:
                        box_width += 35
                        spirite_width += 35
                elif (spirite_height ==box2_height) & (spirite_width+35 == box2_width):
                    if A[(spirite_height)/35][(spirite_width+70)/35] == grass or A[(spirite_height)/35][(spirite_width+70)/35]==hole:
                        box2_width += 35
                        spirite_width += 35
                elif (spirite_height ==box3_height) & (spirite_width+35 == box3_width):
                    if A[(spirite_height) / 35][(spirite_width+70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width+70) / 35] == hole:
                        box3_width += 35
                        spirite_width += 35
                elif (spirite_height == box4_height) & (spirite_width + 35 == box4_width):
                    if A[(spirite_height) / 35][(spirite_width + 70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width + 70) / 35] == hole:
                        box4_width += 35
                        spirite_width += 35
                # spirit move
                elif A[(spirite_height)/35][((spirite_width+35)/35)] == grass or A[(spirite_height)/35][((spirite_width+35)/35)] == hole :
                    spirite_width += 35
    screen.fill(BLACK)
    for num in range(0 , 9):
        for i in range(0 , 9):
            screen.blit(A[num][i], (i * 35, num * 35))
    ShowSpiritDirection(spirite_position)

    flag2 =[0,0,0,0]
    ShowBoxColor(flag2)
    pygame.display.update()
    fclock.tick(fps)

    jieshu=1
    if Jieshu(jieshu) == 1 :
        print "you have pass the level1,congratulation"
     #   pygame.mixer.music.stop()
        fclock.tick(fps)
        time.sleep(1)
        break
#########################################################Level_2#######################################################################
#########################################################Level_2#######################################################################

A=[([black] * 9) for i in range(9)]
for num in range(0, 8):
    for i in range(0, 8):
        A[num][i]=black

for x in range(0,9):
    for y in range(0, 9):
        if (x==0 and y<5)\
                or(x==1 and (y==0 or y==4)) \
                or(x==2 and (y == 0 or y == 4 or y==6 or y==7 or y==8)) \
                or(x==3 and (y == 0 or y == 4 or y == 6 or y == 8)) \
                or(x==4 and (y!=3 and y!=7))\
                or(x==5 and (y==1 or y==2 or y==8))\
                or(x==6 and (y==1 or y==5 or y==8))\
                or(x==7 and (y==1 or y==5 or y==6 or y==7 or y==8))\
                or(x==8 and (y>=1 and y<=5)):
            A[x][y]=wall
        elif (x>=3 and x<=5) and y==7:
            A[x][y]=hole
        elif (x>=1 and x<=3 and y>=1 and y<=3)\
                or(x==4 and y==3)\
                or(x==5 and (y>=3 and y<=6))\
                or(x==6 and (y>1 and y!=5 and y<=7))\
                or(x==7 and(y>1 and y<=4)):
            A[x][y]=grass

#init
spirite_position=spirite_width,spirite_height=35,35
box_position=box_width,box_height=35*2,35*2
box2_position=box2_width,box2_height=35*2,35*3
box3_position=box3_width,box3_height=35*3,35*2

end_position=range(3)
end_position[0] = 7*35 ,3*35
end_position[1] = 7*35 ,4*35
end_position[2] = 7*35 ,5*35

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()

            if event.key==pygame.K_UP:
                spirite_position=0
              # print A[((spirite_width) / 35)][(spirite_height -35 ) / 35]
                if (spirite_height-35 ==box_height) & (spirite_width == box_width):
                    if A[(spirite_height-70)/35][(spirite_width)/35] == grass or A[(spirite_height-70)/35][(spirite_width)/35]==hole:
                        box_height -= 35
                        spirite_height -= 35
                elif (spirite_height-35 ==box2_height) & (spirite_width == box2_width):
                    if A[(spirite_height-70)/35][(spirite_width)/35] == grass or A[(spirite_height-70)/35][(spirite_width)/35]==hole:
                        box2_height -= 35
                        spirite_height -= 35
                elif (spirite_height-35 ==box3_height) & (spirite_width == box3_width):
                    if A[(spirite_height - 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height - 70) / 35][
                                (spirite_width) / 35] == hole:
                        box3_height -= 35
                        spirite_height -= 35
                # spirit move
                elif A[(spirite_height-35)/35][((spirite_width)/35)] == grass or A[(spirite_height-35)/35][((spirite_width)/35)] == hole :
                    spirite_height -= 35

            elif event.key==pygame.K_DOWN:
                spirite_position = 1
                if (spirite_height + 35 == box_height) & (spirite_width == box_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box_height += 35
                        spirite_height += 35
                elif (spirite_height + 35 == box2_height) & (spirite_width == box2_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box2_height += 35
                        spirite_height += 35
                elif (spirite_height + 35 == box3_height) & (spirite_width == box3_width):
                    if A[(spirite_height + 70) / 35][(spirite_width) / 35] == grass or A[(spirite_height + 70) / 35][
                                (spirite_width) / 35] == hole:
                        box3_height += 35
                        spirite_height += 35
                # spirit move
                elif A[(spirite_height + 35) / 35][((spirite_width) / 35)] == grass or A[(spirite_height + 35) / 35][
                    ((spirite_width) / 35)] == hole:
                    spirite_height += 35

            elif event.key==pygame.K_LEFT:
                spirite_position=2
                if (spirite_height ==box_height) & ((spirite_width-35 )== box_width):
                    if A[(spirite_height)/35][(spirite_width-70)/35] == grass or A[(spirite_height)/35][(spirite_width-70)/35]==hole:
                        box_width -= 35
                        spirite_width -= 35
                elif (spirite_height ==box2_height) & (spirite_width-35 == box2_width):
                    if A[(spirite_height)/35][(spirite_width-70)/35] == grass or A[(spirite_height)/35][(spirite_width-70)/35]==hole:
                        box2_width -= 35
                        spirite_width -= 35
                elif (spirite_height ==box3_height) & (spirite_width-35 == box3_width):
                    if A[(spirite_height) / 35][(spirite_width-70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width-70) / 35] == hole:
                        box3_width -= 35
                        spirite_width -= 35
                # spirit move
                elif A[(spirite_height)/35][((spirite_width-35)/35)] == grass or A[(spirite_height)/35][((spirite_width-35)/35)] == hole :
                    spirite_width -= 35



            elif event.key==pygame.K_RIGHT:
                spirite_position=3
                if (spirite_height ==box_height) & ((spirite_width+35 )== box_width):
                    if A[(spirite_height)/35][(spirite_width+70)/35] == grass or A[(spirite_height)/35][(spirite_width+70)/35]==hole:
                        box_width += 35
                        spirite_width += 35
                elif (spirite_height ==box2_height) & (spirite_width+35 == box2_width):
                    if A[(spirite_height)/35][(spirite_width+70)/35] == grass or A[(spirite_height)/35][(spirite_width+70)/35]==hole:
                        box2_width += 35
                        spirite_width += 35
                elif (spirite_height ==box3_height) & (spirite_width+35 == box3_width):
                    if A[(spirite_height) / 35][(spirite_width+70) / 35] == grass or A[(spirite_height) / 35][
                                (spirite_width+70) / 35] == hole:
                        box3_width += 35
                        spirite_width += 35
                # spirit move
                elif A[(spirite_height)/35][((spirite_width+35)/35)] == grass or A[(spirite_height)/35][((spirite_width+35)/35)] == hole :
                    spirite_width += 35

    for num in range(0 , 9):
        for i in range(0 , 9):
            screen.blit(A[num][i], (i * 35, num * 35))
    ShowSpiritDirection(spirite_position)
    flag2 = [0, 0, 0, 0]
    ShowBoxColor2(flag2)
    pygame.display.update()

    if Jieshu2() == True:
        print "you have pass the level 2,congratulation"
        #pygame.mixer.music.stop()
        fclock.tick(fps)
        time.sleep(1)
        break
########################################success####################################################
########################################success####################################################

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                sys.exit()
    screen.fill(BLACK)
    screen.blit(background3, backgroundrect3)
    pygame.display.update()