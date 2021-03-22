# Tyler Quinn
# CPSC 21000 - Programming Fundamentals
# The purpose of this program is to simulate College Football

import turtle 
import random 
import time 


win = turtle.Screen()
win.setup(750,750,100,100)
win.bgcolor(.17, .79, .333)
sam = turtle.Turtle()
sam.hideturtle()
sam.speed(0)
sam.penup()
sam.goto(100,100)




x = -350
y = 300
w = 700
h = 600

field = turtle.Turtle()
field.hideturtle()
field.speed(0)
field.penup()
field.goto(x,y)
field.fillcolor('Yellow')
#field.fillcolor(.17, .79, .333)
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w)
    field.right(90)
    field.forward(h)
    field.right(90)
field.end_fill()
field.penup()
field.goto(-340,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(-240,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(-140,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(-40,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(60,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(160,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()
field.penup()
field.goto(260,290)
field.fillcolor('Green')
field.begin_fill()
field.pendown()
field.seth(0)
for i in range(2): 
    field.forward(w/8.5)
    field.right(90)
    field.forward(h - 20)
    field.right(90)
field.end_fill()










# Formula to find position of turtle 

pixels_per_yard = 20

fieldStartingxPixel = -350

field_starting_yard = 30

myYard = 25

xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard

print('')

#print(xPixel)




# Build the turtle which will write out field yard lines

messages = turtle.Turtle()
messages.hideturtle()
messages.speed(0)
messages.penup()
myYard = 30
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
messages.goto(xPixel,300)

messages.write('30yrd',font=('Arial',12,'bold'))

messages.penup()
myYard = 25
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard

messages.goto(xPixel,300)

messages.write('25yrd',font=('Arial',12,'bold'))


messages.penup()
myYard = 20
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard

messages.goto(xPixel,300)


messages.write('20yrd',font=('Arial',12,'bold'))


messages.penup()
myYard = 15
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard

messages.goto(xPixel, 300)


messages.write('15yrd',font=('Arial',12,'bold'))


messages.penup()
myYard = 10
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
messages.goto(xPixel,300)

messages.write('10yrd',font=('Arial',12,'bold'))


messages.penup()
myYard = 5
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
messages.goto(xPixel,300)

messages.write('5yrd',font=('Arial',12,'bold'))


messages.penup()
myYard = 0
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
messages.goto(xPixel,300)

messages.write('0yrd',font=('Arial',12,'bold'))



# Reset so Football player starts at the 25yrd line
myYard = 25

pixels_per_yard = 20

fieldStartingxPixel = -350

field_starting_yard = 30

xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard






# Build the turtle which will represent the football player 

football = turtle.Turtle()
football.penup()
football.shape('turtle')
football.color(1, .859, .67450)
football.showturtle()
football.goto(xPixel,0)
football.pendown()
    

# 10 Yards to Reset First Down 

yards_to_first = 10 

downs = 1 # First Down 


# Build the turtle which will draw downs and yards text at the bottom of the screen 

bottomText = turtle.Turtle()
bottomText.hideturtle()
bottomText.speed(0)
bottomText.penup()
myYard = 30
xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
bottomText.goto(xPixel,-350)

# Write the text for downs and yards 

bottomText.write('Down %d, %d yards to go' %(downs, yards_to_first),font=('Arial',24,'bold'))


# Once again reset Football player yard position just to be safe 
myYard = 25

pixels_per_yard = 20

fieldStartingxPixel = -350

field_starting_yard = 30

xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard



while downs <= 4 and myYard > 0:
    #While the game hasn't been won or lost 
    #Ask the user to enter p or r 
    choice = input("Select 'p' to pass the ball or select 'r' to run the ball: ")
    gain = 0 #Assume there will be no gain 
    if choice == 'p': 
        #Determine if the pass is complete with a 50/50 chance of completion 
        passCompletion = random.randint(0,1) #Where 0 is incomplete and 1 is complete 
        if passCompletion == 1: #If pass is completed
            gain = random.randint(3,15) #Pass between 3 and 15 yards
    elif choice == 'r': 
        gain = random.randint(-3,8) #Run between -3 and 8 yards 
    myYard = myYard - gain #Accounting for position change in reference to change in yards 
    
    #Reposition the turtle to the new yardline 

    pixels_per_yard = 20

    fieldStartingxPixel = -350

    field_starting_yard = 30

    xPixel = fieldStartingxPixel + (field_starting_yard - myYard) * pixels_per_yard
    football.goto(xPixel,0)

    yards_to_first = yards_to_first - gain #Removing the gained yards from remaining yards to first down

    if yards_to_first <= 0: 
        #If you got a first down
        downs = 1
        if myYard < 10: 
            yards_to_first = myYard
        else: 
            #Full 10 yards to go 
            yards_to_first = 10
    else: 
        #Didn't get a first down 
        downs = downs + 1  


    #Update text at the bottom of the screen
    bottomText.undo() # Clears the last message
    bottomText.write('Down %d, %d yards to go' %(downs, yards_to_first),font=('Arial',24,'bold'))


    #Update the terminal to show the play that just happened and the current yard line, down, yards to first

    if choice == 'p': 
        if passCompletion == 0:
            print('')
            print('Incomplete pass.')
            print('')
        elif passCompletion == 1:
            passStatement = 'Complete pass for %d yards!' %(gain)
            print('')
            print(passStatement)
            print('')

    if choice == 'r': 
        print('')
        runStatement = 'Run for %d yards.' %(gain)
        print(runStatement)
        print('')

    if myYard > 0:

        downStatement = 'Down %d' %(downs)
        print('')
        print(downStatement)
        print('')
        yardstofirstStatement = '%d yards to go on the %d yard line.' %(yards_to_first, myYard)
        print('')
        print(yardstofirstStatement)
        print('')


if myYard <= 0: 
    #Won
    print('')
    print('Touchdown! You won!')
    print('')
    winText = turtle.Turtle()
    winText.hideturtle()
    winText.speed(0)
    winText.penup()
    winText.goto(50,-350)
    winText.write('Touchdown! You win!',font=('Arial',24,'bold'))


elif downs > 4:
    #Lost 
    print('')
    print('You lose!')
    print('')
    loseText = turtle.Turtle()
    loseText.hideturtle()
    loseText.speed(0)
    loseText.penup()
    loseText.goto(50,-350)
    loseText.write('You lose!',font=('Arial',24,'bold'))




input('Press key to close the application: ')
quit()