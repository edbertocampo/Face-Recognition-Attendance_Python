#OCAMPO, EDBERT
#TIAMSIM, MARLENE
#FACE RECOGNITION SYSTEM

#admin_login.py file

from tkinter import Tk,Label, Frame, Entry, Button, StringVar, W
from tkinter import messagebox as ms
import sqlite3
import os

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()



#main Class
class main:
    def __init__(self,master):
       
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()
        self.wid()

        
    #Login Function
    def login(self):
        
    	#Establish Connection para sa login
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            
            ms.showinfo('Info','Admin Logged in')
            self.master.destroy()
            os.system('python datasetcreate.py')
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection na para sa new user
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action 
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methods....
    
    def admin(self):
        self.adminf.pack_forget()
        self.adminf.pack()
        
        
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
        
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    def run(self):
        
        os.system('python datasetcreate.py')
        
        
    def detect(self):
        
        os.system('python detector.py')
    
    
        
    #Draw Widgets na puuuuu
    def widgets(self):
        
        app_width = 650
        app_height = 350
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.master.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.master.configure (bg='black')
        
        
        self.head = Label(self.master,text="Face Recognition System", bg = "blue", width = "50", height = "2",font = ('Early GameBoy',20,'bold'),fg = 'yellow',pady = 10)
        self.head.pack()
        self.adminf = Frame(self.master, padx = 10, pady = 10,bg ='black')
        
        self.adminf = Frame(self.master, padx = 10, pady = 50, bg ='black')  
        Button(self.adminf,text = ' Admin ',bd = 3 ,font = ('monaco',20, 'bold'),padx=24,pady=5,bg= 'blue' ,fg = 'yellow',command=lambda:[self.log(),self.adminf.pack_forget()]).grid(row = 1, column = 1)
        Button(self.adminf,text = ' Employee ',bd = 3 ,font = ('monaco',20, 'bold'),padx=1,pady=5,bg= 'blue' ,fg = 'yellow',command = self.detect).grid(row = 3 , column = 1, pady=(10,0))
        self.adminf.pack()
        
       
     
    def wid(self):
        self.logf = Frame(self.master,padx =10,pady = 10,bg ='black')
        Label(self.logf,text = 'Username: ',font = ('monaco',20, 'bold'),pady=5,padx=5,bg ='black',fg = 'yellow').grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('monaco',20, 'bold')).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('monaco',20, 'bold'),pady=5,padx=5,bg ='black',fg = 'yellow').grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('monaco',20, 'bold'),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('monaco',15, 'bold'),padx=1,pady=1,bg= 'blue' ,fg = 'yellow',command=self.cr).grid(row=2,column=0)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('monaco',15, 'bold'),padx=1,pady=1,bg= 'blue' ,fg = 'yellow', command =lambda: [self.login(),self.logf.pack_forget()]).grid(row=4,column=1)

        
        self.crf = Frame(self.master,padx =10,pady = 10,bg ='black')
        Label(self.crf,text = 'Username: ',font = ('monaco',20, 'bold'),pady=5,padx=5,bg ='black',fg = 'yellow').grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('monaco',20, 'bold')).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('monaco',20, 'bold'),pady=5,padx=5,bg ='black',fg = 'yellow').grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('monaco',20, 'bold'),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('monaco',15, 'bold'),padx=1,pady=1,bg= 'blue' ,fg = 'yellow',command=self.log).grid(row=2,column=0)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('monaco',15, 'bold'),padx=1,pady=1,bg= 'blue' ,fg = 'yellow',command=self.new_user).grid(row=4,column=1)

        
        self.adminmenuf = Frame(self.master,padx =10,pady = 10,bg ='#222831')
        self.head = Label(self.master,text="Face Recognition System", bg = "grey", width = "50", height = "1",font = ('monaco',15,'bold'),pady = 10)
        self.adminmenuf = Frame(self.master,padx =10,pady = 10)
        Button(self.adminmenuf,text = ' Employee Data ',bd = 3 ,font = ('monaco',16, 'bold'),padx=50,pady=5,bg= '#ffd369' ,fg = '#393e46', command =lambda: [self.crf.pack_forget(),self.run()]).grid(row=2,column=1)
        Button(self.adminmenuf,text = ' Employee Login Records ',bd = 3 ,font = ('monaco',15, 'bold'),padx=5,pady=5,bg= '#ffd369' ,fg = '#393e46').grid(row=4,column=1, pady=(10,0))

      

if __name__ == '__main__':
	#Create Object
	#and setup window
    root = Tk()
    root.title('Face-Recognition System')
    root.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')
    main(root)
    root.mainloop()
