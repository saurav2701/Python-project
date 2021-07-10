import tkinter 
import os 
from tkinter import*
from tkinter.messagebox import* 
from tkinter.filedialog import*

class Notepad: 
    __root = Tk() 
    #default win height and widtth 
    __thiswidth = 300 
    __thisheight = 300 
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar,tearoff = 0) 
    __thisEditMenu = Menu(__thisMenuBar , tearoff = 0) 
    __thisHelpMenu = Menu(__thisMenuBar , tearoff = 0) 

    #to add scrillbar 
    __thisScrollBar = Scrollbar(__thisTextArea) 
    __file = None
 
    def __init__(self,**kwargs): 
        #set icon 
        try: 
            self.__root.wm_iconbitmap("Notepad.ico") 
        except: 
            pass 
        #set window size : 
        try: 
            self.__thiswidth = kwargs['width'] 
        except KeyError: 
            pass 

        try: 
            self.__thisheight = kwargs['height'] 
        except KeyError: 
            pass 

        #set windowtext 
        self.__root.title("untitled - Notepad") 
        #center the window 
        screenwidth = self.__root.winfo_screenwidth() 
        screenheight = self.__root.winfo_screenheight() 

        #for left align 
        left = (screenwidth / 2 ) - (self.__thiswidth / 2 ) 
        top = (screenheight /2)  - (self.__thisheight / 2) 
        #for top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % ( self.__thiswidth , 
                                                self.__thisheight,
                                                left,top ))
        self.__root.grid_rowconfigure(0,weight =1)  
        self.__root.grid_columnconfigure(0,weight = 1) 

        #add control widgets : 
        self.__thisTextArea.grid(sticky = N + E + S + W )  

        #to open new file : 
        self.__thisFileMenu.add_command(label = "New" , command = self.__newFile ) 

        #to open a already existing file : 
        self.__thisFileMenu.add_command(label = "open" , command = self.__openFile ) 

        #to save current file : 
        self.__thisFileMenu.add_command(label = "save"  , command = self.__saveFile) 

        #to create a line in the dialoge : 
        self.__thisFileMenu.add_separator() 
        self.__thisFileMenu.add_command(label = "Exit", command =self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)     
          
 # To give a feature of cut 
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut )             
      
        # to give a feature of copy    
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
          
        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
          
        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)     
          
        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
  
        self.__root.config(menu=self.__thisMenuBar)  
        self.__thisScrollBar.pack(side = RIGHT , fill = Y ) 

        #scroll automatically adjust acc to content 

        self.__thisScrollBar.config(command = self.__thisTextArea.yview) 
        self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set) 


    def __quitApplication(self): 
        self.__root.destroy() 
        #exit 
    
    def __showAbout(self): 
        showinfo("Notepad" , "Saurav Bhusal") 
    
    def __openFile(self): 
        self.__file = askopenfilename(defaultextension=".txt" , filetypes=[("All files","*.*"), 
        ("Text Documents","*.txt" )]) 

        if self.__file == "": 
            #no filetoOpen ; 
            self.__file = None 
        else: 
            #try to open the file 
            self.__root.title(os.path.basename(self.__file) + " -Notepad ") 
            self.__thisTextArea.delete(1.0 ,END ) 

            file = open(self.__file,"r" ) 

            self.__thisTextArea.insert(1.0,file.read() ) 
            file.close()  
    
    def __newFile(self): 
        self.__root.title("Untitled - Notepad ") 
        self.__file = None  
        self.__thisTextArea.delete(1.0,END ) 
    
    def __saveFile(self): 
        if self.__saveFile == None: 
            #save as new  file 
            self.__file = asksaveasfilename(initialfile='untitles.txt' , defaultextension=".txt" , filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 

            if self.__file == "": 
                self.__file = None 
            else: 
                #try to save the file 
                file = open(self.__file,'w') 
                file.write(self.__thisTextArea.get(1.0, END))  
                file.close() 

                #change the window title 
                self.__root.title(os.path.basename(self.__file) + "-Notepad") 

        

    def __cut(self): 
        self.__thisTextArea.event_generate("<<cut>>") 

    def __copy(self): 
        self.__thisTextArea.event_generate("<<copy>>")  

    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>") 
        
    def run(self): 
         #run main app 
        self.__root.mainloop() 


#run main application 
notepad =  Notepad(width=600 , height=400)
notepad.run() 



             
  




 


