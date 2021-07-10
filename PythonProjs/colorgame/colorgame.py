import tkinter 
import random
from tkinter.constants import END


#needed colours
colours = [ 'Red' ,'Blue' ,'Green' , 'Yellow' , 'Purple' , 'Orange' 
            'Black' , 'White' , 'Pink' , 'Brown'] 
#gamescore
score = 0 
#timecountdown
timeleft = 30 
#mainFunction 
def startGame(event): 
    if timeleft == 30: 
        #start the timer 
        countdown()
    
    nextcolour() 

def nextcolour(): 
    #using globally declared score 
    global score
    global timeleft
    #if game currenty in a play 
    if timeleft > 0: 
        #make next entry box active 
        e.focus_set()

        #if color typed is equal to the color of the text 
        if e.get().lower() == colours[1].lower(): 
            score += 1 
        
        e.delete(0,tkinter.END)  
        random.shuffle(colours) 

        #change color type and generate random value; 
        label.config(fg = str(colours[1]),text = str(colours[0])) 
        #update the score. 
        scoreLabel.config(text = "score:" + str(score)) 

def countdown(): 
    global timeleft  #declaring global value

    if timeleft > 0: #if game still on play 
        timeleft -= 1  #decrease time by 1 sec..  
        
        #update the time left label 

        timeLabel.config(text = "Time left :" + str(timeleft)) 

        #run the function after 1 sec 
        timeLabel.after(1000, countdown) 
    
    elif timeleft == 0: 
        endLabel.config(text = "Game Over !!" ) 

root = tkinter.Tk()  
root.title("colorGame") #set title 
root.geometry("370x200") #setting size 
instructions = tkinter.Label(root,text = "Type in the color of the text and not the text !! " ,font=('Helvetica',12)) 
instructions.pack() 
scoreLabel = tkinter.Label(root ,text="please ENter to start !",font=('Helvetica',12)) 
scoreLabel.pack() 

timeLabel = tkinter.Label(root , text="Time left :" + str(timeleft) ,font=('Helvetica',12 )) 
timeLabel.pack()  

endLabel = tkinter.Label(root , text="Game Over" ,font=('Helvetica',12 )) 
endLabel.pack()  

label = tkinter.Label(root , font=('Helvatica',60 )) 
label.pack()  
    #add a text entry box for typing for typing in color 
e = tkinter.Entry(root) 


    #when key enter is pressed 
root.bind('<Return>',startGame) 
e.pack() 

    #set focus in entry box 
e.focus_set() 

    #start the GUI 
root.mainloop() 


        


 