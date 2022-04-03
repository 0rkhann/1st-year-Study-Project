import pygame
from pygame.locals import *
import random
from easygui import *
import time
from datetime import datetime
import sys
import os

path=os.path.abspath("Menu.jpg")
path_new=""
for i in range(len(path)): #Getting path of the folder
    if path[i+1]=="M":
        break
    path_new=path_new + path[i] 

sys.setrecursionlimit(5000)

pygame.init()

sounds=True #For mute sound button
sound_on_or_off=[pygame.image.load("Sound_on.png"), pygame.image.load("mute.png")]
clicked=False #For button(Toose a dice)
clicked_once=False #For avoiding a user spaming on a button
clicked_button_2=False #For showing other button related to showing cards of players
List_of_cells=[0, 0, 0, 0] #At which cell the player is located
number="" #A random number from a dice
color1, color2, color3, color4=(235,92,92), (220,220,220), (220,220,220), (220,220,220)
turn_of_player_color_change=1
number_of_players=0

n_event,choose_chem,choose_physics,choose_math,choose_alg,n_question_ge_or, n_question_ge_gr, n_event_outlook, n_question_pl_gr, n_question_pl_ye,n_question_en_ye, n_question_en_or, n_question_fr_re, n_question_al_re, n_question_ch_gr, n_question_ch_or, n_question_ph_ye, n_question_ph_re, n_question_ma_ye,n_question_ma_re, n_question_fr_gr, n_question_fr_ye, n_question_cs_gr, n_question_gq_re, n_question_al_or,n_question_cs_or =1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
List_of_chose_players=[] #Skins of players

#list of coordinates on the screen for each player
coordinates_for_players=[

                        [
                              [820,801], [690,830], [590,830], [490,830], [390,830], [290,830], [185,830],
                              [85, 850], [85, 680], [85, 580], [85 ,480], [85, 370], [85, 270], [85, 170],
                              [130 ,  0], [185,  0], [290,  0], [390,  0], [490,  0], [590,  0], [690,  0],
                              [870, 71], [830,170], [830,270], [830,370], [830,481], [830,581], [830,680]
                        ],

                        [
                              [831,880], [740,880], [641,880], [530,880], [430,880], [330,880], [230,880],
                              [10 ,800], [0 , 680], [0,  580], [0,  480], [0,  370], [0,  270], [0,  170],
                              [80,   0], [230,  0], [330,  0], [430,  0], [531,  0], [641,  0], [740,  0],
                              [910, 70], [920,170], [920,270], [920,370], [920,480], [920,580], [920,680]
                        ],

                        [
                              [880,880], [690,880], [590,880], [490,880], [390,880], [290,880], [190,880],
                              [25 ,820], [26 ,720], [25 ,620], [25, 510], [25, 410], [25, 310], [25, 210],
                              [80, 55],  [190, 55], [290, 55], [390, 55], [490, 55], [590, 56], [690, 55],
                              [870, 70], [860,205], [860,305], [860,405], [860,505], [860,615], [860,715]
                        ],

                        [
                              [880,800], [741,830], [641,830], [530,830], [430,830], [330,830], [230,830],
                              [60 ,820], [60 ,720], [61, 620], [60, 510], [60, 410], [61, 310], [61, 200],
                              [130, 55],  [230, 55], [330, 55], [430, 55], [531, 55], [640, 55], [740, 55],
                              [910, 71], [900,205], [900,305], [900,405], [900,505], [900,615], [900,715]
                        ]
]


List_of_current_coordinates=[ [820, 800], [831, 880], [880, 880], [880, 800] ]
List_of_average_points=[13.0, 13.0, 13.0, 13.0] 
List_of_scholarships=[130,130,130,130] 
List_of_NAMES=[] #Names of players


# lists for cards and list of their prices with correcsponding coordinate
List_of_bought_cards_by_players=[ [], [], [], [] ]
List_of_bought_cards_by_players_string_and_position=[ [ [], [] ], [ [], [] ], [ [], [] ], [ [], [] ] ]
Everything_related_to_cards=[ [1,None,None,None,0,"Begining","Begining",0], [0,0,0,"Without upgrade",0.5,"Chem_green",pygame.image.load("Chem_green.jpg"),1], [0,0,0,"Without upgrade",0.5,"CS_green",pygame.image.load("CS_green.jpg"),2], [0,0,0,"Without upgrade",0.5,"Plagiarism_green",pygame.image.load("Plagiarism_green.jpg"),3], [1,None,None,None,0,"Outlook","Outlook",4], [0,0,0,"Without upgrade",0.5,"Geometry_green",pygame.image.load("Geometry_green.jpg"),5] , [0,0,0,"Without upgrade",0.5,"French_green",pygame.image.load("French_green.jpg"),6], [1,None,None,None,0,"Canteen","Canteen",7], [1,None,None,None,0,"QM","QM",8], [0,0,0,"Without upgrade",0.75,"English_yellow",pygame.image.load("English_yellow.jpg"),9], [0,0,0,"Without upgrade",0.75,"MA_yellow",pygame.image.load("MA_yellow.jpg"),10], [0,0,0,"Without upgrade",0.75,"Physics_yellow",pygame.image.load("Physics_yellow.jpg"),11], [0,0,0,"Without upgrade",0.75,"French_yellow",pygame.image.load("French_yellow.jpg"),12], [0,0,0,"Without upgrade",0.75,"Plagiarism_yellow",pygame.image.load("Plagiarism_yellow.jpg"),13], [1,None,None,None,0,"Choose sub","Choose sub",14], [0,0,0,"Without upgrade",1,"Algebra_orange",pygame.image.load("Algebra_orange.jpg"),15], [1,None,None,None,0,"Outlook","Outlook",16], [0,0,0,"Without upgrade",1,"CS_orange",pygame.image.load("CS_orange.jpg"),17], [0,0,0,"Without upgrade",1,"Chem_orange",pygame.image.load("Chem_orange.jpg"),18], [0,0,0,"Without upgrade",1,"English_orange",pygame.image.load("English_orange.jpg"),19], [0,0,0,"Without upgrade",1,"Geometry_orange",pygame.image.load("Geometry_orange.jpg"),20], [1,None,None,None,0,"Rest day","Rest day",21], [0,0,0,"Without upgrade",1.5,"GQ_red",pygame.image.load("GQ_red.jpg"),22], [0,0,0,"Without upgrade",1.5,"MA_red",pygame.image.load("MA_red.jpg"),23], [1,None,None,None,0,"QM","QM",24], [0,0,0,"Without upgrade",1.5,"French_red",pygame.image.load("French_red.jpg"),25], [0,0,0,"Without upgrade",1.5,"Algebra_red",pygame.image.load("Algebra_red.jpg"),26], [0,0,0,"Without upgrade",1.5,"Physics_red",pygame.image.load("Physics_red.jpg"),27] ]
#First element= bought/ not bought, Second element= 1 Upgrade bought/ not bought, Third element=2 Upgrade bought/ not bought, Fourth elemt= how many points the cell subtract from or add to average points, Fiveth= the name of the cell, Sixth= the image of the cell
Dict_of_prices={1520:"50", 1420:"50", 1320:"50", 1120:"50", 1015:"50", 665:"65", 565:"65", 455:"65", 355:"65", 255:"65", 185:"80", 390:"80", 490:"80", 590:"80", 690:"80", 1000:"100", 1100:"100", 1311:"100", 1411:"100", 1510:"100",     1620:"50", 1521:"50", 1410:"50", 1210:"50", 1110:"50", 580:"65", 480:"65", 370:"65", 270:"65", 170:"65", 230:"80", 430:"80", 531:"80", 641:"80", 740:"80", 1090:"100", 1190:"100", 1400:"100", 1500:"100", 1600:"100",     1570:"50", 1470:"50", 1370:"50", 1170:"50", 1070:"50", 746:"65", 645:"65", 535:"65", 435:"65", 335:"65", 135:"80", 345:"80", 445:"80", 545:"80", 646:"80", 1065:"100", 1165:"100", 1365:"100", 1475:"100", 1575:"100",     1571:"50", 1471:"50", 1360:"50", 1160:"50", 1060:"50", 681:"65", 570:"65", 470:"65", 371:"65", 261:"65", 285:"80", 485:"80", 586:"80", 695:"80", 795:"80", 1105:"100", 1205:"100", 1405:"100", 1515:"100", 1615:"100"}
#red=100, orange=80, yellow=65, green=50
Dict_of_prices_for_first_uprading={1520:"70", 1420:"70", 1320:"70", 1120:"70", 1015:"70", 665:"85", 565:"85", 455:"85", 355:"85", 255:"85", 185:"100", 390:"100", 490:"100", 590:"100", 690:"100", 1000:"120", 1100:"120", 1311:"120", 1411:"120", 1510:"120",     1620:"70", 1521:"70", 1410:"70", 1210:"70", 1110:"70", 580:"85", 480:"85", 370:"85", 270:"85", 170:"85", 230:"100", 430:"100", 531:"100", 641:"100", 740:"100", 1090:"120", 1190:"120", 1400:"120", 1500:"120", 1600:"120",     1570:"70", 1470:"70", 1370:"70", 1170:"70", 1070:"70", 746:"85", 645:"85", 535:"85", 435:"85", 335:"85", 135:"100", 345:"100", 445:"100", 545:"100", 646:"100", 1065:"120", 1165:"120", 1365:"120", 1475:"120", 1575:"120",     1571:"70", 1471:"70", 1360:"70", 1160:"70", 1060:"70", 681:"85", 570:"85", 470:"85", 371:"85", 261:"85", 285:"100", 485:"100", 586:"100", 695:"100", 795:"100", 1105:"120", 1205:"120", 1405:"120", 1515:"120", 1615:"120"}
#red=120, orange=100, yellow=85, green=70
Dict_of_prices_for_second_uprading={1520:"100", 1420:"100", 1320:"100", 1120:"100", 1015:"100", 665:"115", 565:"115", 455:"115", 355:"115", 255:"115", 185:"130", 390:"130", 490:"130", 590:"130", 690:"130", 1000:"150", 1100:"150", 1311:"150", 1411:"150", 1510:"150",     1620:"100", 1521:"100", 1410:"100", 1210:"100", 1110:"100", 580:"115", 480:"115", 370:"115", 270:"115", 170:"115", 230:"130", 430:"130", 531:"130", 641:"130", 740:"130", 1090:"150", 1190:"150", 1400:"150", 1500:"150", 1600:"150",     1570:"100", 1470:"100", 1370:"100", 1170:"100", 1070:"100", 746:"115", 645:"115", 535:"115", 435:"115", 335:"115", 135:"130", 345:"130", 445:"130", 545:"130", 646:"130", 1065:"150", 1165:"150", 1365:"150", 1475:"150", 1575:"150",     1571:"100", 1471:"100", 1360:"100", 1160:"100", 1060:"100", 681:"115", 570:"115", 470:"115", 371:"115", 261:"115", 285:"130", 485:"130", 586:"130", 695:"130", 795:"130", 1105:"150", 1205:"150", 1405:"150", 1515:"150", 1615:"150"}
#red=150, orange=130, yellow=115, green=100

now=""
place_to_add=0 #Index of list, where an element will be added(for history function)
List_of_times=["","","","","",""] #A time, when a player answered the question or bought the cell 
List_of_SENTENCES=["","","","","",""] #A zone, in which a player answered the question or bought the cell 
List_of_names=["","","","","",""] #The question, that is answered, or the cell, that is bought, by a player
List_of_answering=["","","","","",""] #The question is answered True/False

#rules window
def Rules(menu):
    run=True
    if menu==True:
        resolution=(500,500)
    else:
        resolution=(1500,950)
    while run:
        Rules_part1=pygame.image.load("Rules_part1.png")   #load images
        Rules_part2=pygame.image.load("Rules_part2.png")
        display = pygame.display.set_mode( (700,870) )
        display.fill((255,255,255))                       #coordinates for images 
        display.blit(Rules_part1, (0,0))
        display.blit(Rules_part2, (3,515))
        if run==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
        pygame.display.update()
    display = pygame.display.set_mode(resolution)

# function that changes colours depending on players' turns
def Rect_color_change():
    global color1, color2, color3, color4, turn_of_player_color_change
    if number_of_players==2:
        if turn_of_player_color_change==3:
            turn_of_player_color_change=1
    elif number_of_players==3:
        if turn_of_player_color_change==4:
            turn_of_player_color_change=1
    elif number_of_players==4:
        if turn_of_player_color_change==5:
            turn_of_player_color_change=1

    color_of_turn=(235,92,92)              # color when it's players turn
    color_of_not_turn=(220,220,220)        # color when player is inactive
    if turn_of_player_color_change==1:
        color1=color_of_turn
        color2, color3, color4=color_of_not_turn, color_of_not_turn, color_of_not_turn
    elif turn_of_player_color_change==2:
        color2=color_of_turn
        color1, color3, color4=color_of_not_turn, color_of_not_turn, color_of_not_turn
    elif turn_of_player_color_change==3:
        color3=color_of_turn
        color2, color1, color4=color_of_not_turn, color_of_not_turn, color_of_not_turn
    elif turn_of_player_color_change==4:
        color4=color_of_turn
        color2, color3, color1=color_of_not_turn, color_of_not_turn, color_of_not_turn
    
#function for the end of the game
def end(List_of_average_points, number_of_players):
    if sounds==True:
        pygame.mixer.music.load('victory.wav')
        pygame.mixer.music.play(0)
    font=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 26)
    WINNER=font.render(f"{List_of_NAMES[List_of_average_points.index ( max(List_of_average_points) )]} is winner!", True, (221,22,81))
    CONFITTI_Red=[]                        # adding confetti coordinates and colours
    CONFITTI_Green=[]
    CONFITTI_Yellow=[]
    CONFITTI_Blue=[]
    CONFITTI_Purple=[]
    Red=(255,0,0)
    Green=(0,255,0)
    Yellow=(255,255,0)
    Blue=(0,0,255)
    Purple=(128,0,128)
    Dict_of_coordinates={3:(182,120), 4:(172,120), 5:(162,120), 6:(148,120), 7:(142,120), 8:(120,120)}
    for i in range(20):                          # random coordinates to display confetti 
        x1=random.randint(0,500)
        y1=random.randint(0,490)
        x2=random.randint(0,500)
        y2=random.randint(0,490)
        x3=random.randint(0,500)
        y3=random.randint(0,490)
        x4=random.randint(0,500)
        y4=random.randint(0,490)
        x5=random.randint(0,500)
        y5=random.randint(0,490)
        CONFITTI_Red.append( [x1,y1] )
        CONFITTI_Green.append( [x2,y2] )
        CONFITTI_Yellow.append( [x3,y3] )
        CONFITTI_Blue.append( [x4,y4] )
        CONFITTI_Purple.append( [x5,y5] )
    while 0 in List_of_average_points:    
        List_of_average_points.remove(0)
    run=True
    FPS=80
    clock=pygame.time.Clock()
    display = pygame.display.set_mode( (500,500) )   #window coordinates
    END=pygame.image.load("End.jpg")                 # arranging players according to place they got
    if number_of_players==3 or number_of_players==4:     
        First_place=List_of_chose_players[ List_of_average_points.index( max(List_of_average_points) ) ]
        Third_place=List_of_chose_players[ List_of_average_points.index( min(List_of_average_points) ) ]
        List_of_average_points[List_of_average_points.index ( max(List_of_average_points) )]=0
        List_of_average_points[List_of_average_points.index ( min(List_of_average_points) )]=0
        Second_place=List_of_chose_players[ List_of_average_points.index( max(List_of_average_points) ) ]
    elif number_of_players==2:
        First_place=List_of_chose_players[ List_of_average_points.index( max(List_of_average_points) ) ]
        Second_place=List_of_chose_players[ List_of_average_points.index( min(List_of_average_points) ) ]
    List_of_coordinates_for_end=[ (122,260), (219,240), (317,268) ]
    pygame.font.init()
    while run:                                      # animating end of the game
        clock.tick(FPS)
        display.blit(END, (0,0) )
        display.blit(pygame.image.load(f"{Second_place}"), (122,260) )
        display.blit(pygame.image.load(f"{First_place}"), (219,240) )
        if number_of_players==3 or number_of_players==4:
            display.blit(pygame.image.load(f"{Third_place}"), (317,268) )
        display.blit(WINNER, Dict_of_coordinates.get(len(List_of_NAMES[List_of_average_points.index ( max(List_of_average_points) )])))
        for i in CONFITTI_Red:
            i[1]+=1
            pygame.draw.circle(display, Red, i, 4)
            if i[1]>490:
                i[0]=random.randint(0,500)
                i[1]=random.randint(-200,0)
        for i in CONFITTI_Green:
            i[1]+=1
            pygame.draw.circle(display, Green, i, 4)
            if i[1]>490:
                i[0]=random.randint(0,500)
                i[1]=random.randint(-200,0)
        for i in CONFITTI_Yellow:
            i[1]+=1
            pygame.draw.circle(display, Yellow, i, 4)
            if i[1]>490:
                i[0]=random.randint(0,500)
                i[1]=random.randint(-200,0)
        for i in CONFITTI_Blue:
            i[1]+=1
            pygame.draw.circle(display, Blue, i, 4)
            if i[1]>490:
                i[0]=random.randint(0,500)
                i[1]=random.randint(-200,0)
        for i in CONFITTI_Purple:
            i[1]+=1
            pygame.draw.circle(display, Purple, i, 4)
            if i[1]>490:
                i[0]=random.randint(0,500)
                i[1]=random.randint(-200,0)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pygame.display.update()
    List_of_average_points.extend([0,0])

#function that makes code executable
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

# function that creates buttons to use in the game
def draw_button(display,x,y,text,font,clicked_once,width,height,image):
        global clicked
        action=False
        button_col = (204,0,0)
        hover_col =  (235,0,0)
        click_col = (255,0,0)
        text_col = (255,255,255)
        pos=pygame.mouse.get_pos()
        button_rect= Rect(x, y, width, height)    # condition whether button is clicked
        if button_rect.collidepoint(pos):               
            if pygame.mouse.get_pressed()[0]==1:
                clicked=True
                pygame.draw.rect(display, click_col, button_rect)
            elif pygame.mouse.get_pressed()[0]==0 and clicked==True:
                action=True
                clicked=False
            else:
                pygame.draw.rect(display, hover_col, button_rect)
        else:
            pygame.draw.rect(display, button_col, button_rect)
       
        
        pygame.draw.line(display,(0,0,0),(x,y),(x+width, y),2)        #add shading
        pygame.draw.line(display,(0,0,0),(x,y),(x,height+y),2)
        pygame.draw.line(display,(0,0,0),(x,height+y),(x+width,y+height),2)
        pygame.draw.line(display,(0,0,0),(x+width,y),(x+width,y+height),2)

        
        if image==None:
            text_img=font.render(text, True, text_col)    #add text to the button
        elif image!=None:
            text_img=image
        text_len= text_img.get_width()
        display.blit(text_img, (x+int(width/2)-int(text_len/2),y+5))
        if clicked_once==False:
            return action
        else:
            return None

# images of players
def players(display, List_of_current_coordinates, i):
    display.blit(pygame.image.load(f"{List_of_chose_players[i]}"),(List_of_current_coordinates[i][0], List_of_current_coordinates[i][1]))      

# function that shows cards of each player 
def show_cards_of_player(cards, player):
    global clicked_button_2
    run=True
    FPS=80
    if cards!=[]:
        clock=pygame.time.Clock()
        screen_resolution=[ (125,214), (250,214), (375,214), (500,214), (625,214), (750,214), (875,214), (1000,214), (1125,214), (1250,214), (1375,214), (1500,214), (1625,214) ]
        place_for_cards=[(0,0), (125,0), (250,0), (375,0), (500,0), (625,0), (750,0), (875,0), (1000,0), (1125,0), (1250,0), (1375,0), (1500,0) ]
        place_for_upgrades=[ (23,180), (148,180), (273,180), (398,180), (523,180), (648,180), (773,180), (898,180), (1023,180), (1148,180), (1273,180), (1398,180), (1523,180) ]
        display = pygame.display.set_mode( screen_resolution[len(cards)-1] )   #window coordinates
        pygame.display.update()
        pygame.font.init()
        font3=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 10)
        while run:                     
            clock.tick(FPS)
            display.fill((255,255,255))
            try:                                              #displaying cards of player
                for i in range(len(cards)):
                    Upgrade=font3.render(f"{Everything_related_to_cards[ List_of_bought_cards_by_players_string_and_position[player][1][i] ][3]}",True, (255,0,0))
                    display.blit(cards[i], place_for_cards[i])
                    display.blit(Upgrade, place_for_upgrades[i])
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            run=False
            except:
                for i in range(len(cards)-1):
                    Upgrade=font3.render(f"{Everything_related_to_cards[ List_of_bought_cards_by_players_string_and_position[player][1][i] ][3]}",True, (255,0,0))
                    display.blit(cards[i], place_for_cards[i])
                    display.blit(Upgrade, place_for_upgrades[i])
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            run=False
            pygame.display.update()
    else:                                                # if no cards are available 
        display = pygame.display.set_mode( (700,300) )   # window coordinates
        font=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 35)
        TEXT=font.render("There is no card at this deck",True,(0,0,0))
        Trebuchette=pygame.image.load("Trebuchet.jpg")
        while run:
            display.fill((255,255,255))
            display.blit(TEXT, (110,115))
            display.blit(Trebuchette, (520,180))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            pygame.display.update()
    clicked_button_2=False
    display = pygame.display.set_mode( (1500,950) )

# this function displays every event that players did during the game
def History():  
    j=place_to_add-1
    HISTORY=""
    while j>=0:
        if len(List_of_times[j])>0:
            History=f"->At {List_of_times[j]} {List_of_names[j]} {List_of_SENTENCES[j]} {List_of_answering[j]}\n"   # sample of text that will be diplayed
            HISTORY=HISTORY+History
            j-=1
        else:
            j-=1
    msgbox(msg=HISTORY, title="History")

# function that displays questions on each cell accordin to coordinates
def questions(turn_of_player,X,Y):
    time.sleep(0.1)
    global turn_of_player_color_change, sounds, n_event,choose_chem,choose_physics,choose_math,choose_alg, List_of_average_points, List_of_names, List_of_SENTENCES, List_of_times, place_to_add, n_question_ch_gr, n_question_ch_or, n_question_ph_re, n_question_ph_ye, n_question_ma_ye, n_question_ma_re, n_question_fr_gr, n_question_fr_ye, n_question_cs_gr, n_question_gq_re, n_question_al_or,n_question_cs_or, n_question_al_re,n_question_fr_re, n_question_en_ye, n_question_en_or,n_question_pl_gr, n_question_pl_ye, n_event_outlook, n_question_ge_gr, n_question_ge_or

    if turn_of_player==1:
        x=List_of_average_points[0]
        name=List_of_NAMES[0]
    elif turn_of_player==2:
        x=List_of_average_points[1]
        name=List_of_NAMES[1]
    elif turn_of_player==3:
        x=List_of_average_points[2]
        name=List_of_NAMES[2]
    elif turn_of_player==4:
        x=List_of_average_points[3]
        name=List_of_NAMES[3]
    
    if place_to_add==6:
        place_to_add=0
    
    if sounds==True:
        if X+Y!=941 or X+Y!=980 or X+Y!=940 or X+Y!=981 or X+Y!=935 or X+Y!=810 or X+Y!=845 or X+Y!=880 or X+Y!=1220 or X+Y!=1310 or X+Y!=1270 or X+Y!=1260 or X+Y!=290 or X+Y!=330 or X+Y!=345 or X+Y!=385 or X+Y!=1200 or X+Y!=1290 or X+Y!=1305 or X+Y!=1265 or X+Y!=765 or X+Y!=680 or X+Y!=746 or X+Y!=780:
            pass
        else:
            pygame.mixer.music.load('question.ogg')
            pygame.mixer.music.play(0)
    Host=0
    SENTENCE=""
    card_deck=[]
    if turn_of_player==1:
        card_deck=List_of_bought_cards_by_players_string_and_position[0][0]
    elif turn_of_player==2:
        card_deck=List_of_bought_cards_by_players_string_and_position[1][0]
    elif turn_of_player==3:
        card_deck=List_of_bought_cards_by_players_string_and_position[2][0]
    elif turn_of_player==4:
        card_deck=List_of_bought_cards_by_players_string_and_position[3][0]

   #Chemistry green          #checking coordinates
    if X+Y==1520 or X+Y==1620 or X+Y==1570 or X+Y==1571:   
                            #checking whether card is already boght or not 
        if "Chem_green" in card_deck: 
            Host=1
        else:
            if Everything_related_to_cards[1][0]==1:
                Host=0
            else:
                Host=None
        
        SENTENCE="Chemistry, zone:Green"
        title="Chemistry"       # list of questions for the cell
        list_of_questions_Chemistry_green={1:"Which concepts belong to homogeneous substances?\n\n1.Particles create layers or parts\n2.Light will scatter as it passes through\n3.Particles are evenly spread out\n4.Cannot see parts with microscope"
        ,2:"Which type of graph do we use, if we want to represent single events rather that continuous ones?"
        ,3:"What are some factors that might cause the percent yield of the reaction to appear to be more than 100%?"
        ,4:"A tank contains 10 liters of pure water. Salt water containing 20 grams of salt per liter is pumped into tank at 2 liters per minute. Express the salt concentration C(t) after t minutes (in g/L). Answer must be like: 5t/(9+t)"
        ,5:"How do we call hydrates, if water molecules have been driven off by heating?"
        ,6:"The largest number of molecules is in ..."}
        choices_Chemistry_1=["A)1,4","B)2,4","C)2,3","D)3,4"]
        choices_Chemistry_3=["1) product may contain by-products","2)if reverse reaction occurs","3)the product might not be completely dry","4)not mixed properly"]
        choices_Chemistry_6=["A) 36 g of water", "B) 28 g of carbon monoxide", "C) 46 g of ethyl alcohol", "D) 54 g of nitrogen pentoxide"]

        #displaying question and checking it, whether it is correct or not
        if n_question_ch_gr==1:     
            button=buttonbox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}", title=title, choices= choices_Chemistry_1)
            if button==choices_Chemistry_1[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[1][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_gr==2:
            ent=enterbox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}", title=title)
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                ent=ent.lower()
                if ent=="graph" or ent=="column":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[1][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[1][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_gr==3:
            button=multchoicebox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}", title=title, choices= choices_Chemistry_3)
            if button==['1) product may contain by-products', '3)the product might not be completely dry']:
                if Host==1 or Host==None:
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[1][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_gr==4:
            ent=enterbox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}", title=title)
            if ent=="20t/(5+t)":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[1][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_gr==5:
            ent=enterbox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}")
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                ent=ent.lower()
                if ent=="anhydrate":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[1][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[1][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_gr==6:
            button=buttonbox(f"{list_of_questions_Chemistry_green[n_question_ch_gr]}", title=title, choices= choices_Chemistry_6)
            if button==choices_Chemistry_6[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[1][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[1][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[1][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_ch_gr+=1

   #Chemistry orange   
    elif X+Y==586 or X+Y==545 or X+Y==531 or X+Y==490:
        if "Chem_orange" in card_deck:
            Host=1
        else:
            if Everything_related_to_cards[18][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Chemistry, zone:Orange"
        title="Chemistry"
        list_of_questions_Chemistry_orange={1:"To prepare 500 ml HCl 0,250 M a solution of HCl is available at 34,18 percent by weight and with a density of 1,70 g/mL. Calculate the volume of the solution to be taken. Don't forget to write unit."
        ,2:"You have 505 mL of a 0.125 M HCl solution and you want to dilute it to exactly 0.100 M. How much water should you add? Assume volumes are additive."
        ,3:"!!! Shown here are two aqueous solutions containing various ions.  Calculate the mass of the precipitation formed. Treat each sphere as 0.0500 mol.(give the result with 3 sig fig)"
        ,4:"On the sunny day, at the top of the Murov mountain 64.00 g of O2 occupies 69.93 L of the space. If the temperature of the weather is 25°C, find the pressure of the weather in Pascal (Pa). (Assume that, oxygen is an ideal gas) R = 0,0821 L·atm /mol·K Standard pressure = 1 atm = 101325 Pa pV=nRT .You do not need to write the unit in your answer, and give your answer with 3 sig fig."
        ,5:"Combustion of a 1,505 g sample of thiophene, a carbon-hydrogen-sulfur compound, yields 3,149 g CO2 , 0,645 g H2O and 1,146 g SO2 as the only products of the combustion. What is the empirical formula of the thiophene?"
        ,6:"M is the molecular weight of KMnO4. The equivalent weight of KMnO4 when it is converted into K2MnO4 is ..."}
        choices_Chemistry_6q = ["A) M", "B) M/3", "C) M/5", "D) M/7"]

        if n_question_ch_or==1:
            ent=enterbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title)
            if ent=="7.86 ml":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[18][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[18][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_or==2:
            ent=enterbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title)
            if ent=="126 ml":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[18][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[18][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_or==3:
            ent=enterbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title)
       
        elif n_question_ch_or==4:
            ent=enterbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title)
            if ent=="70900":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[18][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[18][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_or==5:
            ent=enterbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title)
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[18][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                if ent=="c4h4s" or ent=="C4H4S":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[18][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} points", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[18][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ch_or==6:
            button=buttonbox(f"{list_of_questions_Chemistry_orange[n_question_ch_or]}", title=title, choices= choices_Chemistry_6q)
            if button==choices_Chemistry_6q[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[18][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[18][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[18][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_ch_or+=1

   #Physics yellow
    elif X+Y==455 or X+Y==370 or X+Y==435 or X+Y==470:
        if "Physics_yellow" in card_deck:
            Host=1
        else:
            if Everything_related_to_cards[11][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Physics, zone:Yellow"
        title="Physics"
        list_of_questions_Physics_yellow={1:"What gives us the slope of the velocity-time graph?"
        , 2:"Velocity equation of the object is 3x+6 (m/s). Within 4 seconds the body has traveled a distance of 50 m. Calculate its average speed during this time."
        , 3:"A vector of magnitude 10 m is added to a vector of magnitude 6 m. The magnitude of this sum might be:"
        , 4:"What is the most accurate way of measuring the length of a 1 m rod?"
        , 5:"Two identical balls are connected by a spring. We consider the studied system to be {balls + spring}. The force exerted by the spring on the two balls is? Select one:"
        , 6:"Which of the following is not a vector quantity?"
        , 7:"The speed of light will be minimum while passing through ..."}
        if n_question_ph_ye==1:
            ent=enterbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title)
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                ent=ent.lower()
                if ent=="acceleration":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[11][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[11][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==2:
            ent=enterbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title)
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                if ent=="12.5 m/s":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[11][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[11][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==3:
            choices_Physics_3=["A)17 m","B)4 m","C)20 m","D)10 m"]
            button=buttonbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title, choices= choices_Physics_3)
            if button==choices_Physics_3[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[11][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==4:
            choices_Physics_4=["A) measuring and then moving ten times a 10.0 cm ruler with an uncertainty on the next position of 1mm","B) using a 1.00 m ruler once","C)Both of the methods lead to the same precision","D)enough information is not given"]
            button=buttonbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title, choices= choices_Physics_4)
            if button==choices_Physics_4[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[11][4]
                if Host==0:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==5:
            choices_Physics_5=["A) total force","B) an internal force","C) an external force","D) there is no correct answer"]
            button=buttonbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title, choices= choices_Physics_5)
            if button==choices_Physics_5[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[11][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==6:
            physics_yellow_choise_6 = ["A) speed", "B) velocity", "C) torque", "D) displacement"]
            button=buttonbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title, choices= physics_yellow_choise_6)
            if button==physics_yellow_choise_6[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[11][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_ye==7:
            physics_yellow_choise_7 = ["A) water", " B) vaccum", "C) air", "D) glass"]
            button=buttonbox(f"{list_of_questions_Physics_yellow[n_question_ph_ye]}", title=title, choices= physics_yellow_choise_7)
            if button==physics_yellow_choise_7[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[11][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[11][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[11][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[11][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_ph_ye+=1

   #Physics red
    elif X+Y==1510 or X+Y==1600 or X+Y==1575 or X+Y==1615:
        if "Physics_red" in card_deck:
            Host=1
        else:
            if Everything_related_to_cards[27][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Physics, zone:Red"
        title="Physics"
        list_of_questions_Physics_red={1:"A bullet is moving at a speed of 367 m/s when it embeds into a lump of moist clay. The bullet penetrates for a distance of 0.0621 m. Determine the acceleration (in m*s^-2) of the bullet while moving into the clay. (Assume a uniform acceleration.)"
        , 2:"A box of mass M = 10 Kg rests on a 35° inclined plane with the horizontal. A string is used to keep the box in equilibrium. The string makes an angle of 25 ° with the inclined plane. The coefficient of friction between the box and the inclined plane is 0.3. Find the magnitude of the tension T in the string (in N). Give the answer with 3 sig fig, take g=10 m/s^2."
        , 3:"A building is under construction, and a construction worker is standing on top of a 130 m high elevator shaft. The worker accidentally drops his hammer down the shaft.At what speed does the hammer hit the ground?\nNote: g=9.8 m/s^2, give the answer with 3 sig fig, in m/s (don’t write the  unit)."
        , 4:"A remote controlled toy car is driven off the edge of a table, at point A, at a speed of 2.2 m/s. It lands at point B. If the table is 1.1 m high, what is the horizontal distance, L, between point A and point B (in m)?\nNote: g=9.8 m/s^2, give the answer with 3 sig fig  (don’t write the unit)."
        , 5:"A 10.0 kg mass sliding on a frictionless horizontal surface at 7.00 m/s hits a spring that is attached to a wall. The spring has a spring constant of 5000 N/m.  Determine the maximum compression of the spring (in m).\nNote: don’t write the unit, give the answer with 3 sig fig."}
        if n_question_ph_re==1:
            ent=enterbox(msg=f"{list_of_questions_Physics_red[n_question_ph_re]}", title=title)
            if ent=="-1.08*10^6":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[27][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[27][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[27][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[27][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_re==2:
            ent=enterbox(image="problem_3.png", msg=f"{list_of_questions_Physics_red[n_question_ph_re]}", title=title)
            if ent=="79.3 N" or ent=="79.3N":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[27][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[27][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[27][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[27][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_re==3:
            ent=enterbox(msg=f"{list_of_questions_Physics_red[n_question_ph_re]}", title=title)
            if ent=="50.5 m/s":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[27][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[27][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[27][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[27][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_re==4:
            ent=enterbox(image="problem_Physics.png", msg=f"{list_of_questions_Physics_red[n_question_ph_re]}", title=title)
            if ent=="1.47 m" or ent=="1.47m":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[27][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[27][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[27][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[27][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ph_re==5:
            ent=enterbox(msg=f"{list_of_questions_Physics_red[n_question_ph_re]}", title=title)
            if ent=="0.313 m" or ent=="0.313m":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[27][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[27][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[27][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[27][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_ph_re+=1
   
   #Math analysis yellow
    elif X+Y==565 or X+Y==480 or X+Y==535 or X+Y==570:
        if "MA_yellow" in card_deck:
            Host=1
        else:
            if Everything_related_to_cards[10][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Math analysis, zone:Yellow"
        title="Math Analysis"
        list_of_questions_Math_Analysis_yellow={1:"Solve following expression"
        ,2:"Is the function continuous at point x=-2? If not, how do we call such kind of discontinuity?"
        ,3:"Solve following expression"
        ,4:"Find the oblige asymptote to the following function"
        ,5:"Find the horizontal asymptote to the function\nNote:give the answer as an example: y=const"
        ,6:"Find the inverse function"}
        if n_question_ma_ye==1:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question1_ma.png")
            if ent=="1":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_ye==3:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question3_ma.png")
            if ent=="1":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_ye==2:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question2_ma.png")
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                ent=ent.lower()
                if ent=="jumping" or ent=="jumping discontiniouty":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} point", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[10][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[10][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_ye==4:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question4_ma.png")
            if ent=="2x+17":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_ye==5:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question5_ma.png")
            if ent=="y=0":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[10][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_ye==6:
            math_yellow_choices = ["q6_ans1.png","q6_ans2.png","q6_ans3.png","q6_ans4.png"]
            button=buttonbox(msg=f"{list_of_questions_Math_Analysis_yellow[n_question_ma_ye]}", title=title, image="question6_ma.png",choices=math_yellow_choices)
            if button==math_yellow_choices[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[10][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[10][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[10][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered false"
        n_question_ma_ye+=1

   #Math analysis red 
    elif X+Y==1100 or X+Y==1190 or X+Y==1165 or X+Y==1205:
        if "MA_red" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[23][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Math analysis, zone:Red"
        title="Math Analysis"
        list_of_questions_Math_Analysis_red={1:"Using which theorem we can prove that lim x tends to ∞  f of x equals to L?\nA) If for every number ε there exists a corresponding number σ>0 such that for all x, 0<|x-x0|< σ   => |f(x)-L|<ε\nB) For every number ε>0 there exist a corresponding number M such that for all x>M, |f(x)-L|< ε\nC) If for every positive real number B there exists a corresponding σ>0 such that for all x 0<|x-x0|<σ  =>   f(x)>B"
        ,2:"For what values of a and b is f continuous at every x?"
        ,3:"What is the derivative of arccos(x)?"
        ,4:"It is given such condition. For what values of a and b f(x) is continious on (-inf,+inf). Write values a and b like: 2 3"
        ,5:"Solve following expression"
        ,6:"Find the horizontal asympote of the function"}
        choices_Math_Analysis_1=["A)","B)","C)"]
        if n_question_ma_re==1:
            button=buttonbox(f"{list_of_questions_Math_Analysis_red[n_question_ma_re]}", title=title, choices= choices_Math_Analysis_1)
            if button==choices_Math_Analysis_1[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[23][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_re==2:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_red[n_question_ma_re]}", title=title, image="question7_ma.png")
            if ent=="-1.5 -1.5" or ent=="-3/2 -3/2":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[23][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_re==3:
            button=buttonbox(msg=f"{list_of_questions_Math_Analysis_red[n_question_ma_re]}",choices=[], title=title, images=["answ1_8question_ma.png","answ2_8question_ma.png","answ3_8question_ma.png","answ4_8question_ma.png"])
            if button=="answ3_8question_ma.png":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[23][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_re==4:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_red[n_question_ma_re]}",title=title,image="question9_ma.png")
            if ent=="c":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[23][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_re==5:
            ent=enterbox(msg=f"{list_of_questions_Math_Analysis_red[n_question_ma_re]}",title=title,image="question10_ma.png")
            if ent=="-1/8":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[23][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ma_re==6:
            math_yellow_choices = ["A) y=-5, y=3", "B)y=-5", "C) y=3", "D)y=1"]
            button=buttonbox(msg=f"{list_of_questions_Math_Analysis_red[n_question_ma_ye]}", title=title, image="question12_ma.png",choices=math_yellow_choices)
            if button==math_yellow_choices[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[23][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[23][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[23][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[23][4]
                List_of_answering[place_to_add]="and answered false"
        n_question_ma_re+=1

   #French green
    elif X+Y==1015 or X+Y==1110 or X+Y==1070 or X+Y==1060:
        if "French_green" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[6][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="French, zone:Green"
        title="French"
        list_of_questions_French_green={1:"...  liseuse sert à lire."
        ,2:"Complètez la phrase:\nJ’aime beaucoup Nina, .... très agreable."
        ,3:"Combien d’adjectifs sont les descriptions physique?\nGrand, sympa, stressèe, intelligente, barbu, bavard, gentille, calme, timide, desagreable, rousse."
        ,4:"Complètez la phrase avec a la, a l’, au, aux, et chez le:\nJe vais ... poissonier."
        ,5:"Qu’est que nous pouvons acheterchez la fromagferie?"
        ,6:"Dans cette phrase, il manque un mot: trouvez-le:\nNous …... sommes perdus dans la ville."}
        choices_French_1=["A)Cette", "B)Ce", "C)Ces"]
        choices_French_2=["A)C’est","B)Il est","C)Elle est"]
        choices_French_5=["A)Le camembert","B)La viande","C)Un gateau","D)La baguette"]
        if n_question_fr_gr==1:
            button=buttonbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title,choices=choices_French_1)
            if button==choices_French_1[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[6][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_gr==2:
            button=buttonbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title,choices=choices_French_2)
            if button==choices_French_2[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[6][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_gr==3:
            ent=enterbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title)
            if ent=="3":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[6][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]  
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_gr==4:
            ent=enterbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title)
            if ent=="chez le" or ent=="Chez le":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[6][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_gr==5:
            button=buttonbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title,choices=choices_French_5)
            if button==choices_French_5[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[6][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_gr==6:
            ent=enterbox(msg=f"{list_of_questions_French_green[n_question_fr_gr]}", title=title)
            if ent=="nous" or ent == "Nous":
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[6][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[6][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[6][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[6][4]
                List_of_answering[place_to_add]="and answered false"
        n_question_fr_gr+=1

   #French yellow
    elif X+Y==355 or X+Y==270 or X+Y==335 or X+Y==371:
        if "French_yellow" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[12][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="French, zone:Yellow"
        title="French"
        list_of_questions_French_yellow={1:"Complètez la phrase avec le bon adjectif possessif:\nIls invitent (ils) ... amis à la maison"
        ,2:"Ècrire un verbe soyer la forme de l'impèratif:\n... (vous) à l’heure au concert!"
        ,3:"Accortez l’adjectif:\nVous prenez les chapeaux (mexicain) ..."
        ,4:"Choisir la bonne réponse:\n... je vais acheterun tablet."
        ,5:"Compéltez la phrase:\nLe ciel est gris, il y a beaucoup de ..."}
        choices_French_4=["A)Hier","B)Il y a 3 jours","C) Dans une semaine","D)L’année dernière"]
        if n_question_fr_ye==1:
            ent=enterbox(msg=f"{list_of_questions_French_yellow[n_question_fr_ye]}", title=title)
            if ent=="leurs" or ent=="Leurs":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[12][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[12][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[12][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[12][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_ye==2:
            ent=enterbox(msg=f"{list_of_questions_French_yellow[n_question_fr_ye]}", title=title)
            if ent=="soyez" or ent=="Soyez":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[12][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[12][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[12][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[12][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_ye==3:
            ent=enterbox(msg=f"{list_of_questions_French_yellow[n_question_fr_ye]}", title=title)
            if ent=="mexicains" or ent=="Mexicains":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[12][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[12][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[12][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[12][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_ye==4:
            button=buttonbox(msg=f"{list_of_questions_French_yellow[n_question_fr_ye]}",title=title,choices=choices_French_4)
            if button==choices_French_4[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[12][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[12][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[12][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[12][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_ye==5:
            ent=enterbox(msg=f"{list_of_questions_French_yellow[n_question_fr_ye]}", title=title)
            if ent=="nuages" or ent=="Nuages":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[12][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[12][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[12][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[12][4]
                List_of_answering[place_to_add]="and answered false"


        n_question_fr_ye+=1

   #French red
    elif  X+Y==1311 or X+Y==1400 or X+Y==1365 or X+Y==1405:
        SENTENCE="French, zone:Red"
        title="French"
        french_questions_red={
        1:"Conjuguez le verbe pour completer less regles:\nIl (ne pas falloir) …..... rester au milieu de la route.",
        2: "Choisis  le bon reponse.\nC’est le dossier (qui/que/qu’) je t’ai envoyé hier.(write whether qui, que or qu’ in the answer)",
        3:"Remettez les mots dans l’ordre pour faire des phrases. \nL'hôtel /meilleurs / sont / Les repas / à l’auberge / qu’à.\nA)  Les repas qu’à L'hôtel  à l’auberge sont /meilleurs\nB) Les repas sont meilleurs à l’auberge qu’à L'hôtel. \nC) Les repas sont à l’auberge qu’à L'hôtel  meilleurs.",
        4: "Il répare les serrures, il est... ",
        5:"Ça sert à ouvrir une porte, c’est un..."}
        if n_question_fr_re==1:
            ent=enterbox(msg=f"{french_questions_red[n_question_fr_re]}", title=title)
            if ent=="ne feut pas" or ent=="Ne feut pas":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[25][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[25][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[25][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[25][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_re==2:
            ent=enterbox(msg=f"{french_questions_red[n_question_fr_re]}", title=title)
            if ent=="que":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[25][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[25][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[25][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[25][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_re==3:
            LIST=["A", "B", "C"]
            button=buttonbox(f"{french_questions_red[n_question_fr_re]}", title=title, choices=LIST)
            if button==LIST[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[25][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[25][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[25][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[25][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_re==4:
            ent=enterbox(msg=f"{french_questions_red[n_question_fr_re]}", title=title)
            if ent=="serrurier" or ent=="Serrurier":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[25][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[25][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[25][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[25][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_fr_re==5:
            ent=enterbox(msg=f"{french_questions_red[n_question_fr_re]}", title=title)
            if ent=="clé" or ent=="Clé":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[25][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[25][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[25][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[25][4]
                List_of_answering[place_to_add]="and answered false"
        n_question_fr_re+=1

   #CS green
    elif X+Y==1420 or X+Y==1521 or X+Y==1470 or X+Y==1471:
        if "CS_green" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[2][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="CS, zone:Green"
        title="CS"
        list_of_questions_CS_green={1:"Which concepts belong to tuples?\n1)Mutable\n2)Ordered\n3)Doesn’t let duplicates\n4)When function returns more than one statement, it returns them in tuple"
        ,2:"What is the output of the program:"
        ,3:"Which function creates a set, which cannot be modified?"
        ,4:"Which module provides a way of plotting graphs with Python?"
        ,5:"How we can access ‘y’ in the list:"
        ,6:"Which of the following statement can be used to free the allocated memory?"}
        choices_CS_1=["A)1,3","B)2,4","C)1,4","D)2,3"]
        choices_Cs_5=["A)L[‘y’]","B)L[3][2]","C)L[4][3][3]","D)L[3][2][2]"]
        if n_question_cs_gr==1:
            button=buttonbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}",title=title,choices=choices_CS_1)
            if button==choices_CS_1[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[2][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_gr==2:
            ent=enterbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}", title=title, image="cs_question2.png")
            if ent=="77":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[2][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_gr==3:
            ent=enterbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}", title=title)
            if ent=="frozenset()"  or ent=="frozenset":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[2][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_gr==4:
            ent=enterbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}", title=title)
            if ent==None:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false"
            else:
                ent=ent.lower()
                if ent=="matplotlib":
                    if Host==1 or Host==None:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} point", title=title, ok_button="OK")
                        x+=Everything_related_to_cards[2][4]
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('correct.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if Host==1:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                    else:
                        if sounds==True:
                            pygame.mixer.music.load('wrong.ogg')
                            pygame.mixer.music.play(0)
                        mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                        x-=Everything_related_to_cards[2][4]
                    List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_gr==5:
            ent=enterbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}", title=title, image="cs_question5.png")
            if ent=="L[3][2][2]":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[2][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[2][4]}", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_gr==6:
            cs_green6=["A) remove ()"," B) free ()","C) vanish ()","D) erase ()"]
            button=buttonbox(msg=f"{list_of_questions_CS_green[n_question_cs_gr]}", title=title, choices=cs_green6)
            if button==cs_green6[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[2][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[2][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[2][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[2][4]
                List_of_answering[place_to_add]="and answered false" 

        n_question_cs_gr+=1

   #CS orange
    elif X+Y==390 or X+Y==430 or X+Y==445 or X+Y==485:
        if "CS_orange" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[2][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="CS, zone:Orange"
        title="CS"
        list_of_questions_CS_orange={1:"How many concepts of the following are true of Python dictionaries:\n1)dictionaries can be nested to any depth \n2) all the keys in a dictionary must be of the same type \n3)Dictionaries are accessed by key \n4)Items are accessed by their position in a dictionary"
        ,2:"What is the output of the following program?"
        ,3:"Does both the loops in the following programs prints the correct string length?"
        ,4:"What is the output of the following program?"
        ,5:"Which is the correct syntax to use typedef for struct?"
        ,6:"Which of the following statements about the null pointer is correct"}
        if n_question_cs_or==1:
            ent=enterbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}", title=title)
            if ent=="2":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_or==2:
            list_cs_or_2= ["A) Compile error", "B) Runtime error", " C) 5", "D) 10"]
            ent=enterbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}\nA) Compile error\nB) Runtime error\nC) 5\nD) 10", title="FSA",image="cs_or_2.png")
            if ent=="D" or ent=="D)":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_or==3:
            ent=enterbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}\nA) Yes, both the loops print the correct length\nB) Only for loop prints the correct length\nC) Only while loop prints the correct length\nD) Compile error in the program", title="CART",image="cs_or_3.png")
            if ent=="B" or ent=="B)":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_or==4:
            list_cs_or_4= ["A) 0 1", "B) 0 2", "C) 0 8", "D) Compile error"]
            ent=enterbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}\nA) 0 1\nB) 0 2\nC) 0 8\nD) Compile error", title="FSA",image="cs_or_4.png")
            if ent=="C" or ent=="c":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_or==5:
            list_cs_or_5= ["A) typedef struct temp\n{\nint a;\n}\nTEMP;","B) typedef struct\n{\nint a;\n}\nTEMP;","C) struct temp\n{\nint a;\n}\ntypedef struct temp TEMP;","D) All of the mentioned"]
            button=buttonbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}", title=title,choices=list_cs_or_5)
            if button==list_cs_or_5[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_cs_or==6:
            list_cs_or_6= ["A) The null pointer is similar to an uninitialized pointer","B) You can declare a null pointer as char* p = (char*)0","C) The NULL macro is defined only in the stdio.h header","D) The sizeof( NULL) operation would return the value 1"]

            button=buttonbox(msg=f"{list_of_questions_CS_orange[n_question_cs_or]}", title=title,choices=list_cs_or_6)
            if button==list_cs_or_6[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[17][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[17][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"This answer is incorrect, you lose {Everything_related_to_cards[17][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[17][4]
                List_of_answering[place_to_add]="and answered false"
                
        n_question_cs_or+=1

   #General question red
    elif X+Y==1000 or X+Y==1090 or X+Y==1065 or X+Y==1105:
        if "GQ_red" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[22][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="General question, zone:Red"
        title="General Questions"
        list_of_questions_General_Questions_red={1:"What is the capital of Iceland?"
        ,2:"What is Queen Elizabeth II's surname?"
        ,3:"How many valves does the human's heart have?"
        ,4:"At what temperature are Fahrenheit and Celsius equal to each other?"
        ,5:"If you get scurvy, what vitamin are you deficient in?"
        ,6:"What is the part of the eye called that's colored and surrounds the pupil?"
        ,7:"What type of sugar does the brain need for energy?"
        ,8:"Who discovered radio waves?"
        ,9:"What disease can you get from ticks?"
        ,10:"Oil, natural gas and coal are examples of..."
        ,11:"What is the largest moon of Saturn called?"
        ,12:"Which polymer is used to manufacture electric switches, computer disks etc."}
        choices_General_Questions=[ ["A)Niamey","B)Monrovia","C)Reykjavik","D)Nicosia"],
        ["A)Hazelton","B)Windsor","C)Denver","D)Crawford"]
        ,["A)3","B)2","C)5","D)4"]
        ,["A)40","B)-40","C)20","D)-20"]
        ,["A)E","B)D","C)A","D)C"]
        ,["A)Iris","B)Lens","C)Cornea","D)Sclera"]
        ,["A)Lactose","B)Glucose","C)Fructose","D)Sucrose"]
        ,["A)Thomas Edison","B)Nikola Tesla","C)Guglielmo Marconi","D) Heinrich Hertz"]
        ,["A)Alzheimer’s disease","B)Measles","C)Lyme disease","D)Pertussis"]
        ,["A) Biofuels","B) Geothermal resources","C) Fossil fuels","D) Renewable resources"]
        ,["A) Titan","B) Ganymede","C)Dione","D)Mimas"]
        ,["A)Orlon","B)Bakelite","C)Kevlar","D)Nylon"] ]
        Answers=["C)Reykjavik","B)Windsor","D)4","B)-40","D)C","A)Iris","B)Glucose","D) Heinrich Hertz","C)Lyme disease","C) Fossil fuels","A) Titan","B)Bakelite"]
        button=buttonbox(msg=f"{list_of_questions_General_Questions_red[n_question_gq_re]}", title=title, choices=choices_General_Questions[n_question_gq_re-1])
        if button==Answers[n_question_gq_re-1]:
            if Host==1 or Host==None:
                if sounds==True:
                    pygame.mixer.music.load('correct.ogg')
                    pygame.mixer.music.play(0)
                mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[22][4]} point", title=title, ok_button="OK")
                x+=Everything_related_to_cards[22][4]
            else:
                if sounds==True:
                    pygame.mixer.music.load('correct.ogg')
                    pygame.mixer.music.play(0)
                mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
            List_of_answering[place_to_add]="and answered true"
        else:
            if Host==1:
                if sounds==True:
                    pygame.mixer.music.load('wrong.ogg')
                    pygame.mixer.music.play(0)
                mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
            else:
                if sounds==True:
                    pygame.mixer.music.load('wrong.ogg')
                    pygame.mixer.music.play(0)
                mesage=msgbox(msg=f"This answer is incorrect, your average point is diminished by {Everything_related_to_cards[22][4]}", title=title, ok_button="OK")
                x-=Everything_related_to_cards[22][4]
            List_of_answering[place_to_add]="and answered false"
       
        n_question_gq_re+=1
   
   #Algebra orange
    elif X+Y==185 or X+Y==230 or X+Y==245 or X+Y==285:
        if "Algebra_orange" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[15][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Algebra, zone:Orange"
        title="Algebra"
        list_of_questions_Algebra_orange={1:"How many common positive divisors do numbers 64680 and 2142 have?"
        ,2:"Simplify the expression:\ngcd(a + b, lcm(a, b)), where a and b are natural numbers"
        ,3:"Determine one particular integer solution (u, v) of the equation 51u + 39v = d by using the Extended Euclidean Algorithm. (first give the value for u then for v)"
        ,4:"Determine a particular integer solution (u, v) of the equation 77u + 56v = d by using the Extended EuclideanAlgorithm\nNote: first write the value of u, then the value of v. Example: -12,4"
        ,5:"Find all possible solutions for a system:\nx ≡ 3 mod 6\nx ≡ 4 mod 17\nx ≡ 5 mod 19"
        ,6:" How many 7-digit telephone numbers can be formed if the first digit cannot be 0 or 1?\nNote: write answer in scientific notation ex: 12e5"}
        choices_Algebra_2=["A)1","B)lcm(a,b)","C)a","D)gcd(a,b)"]
        choices_Algebra_3=["A) u=-3, v=4","B)u=-3, v=-4","C)u=3,v=-4","D)u=3, v=4"]
        choices_Algebra_5=["A) x=1938n + 1449","B)x=1938n+1215","C)x=1900n+1449","D)x=1949n+946"]
        if n_question_al_or==1:
            ent=enterbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}",title=title)
            if ent=="8":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_or==2:
            button=buttonbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}", title=title, choices=choices_Algebra_2)
            if button==choices_Algebra_2[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_or==3:
            button=buttonbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}", title=title, choices=choices_Algebra_3)
            if button==choices_Algebra_3[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:   
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_or==4:
            ent=enterbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}",title=title)
            if ent=="3,-4" or ent=="3 -4" or ent=="-4 3" or ent=="-4,3":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_or==5:
            button=buttonbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}", title=title, choices=choices_Algebra_5)
            if button==choices_Algebra_5[0]:
                if Host==1 or Host==None: 
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_or==6:
            ent=enterbox(msg=f"{list_of_questions_Algebra_orange[n_question_al_or]}",title=title)
            if ent=="8e6":
                if Host==1 or Host==None: 
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[15][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[15][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[15][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[15][4]
                List_of_answering[place_to_add]="and answered false"
               
        n_question_al_or+=1

   #Algebra red
    elif X+Y==1411 or X+Y==1500 or X+Y==1475 or X+Y==1515:
        if "Algebra_red" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[26][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Algebra, zone:Red"
        title="Algebra"
        list_of_questions_Algebra_red={1:"How many 10-letter patterns can be formed from the letters of the word “BASKETBALL”?"
        ,2:"A box contains 12 black and 8 green marbles. How many ways can 3 black and 2 green marbles be chosen?"
        ,3:"A Club consists of 20 members, of which 9 are male and 11 are female.\nSeven members will be selected to form an event-planning committee. How many committees of 4 females and 3 males can be formed?"
        ,4:"Three hardcover books and 5 paperbacks are placed on a shelf.\n How many ways can the books be arranged if all the hardcover books must be together and all the paperbacks must be together?"
        ,5:"In the first box, there are 2 white and 10 black balls, in the second box, 8 white and 4 black balls. From each box one ball is taken. Find the probability that both balls are white."
        ,6:"8 students on a student council are assigned 8 seats around a U-shaped table. How many different ways can students be assigned seats at the table?"}
        if  n_question_al_re == 1:
            ent=enterbox(msg=f"{list_of_questions_Algebra_red[n_question_al_re]}",title=title)
            if ent=="604800":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_re == 2:
            ent=enterbox(msg=f"{list_of_questions_Algebra_red[n_question_al_re]}",title=title)
            if ent=="248":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_re == 3:
            list_answers_alg_re3=["A) 11!", "B)4P11*3P9", "C)4C11*3C9", "D)11!/(4!*3!)"]
            button=buttonbox(f"{list_of_questions_Algebra_red[n_question_al_re]}", title=title, choices=list_answers_alg_re3)
            if button==list_answers_alg_re3[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_re==4:
            ent=enterbox(msg=f"{list_of_questions_Algebra_red[n_question_al_re]}",title=title)
            if ent=="1440":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_re==5:
            ent=enterbox(msg=f"{list_of_questions_Algebra_red[n_question_al_re]}",title=title)
            if ent=="1/9":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_al_re == 6:
            list_answers_alg_re6=["A) 7!", " B) 8", "C)7!+8!", "D)8!"]
            button=buttonbox(f"{list_of_questions_Algebra_red[n_question_al_re]}", title=title, choices=list_answers_alg_re6)
            if button==list_answers_alg_re6[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[26][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[26][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[26][4]
                List_of_answering[place_to_add]="and answered false"
        
        n_question_al_re+=1

   #English yellow 
    elif X+Y==665 or X+Y==580 or X+Y==645 or X+Y==681:
        if "English_yellow" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[15][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="English,zone:Yellow"
        title="English"
        list_of_questions_eng_ye={
        1:"A:'_____ did you live in New York?'\nB:'I lived there for almost five years.'"
        ,2:"When ___?"
        ,3:"They threw a rock ___ the window and broke the glass"
        ,4:"What _____ to do when we finish? "
        ,5:"He crashed his car into a tree because he _____ attention to the road."
        ,6:"I _____ beans when I was a child, but now I love them."}
        en_ye_1 = ["A)When", "B) How much", "C)How long"]
        if n_question_en_ye==1:
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_1)
            if button==en_ye_1[2]: 
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_ye==2:
            en_ye_2 = ["A) did you arrived", " B) did you arrive", "C) were you arrived"]
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_2)
            if button==en_ye_2[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_ye==3:
            en_ye_3 = ["A)through", "B)across", "C)into"]
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_3)
            if button==en_ye_3[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_ye==4:
            en_ye_4 = ["A)have we","B)must we","C)should we","D)do we have"]
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_4)
            if button==en_ye_4[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_ye==5:
            en_ye_5 = ["A)didn't pay","B)hadn't paid","C)wasn't paying","D)not paid"]
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_5)
            if button==en_ye_5[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_ye==6:
            en_ye_6 = ["A)didn't use to like","B)usedn't to like","C)didn't use to liking","D)was not used to like"]
            button=buttonbox(f"{list_of_questions_eng_ye[n_question_en_ye]}", title=title, choices=en_ye_6)
            if button==en_ye_6[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[9][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[9][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[9][4]
                List_of_answering[place_to_add]="and answered false"
        n_question_en_ye+=1

   #English orange
    elif X+Y==590 or X+Y==641 or X+Y==646 or X+Y==695:
        if "English_orange" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[19][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="English,zone:Orange"
        title="English"
        list_of_questions_eng_or={
         1:"Hundreds of people _____ after a fire broke out in an industrial unit." 
        ,2:"She _____ if we hadn't been there to take her to the hospital"
        ,3:"I'm very happy _____ in India. I really miss being there."
        ,4:"I wish I ___ those words. But now it’s too late"
        ,5:"The woman, who has been missing for 10 days, is believed _____."
        ,6:"She was working on her computer with her baby next to _____"}
        if n_question_en_or==1:
            en_or_1 = ["A)have been evacuating","B)were evacuate","C)have evacuated","D)have been evacuated"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_1)
            if button==en_or_1[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_or==2:
            en_or_2 = ["A)wouldn't survive","B)wouldn't have survived","C)hadn't survived","D)didn't survive"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_2)
            if button==en_or_2[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_or==3:
            en_or_3 = ["A)to live","B)to have lived ","C)to have lived ","D)to be living"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_3)
            if button==en_or_3[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_or==4:
            en_or_4 = ["A)on account of", "B)due", "C)because", "D) owing"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_4)
            if button==en_or_4[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_en_or==5:
            en_or_5 = ["A)to be abducted", "B)to be abducting", "C)to have been abducted", "D) to have been abducting"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_5)
            if button==en_or_5[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_en_or==6:
            en_or_6 = ["A)herself", "B)her", "C)her own", "D)hers"]
            button=buttonbox(f"{list_of_questions_eng_or[n_question_en_or]}", title=title, choices=en_or_6)
            if button==en_or_6[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[19][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[19][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[19][4]
                List_of_answering[place_to_add]="and answered false"
        
        n_question_en_or+=1

   #Plagiarizm green
    elif X+Y==1320 or X+Y==1410 or X+Y==1370 or X+Y==1360:
        if "Plagiarism_green" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[3][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Plagiarizm,zone:Green"
        title="Plagiarizm"
        list_of_questions_pl_gr={
        1:"Plagiarism can be defined as",
        2:"When is it necessary to cite a source?",
        3:"In addition to citing sources for written texts, it is also important to reference",
        4:"A student accused of plagiarism based upon evidence from Turnitin.com has no defense against being penalized"}
        if n_question_pl_gr==1:
            pl_gr_1=["A) representing another person's work--their words and/or ideas--as your own","B) not acknowledging the sources your ideas build upon","C) paraphrasing another's ideas with explicit attribution to the author","D) A & B"]
            button=buttonbox(f"{list_of_questions_pl_gr[n_question_pl_gr]}", title=title, choices=pl_gr_1)
            if button==pl_gr_1[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[3][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[3][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_pl_gr==2:
            pl_gr_2=["A) When your ideas build on someone else's","B) When you are paraphrasing someone else's ideas","C) When you use someone else's words","D) If you are unsure whether you should cite the source","E) All of the above"]
            button=buttonbox(f"{list_of_questions_pl_gr[n_question_pl_gr]}", title=title, choices=pl_gr_2)
            if button==pl_gr_2[4]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[3][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[3][4]
                List_of_answering[place_to_add]="and answered false"
        
        elif n_question_pl_gr==3:
            pl_gr_3=["A) any information taken from standard reference works such as encyclopedias, dictionaries, or statistical sources","B) ideas taken from a lecture by a professor","C) information taken from the internet","D) ideas gleaned from classroom discussion","E) all of the above."]
            button=buttonbox(f"{list_of_questions_pl_gr[n_question_pl_gr]}", title=title, choices=pl_gr_3)
            if button==pl_gr_3[4]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[3][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[3][4]
                List_of_answering[place_to_add]="and answered false"
        
        elif n_question_pl_gr==4:
            pl_gr_4=["A)True", "B)False"]
            button=buttonbox(f"{list_of_questions_pl_gr[n_question_pl_gr]}", title=title, choices=pl_gr_4)
            if button==pl_gr_4[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[3][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[3][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[3][4]
                List_of_answering[place_to_add]="and answered false"

        

        n_question_pl_gr+=1

   #Plagiarizm yellow
    elif X+Y==255 or X+Y==170 or X+Y==235 or X+Y==261:
        if "Plagiarism_yellow" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[13][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Plagiarizm,zone:Yellow"
        title="Plagiarizm"
        list_of_questions_pl_ye={
        1:"A student accused of plagiarism based upon evidence from Turnitin.com has no defense against being penalized.",
        2:"Two students work together on their papers. When they submit them to Turnitin.com, they turn up a 35%  match. Their professors will find that",
        3:"Texts like Homer's Iliad or the Bible do not need referencing, since they are ancient and are not covered bycopyright laws"}

        if n_question_pl_ye==1:
            pl_ye_1=["A)True", "B)False"]
            button=buttonbox(f"{list_of_questions_pl_ye[n_question_pl_ye]}", title=title, choices=pl_ye_1)
            if button==pl_ye_1[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[13][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[13][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_pl_ye==2:
            pl_ye_2=["A they are not guilty of plagiarism, since the ideas were derived in common","B only the student to submit his paper last is guilty of plagiarism","C regardless of intent, the students have committed plagiarism","D the students have committed plagiarism if evidence of the intent to plagiarize can be established"]
            button=buttonbox(f"{list_of_questions_pl_ye[n_question_pl_ye]}", title=title, choices=pl_ye_2)
            if button==pl_ye_2[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[13][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[13][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_pl_ye==3:
            pl_ye_3=["A)True", "B)False"]
            button=buttonbox(f"{list_of_questions_pl_ye[n_question_pl_ye]}", title=title, choices=pl_ye_3)
            if button==pl_ye_3[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[13][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[13][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[13][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_pl_ye+=1

   #Geometry green
    elif X+Y==1120 or X+Y==1210 or X+Y==1170 or X+Y==1160:
        if "Geometry_green" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[5][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Geometry,zone:Green"
        title="Geometry"
        list_geom_gr = {
        1:"Convert from spherical to cylindrical coordinates: (sqrt(3),3,-2)"
        ,2:"Write down the equation of the plane that passes through the A (1; −1; 2) point and parallel to the given plane:\nx − 3y + 2z + 1 = 0"
        ,3:"Find the angle between two planes. x + 4y − z + 1 = 0 and x + y − z − 3 = 0"
        ,4:"Given two lines:\nL1: x=1+t, y=t, z=2+t L2: x-3=y-1=z-3\nFind the distance between them"
        ,5:"If two lines with slopes k1 and k2 are orthogonal, which condition is true for their slopes?"
        ,6:"Determine whether given planes are parallel, orthogonal, or neither.\n(write your answer as full word)\nP1: x-5y-z=1 , P2:5x-25y-5z=-3"}

        if n_question_ge_gr==1:
            ge_gr_1 = ["A) (2, π/2, 1)", "B) (1, π/2, 1) ", "C) (1, π, 4) ", "D) (4, π/2, 6)"]
            button=buttonbox(f"{list_geom_gr[n_question_ge_gr]}", title=title, choices=ge_gr_1) 
            if button==ge_gr_1[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"
    
        elif n_question_ge_gr==2:
            ge_gr_2 = ["A) 2x-3y+2z+8=0", "B) x+3y+2z-8=0", "C) x+2y+2z-4=0", "D)x-3y+2z-8=0"]
            button=buttonbox(f"{list_geom_gr[n_question_ge_gr]}", title=title, choices=ge_gr_2)
            if button==ge_gr_2[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_ge_gr==3:
            ge_gr_3 = ["A) 60", "B) sin^-1(½)", "C) Cos^-1 (sqrt (2/3))", "D) sin^-1 (sqrt(2/3))"]
            button=buttonbox(f"{list_geom_gr[n_question_ge_gr]}", title=title, choices=ge_gr_3)
            if button==ge_gr_3[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"

        elif n_question_ge_gr==4:
            ge_gr_4 = ["A) sqrt(6)/3", "B)sqrt(6)", "C)3/2", "D)sqrt(3)/2"]
            button=buttonbox(f"{list_geom_gr[n_question_ge_gr]}", title=title, choices=ge_gr_4)
            if button==ge_gr_4[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"
        
        elif n_question_ge_gr==5:
            ge_gr_5 = ["A) k1*k2=-1", "B) k1*k2=1", "C)k1*k2=0", "D)K1+k2=0"]
            button=buttonbox(f"{list_geom_gr[n_question_ge_gr]}", title=title, choices=ge_gr_5)
            if button==ge_gr_5[0]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"
        
        elif n_question_fr_gr==6:
            ent=enterbox(msg=f"{list_geom_gr[n_question_ge_gr]}", title=title)
            if ent=="Parallel" or ent=="parallel":
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[5][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[5][4]} points", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[5][4]
                List_of_answering[place_to_add]="and answered false"
    
        n_question_ge_gr+=1

   #Geometry orange
    elif X+Y==690 or X+Y==740 or X+Y==745 or X+Y==795:
        if "Geometry_orange" in card_deck:
                Host=1
        else:
            if Everything_related_to_cards[20][0]==1:
                Host=0
            else:
                Host=None
        SENTENCE="Geometry, zone: Orange"
        title="Geometry"
        list_geom_or = {
            1:"Find the point on the line 2i+3j+k+t(-3i+j+k) that is closest to the origin, and find that distance"
            ,2:"Find the point of intersection of the lines of equations x=-2y=3z and x=-5-t , y=-1+t , z=t-11"
            ,3:"Find the distance between two skew lines:\nL1: x=t, y=1+t, z=2+t   L2: x/2=(y-1)/3=z-3"
            ,4:"Convert from spherical to rectangular coordinates: (4, π/3 , 2π/3 )"
            ,5:"Find the volume of the triangular pyramid with vertices A (1; 1; 1) , B (3; 2; 1), C (5; 3; 2), D (3; 4; 5)."
            ,6:"State the point of intersection of plane: 2x+y-z=11 and line x=1+t, y=3-2t, z=2+4t"
        }

        if n_question_ge_or==1:
            ge_or_1 = ["A) 5*sqrt(6)/11", "B) 5sqrt(6/11)", "C) sqrt(30)", "D) 6/sqrt(11)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_1)
            if button==ge_or_1[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ge_or==2:
            ge_or_2 = ["A) (12,6,4)", "B)(−12,6,−4)", "C)(10,6,4)", "D)(12,-6,-4)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_2)
            if button==ge_or_2[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ge_or==3:
            ge_or_3 = ["A)½", "b)1/ sqrt(6)", "C)2/sqrt(6)", "D) sqrt(2)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_3)
            if button==ge_or_3[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ge_or==4:
            ge_or_4 = ["A) (sqrt(3),-2,3)", "B)(3,-2,3)", "C)(sqrt(3),3,-2)", "D)(sqrt(2),-4,-2)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_4)
            if button==ge_or_4[2]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ge_or==5:
            ge_or_5 = ["A) 5*sqrt(6)/11", "B) 5sqrt(6/11)", "C) sqrt(30)", "D) 6/sqrt(11)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_5)
            if button==ge_or_5[1]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"
        elif n_question_ge_or==6:
            ge_or_5 = ["A)(-1,-7,-6)", "B)(1,-7,6)", "C) (1,-7-,6)", "D) (-1,7,-6)"]
            button=buttonbox(f"{list_geom_or[n_question_ge_or]}", title=title, choices=ge_or_5)
            if button==ge_or_5[3]:
                if Host==1 or Host==None:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Great! Your answer is correct, you get {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x+=Everything_related_to_cards[20][4]
                else:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, but you don't get any points", title=title, ok_button="OK")
                List_of_answering[place_to_add]="and answered true"
            else:
                if Host==1:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, but you don't lose any points", title=title, ok_button="OK")
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg=f"Your answer is wrong, you lose {Everything_related_to_cards[20][4]} point", title=title, ok_button="OK")
                    x-=Everything_related_to_cards[20][4]
                List_of_answering[place_to_add]="and answered false"

        n_question_ge_or+=1

   #Outlook green and orange (combined)
    elif X+Y==1220 or X+Y==1310 or X+Y==1270 or X+Y==1260 or X+Y==290 or X+Y==330 or X+Y==345 or X+Y==385:
        SENTENCE="Outlook, recieved new letter"
        title="Outlook"
        if sounds==True:
            pygame.mixer.music.load('Outlook.ogg')
            pygame.mixer.music.play(0)
        if n_event_outlook==1:
            mesage=msgbox(msg="Robin MERINE\n08.02.2021, 10:26\nDear students,\nI hope this email finds you well as I want to conclude the last events regarding your final physics examination.\nAs you may already know,\nI have exceptionally increased the average by two points after some reflexion\n\n You get 2 extra points!", title=title, ok_button="OK")
            x+=2
            List_of_answering[place_to_add]="and gained 2 points from Robin"
        elif n_event_outlook==2:
            mesage=msgbox(msg="Samer El Zant\n08.02.2021, 17:52\nDear all,\nWhat is the explanation that PW2 for you three is the same with same errors?\n\n You've got caught on plagiarism so you lose 1.5 points!", title=title, ok_button="OK")
            x-=1.5
            List_of_answering[place_to_add]="and accused in plagiarism"
        elif n_event_outlook==3:
            mesage=msgbox(msg="Narmin Dadashova\n30.04.2021, 16:28\nDear Students,Please be informed that I organize an online meeting for you.\nIf you have any concerns or comments about your education you can join in the link below.\nhttps://bbb.unistra.fr/b/lat-yzg-v34", title=title, ok_button="OK")
            List_of_answering[place_to_add]="and wrote concern about physics final"
        elif n_event_outlook==4:
            mesage=msgbox(msg="Narmin Dadashova\n15.02.2021, 12:51\nDear students, please be informed that starting from the next week you have pw sessions, and it’s necessary to buy lab coats.", title=title, ok_button="OK")
            List_of_scholarships[turn_of_player-1]-=40
            List_of_answering[place_to_add]="and bought lab coat"
        elif n_event_outlook==5:
            mesage=msgbox(msg="Narmin Dadashova\n23.04.2021, 12:34\nDear Students,Hope you are doing well. According to the decision of the Cabinet of Ministers, in order to ensure the sequence of working and rest days in the territory of the Republic of Azerbaijan, the places of rest on May 8 and May 16 were changed to working days of May 11 and 12, 2021, respectively. Take a rest.", title=title, ok_button="OK")
            List_of_answering[place_to_add]="and took a rest"
        elif n_event_outlook==6:
            mesage=msgbox(msg="Narmin Dadashova\n15.02.2021, 12:51\nDear students, please be informed that starting from the next week you have pw sessions, and it’s necessary to buy protective glasses.", title=title, ok_button="OK")
            List_of_scholarships[turn_of_player-1]-=30
            List_of_answering[place_to_add]="and bought protective glasses"
        n_event_outlook+=1
        
   #Choose subject 
    elif  X+Y==130 or X+Y==80 or X+Y==135 or X+Y==185:
        SENTENCE="Choose subject"
        title="Choose subject"
        subjects = ["Chemistry","Physics","Math analysis","Algebra"]
        button=buttonbox(f"Choose subject", title=title, choices=subjects)
        list_chem={
        1:"Which one of the following is not a buffer solution?"
        ,2:"At 25 degrees C the pH value of a solution is 6. The solution is"
        ,3:"About buffer solution which is correct?"
        ,4:"Which of the following curves represents the titration of a strong base by a strong acid?"
        ,5:"Which of the following is an indication of when a reaction has reached the equivalence point"
        ,6:"1M of a weak acid HZ with Ka=10e-8 equilibrates in water according to the equation HZ + H2O à H3O+ + Z-. What is the pH of the solution at equilibrium?"
        }
        list_phys={
        1:"Snell-Descartes law rules the phenomenon of:\n 1) reflection\n 2) refraction\n 3) transmission\n 4) absorption"
        ,2:"Find the gradient of the function 2sin x + 9cos y"
        ,3:"Which of the following is not one part (type,category) of electromagnetic spectrum?"
        ,4:"Which of the following are always vectorial quantities?\n1) Distance\n2) Force\n3) Volumetric mass\n4) Instant speed\n5) Length\n6) Acceleration\n7) Displacement\n8) Velocity"
        ,5:"The vector vec(Ex+Ey+Ez) is a unit vector?"
        ,6:"Which statement is true?"
        }
        list_math={
        1:"Let f be defined by f(x) = √(2x + 1). Using the definition of the derivative, calculate the derivative of the function f at x = 3."
        ,2:"Find the following limit:"
        ,3:"Determine where the following function is discontinuous:"
        ,4:"Find all vertical asymptotes and horizontal asymptotes of the function:"
        ,5:"Calculate:"
        ,6:"Calculate:"
        }
        list_alg={
        1:"In how many ways can the letters of the word ABACUS be rearranged such that the vowels always appear together?"
        ,2:"In how many ways can 5 letters be posted in 3 post boxes, if any number of letters can be posted in all of the three post boxes?"
        ,3:"Find the sum of all positive integers x such that there is a positive integer y satisfying 9x2−4y2=2021. Hint: 2021=43×47"
        ,4:"Calculate: gcd(a + b; lcm(a; b))"
        ,5:"Calculate φ(φ(78))=?\nwhere φ represents the Euler's Totient function."
        ,6:"Find the natural number x for which φ(x)=4\nwhere φ(x) represent Euler's Totient \nfunction for the natural number x."
        }

        if button==subjects[0]:
            if choose_chem==1:
                answers_chem_1 = ["A)H2S + KHS","B)C6HNH2 + C6H5NH3+Br","C)H2CO3 + KHCO3","D)KClO4 + HClO4"]
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_1)
                if button==answers_chem_1[3]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_chem==2:
                answers_chem_2 = ["A) Basic","B) Acidic","C) Neutral","D) Both b and c"]
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_2)
                if button==answers_chem_2[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_chem==3:
                answers_chem_3 = ["A) 1,3","B) 2,3","C) 1,2","D) All of the above"]
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_3)
                if button==answers_chem_3[3]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_chem==4:
                answers_chem_4 = ['choose1.png','choose2.png','choose3.png','choose4.png']
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_4)
                if button==answers_chem_4[2]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_chem==5:
                answers_chem_5 = ["A) Moles of titrant equals moles of analyte","B) When the volume of both reactants are equal","C) When there is a color change","D) The end point of a titration"]
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_5)
                if button==answers_chem_5[0]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_chem==5:
                answers_chem_5 = ["A) 7","B) 6","C) 4","D) 2"]
                button=buttonbox(f"{list_chem[choose_chem]}", title=title, choices=answers_chem_5)
                if button==answers_chem_5[2]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            choose_chem+=1
 
        elif button==subjects[1]:
            if choose_physics==1:
                answers_ph_1 = ["A) Only 1","B) Only 2","C) 2,3","D) 1,2","E) 2,4"]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_1)
                if button==answers_ph_1[3]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_physics==2:
                answers_ph_2 = ["A) 2cos x i – 9sin y j","B) 2cos x i + 9sin y j","C) 2sin x i + 9cos y j","D) 2sin x i – 9cos y j","E) 2sin (2x) i + 9cos (9y) j"]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_2)
                if button==answers_ph_2[0]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_physics==3:
                answers_ph_3 = ["A) Ultraviolet Waves","B) Infrared Waves","C) Radio Waves","D)X-ray waves","E) Transverse waves"]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_3)
                if button==answers_ph_3[4]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_physics==4:
                answers_ph_4 = ["A) 1,3,4,5","B) 2,4,6,8","C) 1,2,6,8","D) 2,6,7,8","E) 2,3,5,6"]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_4)
                if button==answers_ph_4[3]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_physics==5:
                answers_ph_5 = ["A) True","B) False"]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_5)
                if button==answers_ph_5[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            elif choose_physics==6:
                answers_ph_6 = ["A) The sum of all the forces exerted on a system\nis equal to the mass of the system times\nthe acceleration of its center of mass."
                ,"B) The sum of all the external forces exerted on a system\nis equal to the mass of the system times\nthe acceleration of its center of mass."
                ,"C) The sum of all the internal forces exerted on a system\nis equal to the mass of the system times\nthe acceleration of its center of mass."]
                button=buttonbox(f"{list_phys[choose_physics]}", title=title, choices=answers_ph_6)
                if button==answers_ph_6[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"


            choose_physics+=1


        elif button==subjects[2]:
            if choose_math==1:
                answers_ma_1 = ["A) √7","B)1/ √7","C) 1","D) 1/7"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_1)
                if button==answers_ma_1[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_math==2:
                answers_ma_2 = ["A) 2/3","B) 4/3","C) 3/2","D) 3/8"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_2,image='mat_choose2.png')
                if button==answers_ma_2[2]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_math==3:
                answers_ma_3 = ["A) -1.05","B) -0.53","C) 0.97","D) 2.47","E) -2.95"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_3,image='mat_choose3.png')
                if button==answers_ma_3[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
                

            elif choose_math==4:
                answers_ma_4 = ["A) Horizontal Asymptotes: None\nVertical Asymptotes: x=0 and x=2","B) Horizontal Asymptotes: y=3\nVertical Asymptotes: x=0 and x=−1","C) The horizontal asymptote is y=−2 \nThe vertical asymptotes are x=0 and x=2","D) Horizontal Asymptotes: y=3\nVertical Asymptotes: x=0","E) The horizontal asymptote is y=2\nThe vertical asymptotes is x=2"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_4,image='mat_choose4.png')
                if button==answers_ma_4[2]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_math==5:
                answers_ma_5 = ["A) ∞","B) 0","C) 2","D) -∞"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_5,image='mat_choose5.png')
                if button==answers_ma_5[0]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_math==6:
                answers_ma_6 = ["A) -3","B) 6","C) 0","D) 2","E) -5"]
                button=buttonbox(f"{list_math[choose_math]}", title=title, choices=answers_ma_6,image='mat_choose6.png')
                if button==answers_ma_6[4]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            choose_math+=1

        elif button==subjects[3]:

            if choose_alg==1:
                answers_alg_1 = ["A) 6!2!","B) 3!×3!","C) 4!2!","D) 4!×3!/2!","E) 3!×3!/2!"]
                button=buttonbox(f"{list_alg[choose_alg]}", title=title, choices=answers_alg_1)
                if button==answers_alg_1[1]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"
                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_alg==2:
                answers_alg_2 = ["A) 5 C 3","B) 5 P 3","C) 5^3","D) 3^5","E) 2^5"]
                button=buttonbox(f"{list_alg[choose_alg]}", title=title, choices=answers_alg_2)
                if button==answers_alg_2[3]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"

                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_alg==3:
                ent=enterbox(msg=f"{list_alg[choose_alg]}", title=title)
                if ent=="15":
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"

                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"


            elif choose_alg==4:
                answers_alg_4 = ["A) 1","B) ab","C) lcm(a; b)","D) b","E) a","F) gcd(a; b)"]
                button=buttonbox(f"{list_alg[choose_alg]}", title=title, choices=answers_alg_4)
                if button==answers_alg_4[5]:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"

                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"
            
            elif choose_alg==5:
                ent=enterbox(msg=f"{list_alg[choose_alg]}", title=title)
                if ent=="8":
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"

                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            elif choose_alg==6:
                ent=enterbox(msg=f"{list_alg[choose_alg]}", title=title)
                if ent=="5":
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1 point", title=title, ok_button="OK")
                    x+=1
                    List_of_answering[place_to_add]="and answered true"

                else:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1 point", title=title, ok_button="OK")
                    x-=1
                    List_of_answering[place_to_add]="and answered false"

            choose_alg+=1

   #? yellow and red (combined)
    elif X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265 or X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
        if sounds==True:
            pygame.mixer.music.load('Question_mark.ogg')
            pygame.mixer.music.play(0)
        SENTENCE="Event"
        title="Event"
        list_event={
        1:"What is your comment on the below C statement?\nsigned int *p=(int*)malloc(sizeof(unsigned int));"
        ,2:"A 10.0 kg mass sliding on a frictionless horizontal surface at 7.00 m/s hits a spring that is attached to a wall.\nThe spring has a spring constant of 5000 N/m.\nDetermine the maximum compression of the spring (in m).\nDon't write the unit, give the answer with 3 sig fig (in m)."
        ,3:"Three hardcover books and 5 paperbacks are placed on a shelf. How many ways can the books be arranged if all the hardcover books must be together and all the paperbacks must be together?"
        }
        if n_event==1:
            list_cs_q=["A) Improper type casting","B) Would throw Runtime error","C) Memory will be allocated but cannot hold an int value in the memory","D) No issue with statement"]
            button=buttonbox(f"{list_event[n_event]}", title=title, choices=list_cs_q)
            if button==list_cs_q[3]:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"

            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"

        elif n_event==2:
            ent=enterbox(msg=f"{list_event[n_event]}", title=title)
            if ent=="0.313":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"

            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"

        elif n_event==3:
            ent=enterbox(msg=f"{list_event[n_event]}", title=title)
            if ent=="1440":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"

            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==4:
            ent=enterbox(msg="For the complex number z satisfying |z−1|+z=2+3i find 2–√|z|", title=title)
            if ent=="3√2":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==5:
            ent=enterbox(msg="Find the distance from the origin to a given point A(6,450,8) with the cylindrical coordinates", title=title)
            if ent=="10":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==6:
            ent=enterbox(msg="Calculate the molar concentration of a 30 % HCl solution (% weight). Do not forget the units.\nData for this 30 % solution: d= 1.149 g.mL-1\nM(H)= 1.01 g.mol-1\nM(Cl)= 35.45 g.mol-1", title=title)
            if ent=="9.7 mol/l" or ent=="9.7 mol/L":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==7:
            ent=enterbox(msg="The density of iron is 7.874 g/cm3. Convert it into SI Units (don't forget to mention the unit in your answer).")
            if ent=="7874 kg/m^3":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==8:
            ent=enterbox(msg="A tar (tar-musical instrument) string vibrates at a frequency of 660 Hz. A  point at its center moves in simple harmonic motion with an amplitude of 2.0 mm and  a phase angle of zero. What is the maximum value of the magnitude of the acceleration of the center of the string?", title=title)
            if ent=="3,4*10^4 m/s^2" or ent=="34000 m/s^2":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==9:
            ent=enterbox(msg="Find the scalar product of vectors 2a⃗ −b⃗  and a⃗ +3b⃗ , if it's known that |a⃗ |=4, |b⃗ |=5 and angle between vectors a⃗  and b⃗  equal to π/3", title=title)
            if ent=="7":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        elif n_event==10:
            ent=enterbox(msg="Find the area of a parallelogram with sides a⃗ +3b⃗ ,3a⃗ +3b⃗  if it's known that |a⃗ |=|b⃗ |=1 and angle between vectors a⃗  and b⃗  is 300", title=title)
            if ent=="3":
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 1.5 points", title=title, ok_button="OK")
                    x+=1.5
                    List_of_answering[place_to_add]="and answered true"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('correct.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Great! Your answer is correct, you get 0.75 points", title=title, ok_button="OK")
                    x+=0.75
                    List_of_answering[place_to_add]="and answered true"
            else:
                if X+Y==1200 or X+Y==1290 or X+Y==1305 or X+Y==1265:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 1.5 points", title=title, ok_button="OK")
                    x-=1.5
                    List_of_answering[place_to_add]="and answered false"
                elif X+Y==765 or X+Y==680 or X+Y==746 or X+Y==780:
                    if sounds==True:
                        pygame.mixer.music.load('wrong.ogg')
                        pygame.mixer.music.play(0)
                    mesage=msgbox(msg="Your answer is wrong, you lose 0.75 points", title=title, ok_button="OK")
                    x-=0.75
                    List_of_answering[place_to_add]="and answered false"
        n_event+=1

   #Canteen
    elif X+Y==935 or X+Y==810 or X+Y==845 or X+Y==880:
        SENTENCE="Canteen"
        title="Canteen"
        mesage=msgbox(msg="For the entry to canteen from your money was subtracted 30 AZN", title=title, ok_button="OK")
        List_of_scholarships[turn_of_player-1]-=30
        List_of_answering[place_to_add]="and drank tea"

   #Rest day
    elif X+Y==941 or X+Y==980 or X+Y==940 or X+Y==981:
        SENTENCE="Rest day"
        title="Rest day"
        mesage=msgbox(msg="Take a rest before difficult questions!", title=title, ok_button="OK")
        List_of_answering[place_to_add]="and had a rest"
   
   #Beggining
    elif X+Y==1620 or X+Y==1711 or X+Y==1760 or X+Y==1680:
        SENTENCE="Beggining"
        List_of_answering[place_to_add]="and gain scholarship"
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    List_of_times[place_to_add]=current_time
    name=name+" entered"
    List_of_names[place_to_add]=name
    List_of_SENTENCES[place_to_add]=SENTENCE
    place_to_add+=1
    clicked_once=False
    
    if turn_of_player==1:
        List_of_average_points[0]=x
    elif turn_of_player==2:
        List_of_average_points[1]=x
    elif turn_of_player==3:
        List_of_average_points[2]=x
    elif turn_of_player==4:
        List_of_average_points[3]=x

    Rect_color_change()

# function related to upgrading cards
def buying_upgrading(turn_of_player,x1,y1,x2,y2,x3,y3,x4,y4):
    global place_to_add, Everything_related_to_cards, clicked_once

    SENTENCE=""
    name=""
    clicked_once=False

    if place_to_add==6:
        place_to_add=0

    if turn_of_player==1:
        name=name+List_of_NAMES[0]
        X=x1
        Y=y1
    elif turn_of_player==2:
        name=name+List_of_NAMES[1]
        X=x2
        Y=y2
    elif turn_of_player==3:
        name=name+List_of_NAMES[2]
        X=x3
        Y=y3
    elif turn_of_player==4:
        name=name+List_of_NAMES[3]
        X=x4
        Y=y4

    # sample of the text for players' history
    if X+Y==1520 or X+Y==1620 or X+Y==1570 or X+Y==1571:
        SENTENCE=SENTENCE+"Chemistry, zone:Green"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==586 or X+Y==545 or X+Y==531 or X+Y==490:
        SENTENCE=SENTENCE+"Chemistry, zone:Orange"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==455 or X+Y==370 or X+Y==435 or X+Y==470:
        SENTENCE=SENTENCE+"Physics, zone:Yellow"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1510 or X+Y==1600 or X+Y==1575 or X+Y==1615:
        SENTENCE=SENTENCE+"Physics, zone:Red"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==565 or X+Y==480 or X+Y==535 or X+Y==570:
        SENTENCE=SENTENCE+"Math analysis, zone:Yellow"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1100 or X+Y==1190 or X+Y==1165 or X+Y==1205:
        SENTENCE=SENTENCE+"Math analysis, zone:Red"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1015 or X+Y==1110 or X+Y==1070 or X+Y==1060:
        SENTENCE=SENTENCE+"French, zone:Green"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==355 or X+Y==270 or X+Y==335 or X+Y==371:
        SENTENCE=SENTENCE+"French, zone:Yellow"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif  X+Y==1311 or X+Y==1400 or X+Y==1365 or X+Y==1405:
        SENTENCE=SENTENCE+"French, zone:Red"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1420 or X+Y==1521 or X+Y==1470 or X+Y==1471:
        SENTENCE=SENTENCE+"CS, zone:Green"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1000 or X+Y==1090 or X+Y==1065 or X+Y==1105:
        SENTENCE=SENTENCE+"General question, zone:Red"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==185 or X+Y==230 or X+Y==245 or X+Y==285:
        SENTENCE=SENTENCE+"Algebra, zone:Orange"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1411 or X+Y==1500 or X+Y==1475 or X+Y==1515:
        SENTENCE=SENTENCE+"Algebra, zone:Red"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==665 or X+Y==580 or X+Y==645 or X+Y==681:
        SENTENCE=SENTENCE+"English, zone:Yellow"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==590 or X+Y==641 or X+Y==646 or X+Y==695:
        SENTENCE=SENTENCE+"English, zone:Orange"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1320 or X+Y==1410 or X+Y==1370 or X+Y==1360:
        SENTENCE=SENTENCE+"Plagiarism, zone:Green"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==255 or X+Y==170 or X+Y==235 or X+Y==261:
        SENTENCE=SENTENCE+"Plagiarism, zone:Yellow"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==1120 or X+Y==1210 or X+Y==1170 or X+Y==1160:
        SENTENCE=SENTENCE+"Geometry, zone:Green"
        List_of_SENTENCES[place_to_add]=SENTENCE
    elif X+Y==690 or X+Y==740 or X+Y==745 or X+Y==795:
        SENTENCE=SENTENCE+"Geometry, zone:Orange"
        List_of_SENTENCES[place_to_add]=SENTENCE
    
    
    
    
    
    if Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][0]==0:
        if int(Dict_of_prices.get(X+Y))<=List_of_scholarships[turn_of_player-1]:
            BUTTON=buttonbox("Do you want to buy this cell for "+ Dict_of_prices.get(X+Y) +" AZN?", "UFAZ monopoly",["Yes", "No"])
            if BUTTON=="Yes":
                if sounds==True:
                    pygame.mixer.music.load('cash.ogg')
                    pygame.mixer.music.play(0)
                    List_of_scholarships[turn_of_player-1]=List_of_scholarships[turn_of_player-1]-int(Dict_of_prices.get(X+Y))
                    time.sleep(1)
                Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][0]=1
                List_of_bought_cards_by_players[turn_of_player-1].append(Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][6])
                List_of_bought_cards_by_players_string_and_position[turn_of_player-1][0].append(Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][5])
                List_of_bought_cards_by_players_string_and_position[turn_of_player-1][1].append(Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][7])
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                List_of_times[place_to_add]=current_time
                name=name+" bought"
                List_of_names[place_to_add]=name
                List_of_answering[place_to_add]=" "
                place_to_add+=1
                questions(turn_of_player,X,Y)
            else:
                questions(turn_of_player,X,Y)
        else:
            questions(turn_of_player,X,Y)

    elif Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][1]==0:
        if Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][6] not in List_of_bought_cards_by_players[turn_of_player-1]:
            questions(turn_of_player, X, Y)
        else:
            if int(Dict_of_prices_for_first_uprading.get(X+Y))<=List_of_scholarships[turn_of_player-1]:
                but=buttonbox("Do you want to upgrade this cell for "+ Dict_of_prices_for_first_uprading.get(X+Y) +" AZN?", "UFAZ monopoly",["Yes", "No"])
                if but=="Yes":
                    if sounds==True:
                        pygame.mixer.music.load('cash.ogg')
                        pygame.mixer.music.play(0)
                        List_of_scholarships[turn_of_player-1]=List_of_scholarships[turn_of_player-1]-int(Dict_of_prices_for_first_uprading.get(X+Y))
                        time.sleep(1)
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][1]=1
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][4]+=0.25
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][3]="With 1 upgrade"
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    List_of_times[place_to_add]=current_time
                    name=name+" Upgraded"
                    List_of_names[place_to_add]=name
                    List_of_answering[place_to_add]=" "
                    place_to_add+=1

                    questions(turn_of_player,X,Y)
                else:
                    questions(turn_of_player,X,Y)
            else:
                questions(turn_of_player,X,Y)

    elif Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][2]==0:
        if Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][6] not in List_of_bought_cards_by_players[turn_of_player-1]:
            questions(turn_of_player, X, Y)
        else:
            if int(Dict_of_prices_for_second_uprading.get(X+Y))<=List_of_scholarships[turn_of_player-1]:
                but=buttonbox("Do you want to upgrade one more time this cell for "+ Dict_of_prices_for_second_uprading.get(X+Y) +" AZN?", "UFAZ monopoly",["Yes", "No"])
                if but=="Yes":
                    if sounds==True:
                        pygame.mixer.music.load('cash.ogg')
                        pygame.mixer.music.play(0)
                        List_of_scholarships[turn_of_player-1]=List_of_scholarships[turn_of_player-1]-int(Dict_of_prices_for_second_uprading.get(X+Y))
                        time.sleep(1)
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][1]=1
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][4]+=0.25
                    Everything_related_to_cards[ List_of_cells[turn_of_player-1] ][3]="With 2 upgrade"
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    List_of_times[place_to_add]=current_time
                    name=name+" Upgraded twice"
                    List_of_names[place_to_add]=name
                    List_of_answering[place_to_add]=" "
                    place_to_add+=1
                    questions(turn_of_player,X,Y)
                else:
                    questions(turn_of_player,X,Y)
            else:
                questions(turn_of_player,X,Y)        
    else:
        questions(turn_of_player, X, Y)
        
#players' names depending on number of players that was chosen
def interface(number_of_players):
    if number_of_players==2:
        interface=multenterbox("Enter your names", "UFAZ monopoly", fields=["Name of player1:", "Name of player2:"])
        List_of_NAMES.extend([ interface[0], interface[1] ])
    elif number_of_players==3:
        interface=multenterbox("Enter your names", "UFAZ monopoly", fields=["Name of player1:", "Name of player2:", "Name of player3:"])
        List_of_NAMES.extend([ interface[0], interface[1], interface[2] ])
    elif number_of_players==4:
        interface=multenterbox("Enter your names", "UFAZ monopoly", fields=["Name of player1:", "Name of player2:", "Name of player3:", "Name of player4:"])
        List_of_NAMES.extend([ interface[0], interface[1], interface[2], interface[3] ])
    main(number_of_players)

#function for the game process
def main(num_of_players):
    global turn_of_player_color_change ,number_of_players, number, List_of_current_coordinates, List_of_cells, List_of_bought_cards_by_players, List_of_scholarships, clicked_once, clicked_button_2, sounds
    number_of_players=num_of_players
    clicked_Rules=0
    FPS=120
    start=0
    sound_button_clicked=0
    pygame.font.init()
    font=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 35)    #random number font
    display = pygame.display.set_mode( (1500,950) )   #window coordinates
    pygame.display.update()
    pygame.display.set_caption("UFAZ monopoly")
    run=True
    clock=pygame.time.Clock()
    board=pygame.image.load('monopoly_board.jpg')
    turn_of_player=0
    number2=0
    number1=-2
    font_for_button1=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 24)
    font_text=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 15)
    pygame.mixer.init()
    image_for_sound=sound_on_or_off[0]
    dice_options=[pygame.image.load("dice_1.png"),pygame.image.load("dice_2.png"),pygame.image.load("dice_3.png"), pygame.image.load("dice_4.png"),pygame.image.load("dice_5.png"),pygame.image.load("dice_6.png")]
    while run:                 # main game buttons
        clock.tick(FPS)
        display.fill((255,255,255))
        display.blit(board, (0,0))
        button_1=draw_button(display,1010,455,"Toss a dice",font_for_button1,clicked_once,135,35,None)
        button_2=draw_button(display,1175,455,"History",font_for_button1,clicked_once,135,35,None)
        button_3=draw_button(display,1340,455,"Rules",font_for_button1,clicked_once,135,35,None)
        sound_button=draw_button(display,1433,903,None,None,clicked_once,60,40,image_for_sound)


        #building up interface 

        Dict_coordinates_name_player1={2:(1229, 109), 3:(1229, 109), 4:(1224, 109), 5:(1221, 109), 6:(1215, 109), 7:(1208, 109), 8:(1202, 109)}
        rect_player1= Rect(1085, 20, 310, 195)
        pygame.draw.rect(display, color1, rect_player1)
        pygame.draw.circle(display, (0,0,0), (1240,65), 40)
        pygame.draw.circle(display, (255,255,255), (1240,65), 37)
        Name_player1=font_text.render(f"{List_of_NAMES[0]}",True,(0,0,0))
        Average_points_player1=font_text.render(f"Average points: {List_of_average_points[0]}", True, (0,0,0))
        Money_player1=font_text.render(f"Money: {List_of_scholarships[0]}", True, (0,0,0))
        check_deck_player1=draw_button(display,1200,180,"Check deck",font_text,clicked_once,84,25,None)
        display.blit(pygame.image.load(f"{List_of_chose_players[0]}"), (1208, 33))
        display.blit(Name_player1, Dict_coordinates_name_player1.get(len(List_of_NAMES[0])))
        display.blit(Average_points_player1, (1175, 130))
        display.blit(Money_player1, (1201, 154))
        if check_deck_player1==True:
            show_cards_of_player(List_of_bought_cards_by_players[0], 0)


        if number_of_players>=3:
            Dict_coordinates_name_player3={2:(1229, 329), 3:(1229, 329), 4:(1224, 329), 5:(1221, 329), 6:(1215, 329), 7:(1208, 329), 8:(1202, 329)}
            rect_player3= Rect(1085, 240, 310, 195)
            pygame.draw.rect(display, color3, rect_player3)
            pygame.draw.circle(display, (0,0,0), (1240,285), 40)
            pygame.draw.circle(display, (255,255,255), (1240,285), 37)
            Name_player3=font_text.render(f"{List_of_NAMES[2]}",True,(0,0,0))
            Average_points_player3=font_text.render(f"Average points: {List_of_average_points[2]}", True, (0,0,0))
            Money_player3=font_text.render(f"Money: {List_of_scholarships[2]}", True, (0,0,0))
            check_deck_player3=draw_button(display,1200,400,"Check deck",font_text,clicked_once,84,25,None)
            display.blit(pygame.image.load(f"{List_of_chose_players[2]}"), (1208, 253))
            display.blit(Name_player3, Dict_coordinates_name_player3.get(len(List_of_NAMES[2])))
            display.blit(Average_points_player3, (1175, 350))
            display.blit(Money_player3, (1201, 374))
            if check_deck_player3==True:
                show_cards_of_player(List_of_bought_cards_by_players[2], 2)
            if number_of_players==4:
                Dict_coordinates_name_player4={2:(1229, 601), 3:(1229, 601), 4:(1224, 601), 5:(1221, 601), 6:(1215, 601), 7:(1208, 601), 8:(1202, 601)}
                rect_player4= Rect(1085, 512, 310, 195)
                pygame.draw.rect(display, color4, rect_player4)
                pygame.draw.circle(display, (0,0,0), (1240,557), 40)
                pygame.draw.circle(display, (255,255,255), (1240,557), 37)
                Name_player4=font_text.render(f"{List_of_NAMES[3]}",True,(0,0,0))
                Average_points_player4=font_text.render(f"Average points: {List_of_average_points[3]}", True, (0,0,0))
                Money_player4=font_text.render(f"Money: {List_of_scholarships[3]}", True, (0,0,0))
                check_deck_player4=draw_button(display,1200,672,"Check deck",font_text,clicked_once,84,25,None)
                display.blit(pygame.image.load(f"{List_of_chose_players[3]}"), (1208, 525))
                display.blit(Name_player4, Dict_coordinates_name_player4.get(len(List_of_NAMES[3])))
                display.blit(Average_points_player4, (1175, 622))
                display.blit(Money_player4, (1201, 646))
                if check_deck_player4==True:
                    show_cards_of_player(List_of_bought_cards_by_players[3], 3)

        pygame.draw.rect(display, (0,0,0), pygame.Rect(985, 440, 715, 5))
        pygame.draw.rect(display, (0,0,0), pygame.Rect(985, 502, 715, 5))

        Dict_coordinates_name_player2={2:(1229, 821), 3:(1229, 821), 4:(1224, 821), 5:(1221, 821), 6:(1215, 821), 7:(1208, 821), 8:(1202, 821)}
        rect_player2= Rect(1085, 732, 310, 195)
        pygame.draw.rect(display, color2, rect_player2)
        pygame.draw.circle(display, (0,0,0), (1240,777), 40)
        pygame.draw.circle(display, (255,255,255), (1240,777), 37)
        Name_player2=font_text.render(f"{List_of_NAMES[1]}",True,(0,0,0))
        Average_points_player2=font_text.render(f"Average points: {List_of_average_points[1]}", True, (0,0,0))
        Money_player2=font_text.render(f"Money: {List_of_scholarships[1]}", True, (0,0,0))
        check_deck_player2=draw_button(display,1200,892,"Check deck",font_text,clicked_once,84,25,None)
        display.blit(pygame.image.load(f"{List_of_chose_players[1]}"), (1208, 745))
        display.blit(Name_player2, Dict_coordinates_name_player2.get(len(List_of_NAMES[1])))
        display.blit(Average_points_player2, (1175, 842))
        display.blit(Money_player2, (1201, 866))
        if check_deck_player2==True:
            show_cards_of_player(List_of_bought_cards_by_players[1], 1)

        # tossing a dice 
        if button_1==True:
            number=random.randint(4,6)
            number1, number2=number, number
            turn_of_player+=1
            turn_of_player_color_change+=1
            if sounds==True:
                pygame.mixer.music.load('dice_shuffle.ogg')
                pygame.mixer.music.play(0)
            random_number_1, random_number_2, random_number_3, random_number_4, random_number_5, random_number_6=random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)
            random_x1, random_x2, random_x3, random_x4, random_x5, random_x6, random_x7=random.randint(188,712), random.randint(188,712), random.randint(188,712), random.randint(188,712), random.randint(188,712), random.randint(188,712), random.randint(188,712)
            random_y1, random_y2, random_y3, random_y4, random_y5, random_y6, random_y7=random.randint(164,702), random.randint(164,702), random.randint(164,702), random.randint(164,702), random.randint(164,702), random.randint(164,702), random.randint(164,702)
            clicked_once=True
            start = time.time()

        if sound_button==True:
            sound_button_clicked+=1
            if sound_button_clicked%2==0:
                image_for_sound=image_for_sound=sound_on_or_off[0]
                sounds=True
            else:
                image_for_sound=sound_on_or_off[1]
                sounds=False
        
        if button_3==True:
            Rules(False)
        
        if button_2==True:
            History()


        #displaying pictures of dice 
        finish1=time.time()
        if 0<finish1-start<0.5:
            display.blit(dice_options[random_number_1-1], (random_x7,random_y7))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if 0.5<finish1-start<1:
            display.blit(dice_options[random_number_2-1], (random_x1,random_y1))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if 1<finish1-start<1.5:
            display.blit(dice_options[random_number_3-1], (random_x2,random_y2))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if 1.5<finish1-start<2:
            display.blit(dice_options[random_number_4-1], (random_x3,random_y3))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if 2<finish1-start<2.5:
            display.blit(dice_options[random_number_5-1], (random_x4,random_y4))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if 2.5<finish1-start<3:
            display.blit(dice_options[random_number_6-1], (random_x5,random_y5))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if finish1-start>3:
            if number!='':
                display.blit(dice_options[number-1],  (random_x6,random_y6))
            for i in range(number_of_players):
                players(display,List_of_current_coordinates, i)

        if List_of_current_coordinates[turn_of_player-1][0]==coordinates_for_players[turn_of_player-1][0][0]:
            if List_of_average_points[turn_of_player-1]<10:
                end(List_of_average_points, number_of_players)
                run=False

        if finish1-start>3:
            if number1!=-2:
                if number1!=-1:
                    if number1==0:
                        if List_of_current_coordinates[turn_of_player-1][0]==coordinates_for_players[turn_of_player-1][0][0]:
                            if sounds==True:
                                pygame.mixer.music.load('Money_gaining.wav')
                                pygame.mixer.music.play(0)
                            if 10<=List_of_average_points[turn_of_player-1]<11.5:
                                List_of_scholarships[turn_of_player-1]-=70
                            elif 11.5<=List_of_average_points[turn_of_player-1]<13.5:
                                List_of_scholarships[turn_of_player-1]-=110
                            elif List_of_average_points[turn_of_player-1]>=13.5:
                                List_of_scholarships[turn_of_player-1]-=130
                        List_of_cells[turn_of_player-1]-=1
                    List_of_cells[turn_of_player-1]+=1
                    if List_of_cells[turn_of_player-1]==28:
                        List_of_cells[turn_of_player-1]-=28
                    time.sleep(0.35)
                    List_of_current_coordinates[turn_of_player-1][0]=coordinates_for_players[turn_of_player-1][ List_of_cells[turn_of_player-1] ][0]
                    List_of_current_coordinates[turn_of_player-1][1]=coordinates_for_players[turn_of_player-1][ List_of_cells[turn_of_player-1] ][1]
                    time.sleep(0.35)
                    if List_of_current_coordinates[turn_of_player-1][0]!=coordinates_for_players[turn_of_player-1][0][0]:
                        if run==True:
                            if sounds==True:
                                pygame.mixer.music.load('step.ogg')
                                pygame.mixer.music.play(0)
                    if List_of_current_coordinates[turn_of_player-1][0]==coordinates_for_players[turn_of_player-1][0][0]:
                        if 10<=List_of_average_points[turn_of_player-1]<11.5:
                            List_of_scholarships[turn_of_player-1]+=70
                        elif 11.5<=List_of_average_points[turn_of_player-1]<13.5:
                            List_of_scholarships[turn_of_player-1]+=110
                        elif List_of_average_points[turn_of_player-1]>=13.5:
                            List_of_scholarships[turn_of_player-1]+=130
                    number1-=1
            finish=time.time()
        

        if 5.1<finish-start<5.3: #dice=1
            if number2==1:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])

        elif 5.8<finish-start<6: #dice=2            
            if number2==2:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])
        
        elif 6.5<finish-start<6.7: #dice=3
            if number2==3:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])

        elif 7<finish-start<7.2: #dice=4
            if number2==4:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])
        
        elif 7.7<finish-start<7.9: #dice=5
            if number2==5:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])

        elif 8.3<finish-start<8.5: #dice=6
            if number2==6:
                buying_upgrading(turn_of_player, List_of_current_coordinates[0][0], List_of_current_coordinates[0][1], List_of_current_coordinates[1][0], List_of_current_coordinates[1][1],List_of_current_coordinates[2][0],List_of_current_coordinates[2][1],List_of_current_coordinates[3][0],List_of_current_coordinates[3][1])
       
        if number_of_players==2:
            if turn_of_player==3:
                turn_of_player=1
            List_of_current_coordinates[2][0]=0
            List_of_current_coordinates[2][1]=0
            List_of_current_coordinates[3][0]=0
            List_of_current_coordinates[3][1]=0
            List_of_average_points[2]=0
            List_of_average_points[3]=0
        elif number_of_players==3:
            if turn_of_player==4:
                turn_of_player=1
            List_of_current_coordinates[3][0]=0
            List_of_current_coordinates[3][1]=0
            List_of_average_points[3]=0
        elif number_of_players==4:
            if turn_of_player==5:
                turn_of_player=1
        
        for i in range(len(List_of_average_points)):
            if List_of_average_points[i]>20:
                List_of_average_points[i]=20

        for i in range(len(List_of_scholarships)):
            if List_of_scholarships[i]<0:
                List_of_scholarships[i]=0
        
        if run==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

        pygame.display.update()

    pygame.quit()

#choosing number of players
def beginning():
    ent=enterbox("How many players will play in game?(Possible variants: 2-4)", title="UFAZ monopoly")
    while ent!="2" and ent!="3" and ent!="4":
        ent=enterbox("How many players will play in game?(Possible variants:2-4)", title="UFAZ monopoly")
    choose_characters(ent)

#choosing avatar for each player
def choose_characters(number_of_players):
    global List_of_chose_players
    player=1
    number_of_players=int(number_of_players)
    List_of_images=['player1.png','player2.png','player3.png','player4.png','player5.png','player6.png']
    for i in range(number_of_players): 
        choice=buttonbox(msg=f"Player{player}, choose own character:",title="Choose your skin for character",choices=[],images=List_of_images) # adding avatar and removing from list
        List_of_chose_players.append(choice)
        List_of_images.remove(choice)
        player+=1
    interface(number_of_players)

#beggining menu of the game
def menu():
    run=True
    FPS=80
    clock=pygame.time.Clock()
    display = pygame.display.set_mode( (500,500) )   #window coordinates
    pygame.font.init()
    pygame.display.set_caption("UFAZ monopoly")
    Menu=pygame.image.load("Menu.jpg")
    clicked_Rules=0
    font=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 30)
    font1=pygame.font.Font(resource_path(os.path.join(f'{path_new}', 'FreeSansBold.ttf')), 20)
    while run:
        clock.tick(FPS)
        display.blit(Menu, (0,0) )
        button_play=draw_button(display,283,180,"Play",font,False,155,45,None)
        button_rules=draw_button(display,283,240,"Rules",font,False,155,45,None)
        if button_play==True:              # begin the game
            run=False
            pygame.quit()
            beginning()
        if button_rules==True:             # show rules
            Rules(True)

        if run==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            pygame.display.update()
    pygame.quit()
        
menu()