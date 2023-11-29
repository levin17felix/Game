#importing library and modules

from tkinter import *
from tkinter import ttk
from tkinter import font
#import mysql.connector as sqlcon
from sys import exit 

#==============================================================================================================================#
#code for the startup and menu

def loading():#function to show loading
    logo.destroy()#destroys the previous data in the window
    global loading#globalising varaible
    loading=Label(splash_root,text="Loading...",fg="white",bg="black",font=("Book Antiqua",35))#creating text in window
    loading.pack(pady=125)#packing with 125px in y axis
    splash_root.after(2000,Welcome)#after 2000ms the function loading is revoked
    
def Welcome():#function to show welcome
    loading.destroy()#destroys the previous data in the window
    global welcome#globalising varaible
    welcome=Label(splash_root,text="Welcome To Our Project!",fg="white",bg="black",font=("Book Antiqua",70))#creating text in window
    welcome.pack(pady=125)#packing with 125px in y axis
    splash_root.after(2000,GameOptions)#after 2000ms the function loading is revoked
      
splash_root=Tk()#creating window
splash_root.configure(bg='black')#setting bg to black 
splash_root.title("Menu")#setting window title
splash_root.geometry("1250x400")#setting window dimensons
img=PhotoImage(file='logo.png')#loading image
logo=Label(splash_root,image=img)#setting image on the window
logo.pack()#packing entire window
splash_root.after(2000,loading)#after 2000ms the function loading is revoked
    
def GameOptions():#function to show menu
    welcome.destroy()#destroys the previous data in the window
    slabel1=Label(splash_root,text="Click The Game You Would Like To Play:",fg="white",bg="black",font=("Book Antiqua",50))#creating text in window
    slabel2=Label(splash_root,text=" ",bg="black")#creating text in window(empty for space btw the button)
    slabel3=Label(splash_root,text=" ",bg="black")#creating text in window(empty for space btw the button)
    slabel4=Label(splash_root,text=" ",bg="black")#creating text in window(empty for space btw the button)
    buttonFont = font.Font(family='Book Antiqua', size=20) #specifications of button letters
    button1=Button(splash_root,text="Dino",font=buttonFont, command=accept_dino) #creaintg button for dino game
    button2=Button(splash_root,text="Pew Pew",font=buttonFont,command=accept_pewpew)#creaintg button for pewpew
    button3=Button(splash_root,text="Snake",font=buttonFont,command=accept_snake)#creaintg button for snake

    #placing all the labels and buttons
    slabel1.grid(row=0,column=0)
    slabel2.grid(row=6,column=0)
    button1.grid(row=7,column=0,ipadx=40,ipady=10)
    slabel3.grid(row=8,column=0)
    button2.grid(row=9,column=0,ipadx=15,ipady=10)
    slabel4.grid(row=10,column=0)
    button3.grid(row=11,column=0,ipadx=35,ipady=10)
    
#==============================================================================================================================#
#Python -Mysql connection and Scoreboard
    
def creating_pointtable():
    mycon= sqlcon.connect(host="localhost",user="root",passwd="root123")#connecting to mysql
    mycursor = mycon.cursor()#creating cursor object
    mycursor.execute("create database if not exists Game")#creating database
    mycursor.execute("use game")#using database
    mycursor.execute("Create Table if not exists Dino (Player_name varchar(50) ,Player_Score int(8))")#creating table
    mycursor.execute("Create Table if not exists PewPew (Player_name varchar(50) ,Player_Score int(8))")#creating table
    mycursor.execute("Create Table if not exists Snake (Player_name varchar(50) ,Player_Score int(8))")#creating table

def dino_points(name,points):#function for dino points
    mycon= sqlcon.connect(host="localhost",user="root",passwd="root123",database="game")#connecting to mysql
    cursor1 = mycon.cursor()#creating cursor object
    query="insert into Dino values (%s,%s)"#inserting points to table
    tup1=(name ,points)#tuple of data
    cursor1.execute(query,tup1)#executing the query with the tuple of data
    mycon.commit()#making the change in mysql table
    cursor1.execute("select * from Dino order by player_score desc")#taking out the highest 10 scores
    data=cursor1.fetchmany(10)#fetching 10 data
    scoreboard(data)#function to show the data as a table

def pewpew_points(name,points):#function for pewpew points
    mycon= sqlcon.connect(host="localhost",user="root",passwd="root123",database="game")#connecting to mysql
    cursor1 = mycon.cursor()#creating cursor object
    query="insert into PewPew values (%s,%s)"#inserting points to table
    tup1=(name ,points)#tuple of data
    cursor1.execute(query,tup1)#executing the query with the tuple of data
    mycon.commit()#making the change in mysql table
    cursor1.execute("select * from PewPew order by player_score desc")#taking out the highest 10 scores
    data=cursor1.fetchmany(10)#fetching 10 data
    scoreboard(data)#function to show the data as a table

def snake_points(name,points):#function for snake points
    mycon= sqlcon.connect(host="localhost",user="root",passwd="root123",database="game")#connecting to mysql
    cursor1 = mycon.cursor()#creating cursor object
    query="insert into Snake values (%s,%s)"#inserting points to table
    tup1=(name ,points)#tuple of data
    cursor1.execute(query,tup1)#executing the query with the tuple of data
    mycon.commit()#making the change in mysql table
    cursor1.execute("select * from Snake order by player_score desc")#taking out the highest 10 scores
    data=cursor1.fetchmany(10)#fetching 10 data
    scoreboard(data)#function to show the data as a table
    
def scoreboard(data):
    scoreboard = Tk()#creating window
    scoreboard .geometry("620x300")#setting dimensions of window
    scoreboard.title("Scoreboard")#setting title of window
    scoreboard.configure(bg="black")#setting bg of window
    heading=Label(scoreboard,text="Leaderboard",fg="white",bg="black",font=("Book Antiqua",30))#heading
    heading.grid(row=0,column=0)#placing it
    tree = ttk.Treeview(scoreboard , column=("c1", "c2", "c3"), show='headings', height=10)#creating table in window
    tree.grid(row=10,column=0,ipadx=10,ipady=0)#placing it
    tree.column("# 1", anchor=CENTER)#positioning heading for table
    tree.heading("# 1", text="POSITION")#setting up heading for table
    tree.column("# 2", anchor=CENTER)#positioning heading for table
    tree.heading("# 2", text="NAME")#setting up heading for table
    tree.column("# 3", anchor=CENTER)#positioning heading for table
    tree.heading("# 3", text="SCORE")#setting up heading for table
    for i in range(len(data)): #each data is added to the table
        tree.insert('', 'end', text=i+1, values=(i+1,data[i][0],data[i][1]))

#==============================================================================================================================#
#Code for Dino
        
def accept_dino():  #d=dino

    def display_text():#when confirm is pressed dino name is accpeted
        global dino_name
        dino_name= dentry.get()
        
    global droot
    droot = Tk()# creating tkinter window 
    droot.geometry("750x250")#dimensions for window
    droot.title("Accepting Dino")#title for the window
    droot.configure(bg='black')#bg for the window
    dlabel=Label(droot, text="Enter Name", font=("Book Antiqua",25))#creating label
    dlabel.pack(pady = 20)#packing the label
    global dentry #globalising
    dentry= Entry(droot, width= 40)#Create an Entry widget to accept User Input
    dentry.focus_set()#setting focus on this tab
    dentry.pack()#packing the entry
    dbtn1 = Button(droot, text ="Confirm", command=display_text)# Creating confirm button.
    dbtn1.pack(pady = 20)#packing button
    dbtn2 = Button(droot, text ="Continue", command=Dino)#creating continue button
    dbtn2.pack(pady = 5)#packing button

def Dino():
    droot.destroy()#destroying name accepting window
    import pygame
    import os
    import random

	#global constants
    pygame.init()
    SCREEN_HEIGHT=600
    SCREEN_WIDTH=1100
    SCREEN=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	#importing all images required for the game
    RUNNING=[pygame.image.load('DinoRun1.png'),pygame.image.load('DinoRun2.png')]
    JUMPING=pygame.image.load("DinoJump.png")
    DUCKING=[pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
    SMALL_CACTUS=[pygame.image.load("SmallCactus1.png"),pygame.image.load("SmallCactus2.png"),pygame.image.load("SmallCactus3.png")]
    LARGE_CACTUS=[pygame.image.load("LargeCactus1.png"),pygame.image.load("LargeCactus2.png"),pygame.image.load("LargeCactus3.png")]
    BIRD=[pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
    CLOUD=pygame.image.load("Cloud.png")
    BG=pygame.image.load("Track.png")

    class Dinosaur:
        X_POS=80                    #x coordinate of the dinosaur               
        Y_POS=310                  #y coordinate of the dinosaur
        Y_POS_DUCK=340
        JUMP_VEL=8.5        #the velocity with which the dinosaur takes off when jumping
    
        def __init__(self):     #will initialize the dinosaur whenever an object of this class is created
            self.duck_img=DUCKING
            self.run_img=RUNNING
            self.jump_img=JUMPING
            self.dino_duck=False
            self.dino_run=True          #initially the dino is only running
            self.dino_jump=False
            self.step_index=0
            self.jump_vel=self.JUMP_VEL
            self.image=self.run_img[0]                  #hitbox of the dinosaur
            self.dino_rect=self.image.get_rect()    #coordinates of the hitbox
            self.dino_rect.x=self.X_POS
            self.dino_rect.y=self.Y_POS

        def update(self,userInput):     #updates the function with every while loop iteration
            if self.dino_duck:                  #if the dino is ducking
                self.duck()                         #calls the function
            if self.dino_run:                   #if the dino is running
                self.run()                          #calls the function
            if self.dino_jump:                  #if the dino is jumping
                self.jump()                         #calls the function
            if self.step_index>=10:
                self.step_index=0
            if userInput[pygame.K_UP] and not self.dino_jump:       #if the dino user wants to jump  but the dino is not jumping
                self.dino_duck=False
                self.dino_run=False
                self.dino_jump=True
            elif userInput[pygame.K_DOWN] and not self.dino_jump:   #if the user wants to duck but the dino is not jumping
                self.dino_duck=True
                self.dino_run=False
                self.dino_jump=False
            elif not(self.dino_jump or userInput[pygame.K_DOWN]):       #if the user doesn't want to run or jump 
                self.dino_duck=False
                self.dino_run=True
                self.dino_jump=False

        def duck(self):
            self.image=self.duck_img[self.step_index//5]     #variable set to the correspinding image of the dino running
            self.dino_rect=self.image.get_rect()
            self.dino_rect.x=self.X_POS
            self.dino_rect.y=self.Y_POS_DUCK                #when we press the down arrow, the state of the dinosaur is set to duck
            self.step_index+=1              #every 5 units the image is cycled so that the dino looks animated

        def run(self):
            self.image=self.run_img[self.step_index//5]     #variable set to the correspinding image of the dino running
            self.dino_rect=self.image.get_rect()
            self.dino_rect.x=self.X_POS
            self.dino_rect.y=self.Y_POS
            self.step_index+=1              #every 5 units the image is cycled so that the dino looks animated

        def jump(self):
            self.image=self.jump_img        #setting the image as the dinosaur jumping
            if self.dino_jump:
                self.dino_rect.y-=self.jump_vel * 4 #decreasing the y coordinate of the dino so that it moves up
                self.jump_vel-=0.8             #decreasing the velocity as he jumps
            if self.jump_vel<-self.JUMP_VEL:        #if velocity reaches the value -8.5
                 self.dino_jump=False
                 self.jump_vel=self.JUMP_VEL           #resetting the dino jump velocity
             
        def draw(self, SCREEN):
            SCREEN.blit(self.image,(self.dino_rect.x, self.dino_rect.y)) #blits the dino onto the screen

    class Cloud:
        def __init__(self):
            self.x=SCREEN_WIDTH+random.randint(800,1000)    #coordinates of the cloud 
            self.y=random.randint(50,100)
            self.image=CLOUD        #directs to the directory containing the image of the cloud
            self.width=self.image.get_width()   #gets the width of the image of the cloud

        def update(self):
            self.x-=game_speed
            if self.x<-self.width:
                self.x=SCREEN_WIDTH+random.randint(2500,3000)       #distance intervals for cloud on x axis
                self.y=random.randint(50,100)                                   #distance intervals for cloud on y axis
    
        def draw(self,SCREEN):
            SCREEN.blit(self.image,(self.x,self.y))

    class Obstacle():
        def __init__(self,image,type):
            self.image=image
            self.type=type
            self.rect=self.image[self.type].get_rect()      #gets the coordinates of the rectangle of the image
            self.rect.x=SCREEN_WIDTH

        def update(self):
            self.rect.x-=game_speed
            if self.rect.x<-self.rect.width:     #removes the obstacle as soon as it exits the screen
                 obstacles.pop()

        def draw(self,SCREEN):
            SCREEN.blit(self.image[self.type],self.rect)

    class SmallCactus(Obstacle):
        def __init__(self,image):
            self.type=random.randint(0,2)
            super().__init__(image,self.type)   #initializes the init method of the parent class Obstacles
            self.rect.y=325

    class LargeCactus(Obstacle):
        def __init__(self,image):
            self.type=random.randint(0,2)
            super().__init__(image,self.type)
            self.rect.y=300         #is lower than the small cactus

    class Bird(Obstacle):
        def __init__(self,image):
            self.type=0
            super().__init__(image,self.type)
            self.rect.y=250
            self.index=0

        def draw(self,SCREEN):
            if self.index>=9:           #resets the index once it reaches 9
                self.index=0
            SCREEN.blit(self.image[self.index//5],self.rect)        #blits the image onto the screen
            self.index+=1
        
    def main():
        global game_speed,x_pos_bg,y_pos_bg,points,obstacles   #makes global variable
        run=True                    #switch for the while loop
        clock=pygame.time.Clock()       #clock to time the game
        player = Dinosaur()           #creating the player
        cloud=Cloud()           #creating cloud
        game_speed=14       #setting game speed
        x_pos_bg=0
        y_pos_bg=380
        points=0            #points at the beginning is 0
        font=pygame.font.Font('freesansbold.ttf',20)
        obstacles=[]
        death_count=0       #death counter at the beginning is 0
  
        def score():
            global points, game_speed
            points+=1       #increases the points by 1 each time the function is called
            if points%100==0:           #increases the speed each time the points increase by 100
                game_speed+=1
            text=font.render("Points:"+str(points),True,(0,0,0))    #how the points are displayed
            textRect=text.get_rect()            #the rectangle in which the points are displayed
            textRect.center=(1000,40)           #setting the rectangle's center to the top right
            SCREEN.blit(text,textRect)          #blits the points on the screen
        
        def background():
            global x_pos_bg,y_pos_bg            #fetching the global coordinates of the background
            image_width=BG.get_width()      #fetching the image width of the background image
            SCREEN.blit(BG,(x_pos_bg,y_pos_bg))     #blit the image onto the screen
            SCREEN.blit(BG,(image_width+x_pos_bg,y_pos_bg)) #blit another image behind the first one
            if x_pos_bg<=-image_width:           #if the image moves out of screen
                SCREEN.blit(BG,(image_width+x_pos_bg,y_pos_bg)) #a new image(the same one) is again displayed
                x_pos_bg=0
            x_pos_bg-=game_speed
        
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:         #creating a function to close the game when you press the x on the top
                    run=False
                    pygame.quit()
                    exit()
                
            SCREEN.fill((255,255,255))              #filling the screen white on every iteration
            userInput=pygame.key.get_pressed()  #adding the variable
            player.draw(SCREEN)
            player.update(userInput)
            if len(obstacles)==0:               #randomly spawns either small or large cactus, or bird when there is no obstacles on screen
                if random.randint(0,2)==0:
                    obstacles.append(SmallCactus(SMALL_CACTUS))
                elif random.randint(0,2)==1:
                    obstacles.append(LargeCactus(LARGE_CACTUS))
                elif random.randint(0,2)==2:
                    obstacles.append(Bird(BIRD))

            for obstacle in obstacles:
                obstacle.draw(SCREEN)
                obstacle.update()
                if player.dino_rect.colliderect(obstacle.rect): #if the player hitbox collides with the hitbox of an obstacle
                    pygame.time.delay(2000)
                    death_count+=1
                    menu(death_count)

            background()
            cloud.draw(SCREEN)          #calling the function with parameter SCREEN
            cloud.update()      #calling the function
            score()
            clock.tick(30)      #setting the timing of the game
            pygame.display.update()     #updates the display

    def menu(death_count):
        global points
        while True:
            SCREEN.fill((255,255,255))          #fills the screen with white
            font=pygame.font.Font('freesansbold.ttf',30)        #Inserts text with specifications
            if death_count==0:
                text=font.render("Press any key to start",True,(0,0,0))
            elif death_count>0:
                text=font.render("Press any key to restart",True,(0,0,0))
                global score
                score=font.render("Your score:"+ str(points),True,(0,0,0))
                scoreRect=score.get_rect()          #gets the score
                scoreRect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+50)      #positions the score rectangle
                SCREEN.blit(score,scoreRect)
            textRect=text.get_rect()
            textRect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)          #positions the score in the rectangle
            SCREEN.blit(text,textRect)
            SCREEN.blit(RUNNING[0],(SCREEN_WIDTH//2-20,SCREEN_HEIGHT//2-140)) #positions the image of a runnning dino
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    dino_points(dino_name,points)
                    pygame.quit()
                    exit()
                elif event.type==pygame.KEYDOWN:
                    main()
  
    menu(death_count=0)

#==============================================================================================================================#
#code for PewPew
def accept_pewpew():    #p=pewpew
  
    def display_text():#when confirm is pressed, pewpew name is accpeted
        global pewpew_name
        pewpew_name= pentry.get()
        
    global proot
    proot = Tk()# creating tkinter window and setting it
    proot.geometry("750x250")#dimensions for window
    proot.title("Accepting PewPew")#title for the window
    proot.configure(bg='black')#bg for the window 
    plabel=Label(proot, text="Enter Name", font=("Book Antiqua",25))#creating label
    plabel.pack(pady = 20)#packing the label
    global pentry #globalisingut
    pentry= Entry(proot, width= 40)#Create an Entry widget to accept User Input
    pentry.focus_set()#setting focus on this tab
    pentry.pack()#packing the entry
    pbtn1 = Button(proot, text ="Confirm", command=display_text)# Creating confirm button.
    pbtn1.pack(pady = 20)#packing button
    pbtn2 = Button(proot, text ="Continue", command=PewPew)#creating continue button
    pbtn2.pack(pady = 5)#packing button
    
def PewPew():
    proot.destroy()#destroying name accepting window
    import pygame
    import random
    import math
    from pygame import mixer

    mixer.init()        #initiating modules
    pygame.init()
    
    mixer.music.load('background.wav')  #loading the music file
    mixer.music.play(-1)
    #playing the music
    screen=pygame.display.set_mode((800,600))       #size of the screen
    pygame.display.set_caption('Space Shooter Game')    #naming the game/popup               #setting the icon image
    background=pygame.image.load('bg.png')      #loading the image files
    spaceshipimg=pygame.image.load('gun.png')
    alienimg=[]         #empty lists
    alienX=[]
    alienY=[]
    alienspeedX=[]
    alienspeedY=[]
    no_of_aliens=6
    for i in range(no_of_aliens):
        alienimg.append(pygame.image.load('baloon.png'))
        alienX.append(random.randint(0,736))    #random number from 0 to 736
        alienY.append(random.randint(30,150))
        alienspeedX.append(-1)
        alienspeedY.append(40)

    score=0         #score tally
    bulletimg=pygame.image.load('dart.png')
    check=False
    bulletX=386     #x and y coordinates of bullet
    bulletY=490
    spaceshipX=370      #x and y coordinates of the ship
    spaceshipY=480
    changeX=0
    running=True
    font=pygame.font.SysFont('Arial',32,'bold') #font style and size

    def score_text():
        img=font.render(f'Score:{score}',True,'white')
        screen.blit(img,(10,10))

    def gameover():
        img_gameover = font_gameover.render('GAME OVER', True, 'white')
        screen.blit(img_gameover, (200, 250))
        

  
    
    font_gameover=pygame.font.SysFont('Arial',64,'bold')
    while running:
        screen.blit(background,(0,0))
        for event in pygame.event.get():        #from all the events done by user, if the user clicks the exit button
            if event.type==pygame.QUIT:         
                running=False          #stops the running of the program
                pewpew_points(pewpew_name,score)
                pygame.quit()#quits the pygame module
                exit()#exits
    
            if event.type==pygame.KEYDOWN:  #if a key is pressed
                if event.key==pygame.K_LEFT:    #and that key is left arrow
                    changeX=-5              #move to the left by 5 units
                if event.key==pygame.K_RIGHT:   #if the key is right arrow
                    changeX=5                #move to the right by 5 inits
                if event.key==pygame.K_SPACE:   #if the key is the space bar
                    if check is False:
                        bulletSound=mixer.Sound('laser.wav')    #play the music track for shooting
                        bulletSound.play()
                        check=True
                        bulletX=spaceshipX+16       #the bullet moves
            if event.type==pygame.KEYUP:    #if the key is the up arrow
                changeX=0           #nothing happens
        spaceshipX+=changeX  #spaceshipX=spaceshipX-changeX
        if spaceshipX<=0:
            spaceshipX=0        #side of the screen
        elif spaceshipX>=736:
            spaceshipX=736      #side of the screen
        for i in range(no_of_aliens):
            if alienY[i] > 420:         #if the aliens cross 420 on the y axis
                for j in range(no_of_aliens):
                    alienY[j] = 2000        
                gameover()          #calls the function to end the game
                break
            alienX[i]+=alienspeedX[i]           #alien speeds
            if alienX[i]<=0:
                alienspeedX[i]=1
                alienY[i]+=alienspeedY[i]
            if alienX[i]>=736:
                alienspeedX[i]=-1
                alienY[i]+=alienspeedY[i]
            distance = math.sqrt(math.pow(bulletX - alienX[i], 2) + math.pow(bulletY - alienY[i], 2))   #bullet physics
            if distance < 27:       #if the bullet hits
                explosion= mixer.Sound('explosion.wav')     #explosion sounds comes
                explosion.play()        #plays the explosion sound
                bulletY = 480
                check = False
                alienX[i] = random.randint(0, 736)      #random x coordinate of new alien
                alienY[i] = random.randint(30, 150)     #random y coordinate of new alien
                score += 1                  #increases the score by one for each time the explosion is hear
            screen.blit(alienimg[i], (alienX[i], alienY[i]))        #blits the new alien at the random coordinates
        if bulletY<=0:
            bulletY=490
            check=False
        if check:
            screen.blit(bulletimg, (bulletX, bulletY))
            bulletY-=5
        screen.blit(spaceshipimg, (spaceshipX, spaceshipY))     #calling the functions
        score_text()
        pygame.display.update()

#==============================================================================================================================#
 #code for Snake
def accept_snake():  #s=snake
    global sroot
    sroot = Tk()# creating tkinter window and setting it
    sroot.geometry("750x250")#dimensions for window
    sroot.title("Accepting Snake")#title for the window
    sroot.configure(bg='black')#bg for the window 

    def display_text():
        global snake_name
        snake_name= sentry.get()
        
    slabel=Label(sroot, text="Enter Name", font=("Book Antiqua",25))#creating label
    slabel.pack(pady = 20)#packing the label
    global sentry#globalising
    sentry= Entry(sroot, width= 40)#Create an Entry widget to accept User Input
    sentry.focus_set()#setting focus on this tab
    sentry.pack()#packing the entry
    sbtn1 = Button(sroot, text ="Confirm", command=display_text)# Creating confirm button.
    sbtn1.pack(pady = 20)#packing button
    sbtn2 = Button(sroot, text ="Continue", command=Snake)#creating continue button
    sbtn2.pack(pady = 5)#packing button

def Snake():
    sroot.destroy()#destroying name accepting window
    #importing module
    import turtle
    import random
	
    #global constants
    turtle.TurtleScreen._RUNNING=True#letting turtle module know that the screen is running
    w = 500#width of window
    h = 500#height of window
    food_size = 10#size of food
    delay = 100#delay in ms
    start = {"up": (0, 20),"down": (0, -20),"left": (-20, 0),"right": (20, 0)}#star position
 
    def character():
        global snake, snake_dir, food_position, pen
        snake = [[0, 0]]#size of snake st start
        snake_dir = "up"#direction of snake at start
        food_position = get_random_food_position()      #gets random position of food
        food.goto(food_position)                    #puts the food in the random position
        move_snake()
     
    def move_snake():
        global snake_dir

	#working of snake, take head from last and puts it in front and and the process is repeated
        new_head = snake[-1].copy()
        new_head[0] = snake[-1][0] + start[snake_dir][0]
        new_head[1] = snake[-1][1] + start[snake_dir][1]
        if new_head in snake[:-1]:#if the end and head collides
            turtle.clear()#clearing the turle board (score)
            global score #globalising
            score=len(snake)#figuring out score by count length of snake
            snake_points(snake_name,score) #invoking function to add points and show leaderboard
            turtle.pencolor("green")#pen color
            turtle.setposition(0, 0)#position to show final score
            turtle.color('white')#color to show final score
            turtle.write("Score \n",align='center', font=("Book Antiqua",30))#writing score
            turtle.write(score, align='center',font=("Book Antiqua",30))#writing score
            turtle.hideturtle()#hiding the turtle arrow
            
        else: #if the end and head doesnt collides
            turtle.clear()#clearing the turle board(score)
            turtle.setposition(200, 200)#position to write current score
            turtle.write(len(snake),font=("Book Antiqua",20))#writing the current score
            turtle.hideturtle()#hiding the tutrle arrow
            snake.append(new_head) #adding extra lenght
			
            #to make the edges valid for the code(ie hitting the edges doesnt stop inside snake comes through other side)
            if not food_collision():
                snake.pop(0)
            if snake[-1][0] > w / 2:
                snake[-1][0] -= w
            elif snake[-1][0] < - w / 2:
                snake[-1][0] += w
            elif snake[-1][1] > h / 2:
                snake[-1][1] -= h
            elif snake[-1][1] < -h / 2:
                snake[-1][1] += h

            pen.clearstamps()
             
            for segment in snake:
                pen.goto(segment[0], segment[1])
                pen.stamp()
 
            screen.update()#updating screen
            turtle.ontimer(move_snake, delay)#moving snake atfer the delay time set
 
    def food_collision():#function if food collides
        global food_position#getting position of food
        if get_distance(snake[-1], food_position) < 20:#checking if food is close to snake head
            food_position = get_random_food_position()#if close, places new food at random places
            food.goto(food_position)#the code goes to the mentioned function line
            return True
        return False
		
    def get_random_food_position():#creating random posistion for food
        x = random.randint(- w / 2 + food_size, w / 2 - food_size)
        y = random.randint(- h / 2 + food_size, h / 2 - food_size)
        return (x, y)
 
    def get_distance(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance
    def go_up():#function to make snake go up
        global snake_dir
        if snake_dir != "down":
            snake_dir = "up"
 
    def go_right():#function to make snake go right
        global snake_dir
        if snake_dir != "left":
            snake_dir = "right"
 
    def go_down():#function to make snake go down
        global snake_dir
        if snake_dir!= "up":
            snake_dir = "down"
 
    def go_left():#function to make snake go left
        global snake_dir
        if snake_dir != "right":
            snake_dir = "left"
 
 
    screen = turtle.Screen()#creating turtle window
    screen.setup(w, h)#dimensions of window
    screen.title("Snake")#title of window
    screen.bgcolor("green")#bg of window
    screen.tracer(0) #delay and delay for screen to update
    pen = turtle.Turtle("square")#size of snake(individual)
    pen.penup()
    food = turtle.Turtle()      #making the food 
    food.shape("square")        #setting food shape
    food.color("red")        #setting food colour
    food.shapesize(food_size / 20)  #setting food size
    food.penup()
    screen.listen()
	
    #when the button is pressed the rightful function is performed
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    
    character()
    turtle.done()

#==============================================================================================================================#
#running the program
#creating_pointtable()
mainloop()
