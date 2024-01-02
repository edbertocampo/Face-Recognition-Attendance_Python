#OCAMPO, EDBERT
#TIAMSIM, MARLENE
#FACE RECOGNITION SYSTEM
#improved at face recognition tahn the last presentation at the newly registered faces 


#datacreate.py file

from tkinter import Tk,Label, Frame, Entry, Button, StringVar
from tkinter import messagebox as ms
import os
import sqlite3
import cv2
import random


faceDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');
eyesDetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml');
camera_port = 0
cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW);

    
class admin(object):
    def __init__(self,master):
        self.master = master
        self.lname = StringVar()
        self.fname = StringVar()
        self.mname = StringVar()
        self.age = StringVar()
        self.birthdate = StringVar()
        self.gender = StringVar()
        self.address = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        
        self.lname_editor = StringVar()
        self.fname_editor = StringVar()
        self.mname_editor = StringVar()
        self.age_editor = StringVar()
        self.birthdate_editor = StringVar()
        self.gender_editor = StringVar()
        self.address_editor = StringVar()
        self.email_editor = StringVar()
        self.contact_editor = StringVar()
        self.selectbox = StringVar()
        #Create Widgets
        self.widgets()
        #self.cam()
        
  
    #para sa update
    def search(self):
         search = Tk()
         search.title('Employee Data Records')
         search.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')

         app_width = 1460
         app_height = 200

         screen_width = search.winfo_screenwidth()
         screen_height = search.winfo_screenheight()

         x = (screen_width / 2) - (app_width / 2)
         y = (screen_height / 2) - (app_height / 2)
    
        
         search.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
         search.configure (bg='black')
        #create a connection
         conn = sqlite3.connect("FaceRecognition_Employee.db")
        #create a cursor
         c = conn.cursor()
         
         #query sa database
         c.execute("SELECT * FROM Employee_Record  WHERE oid = " + self.selectbox.get())
         records = c.fetchall()
         
         Label(search,text = "Employee Data Records", bg = "blue", width = "70", height = "1",font =('Early GameBoy',15,'bold'),fg='yellow',pady = 10).grid(columnspan = 20,sticky="nw")
         if records:
             #loop thru results
                 print_records0=''
                 for record in records:
                     print_records0 +=   str (record[0]) +"\n"
                     
                 print_records1=''
                 for record in records:
                     print_records1 +=   str (record[1]) +"\n"
                
                 print_records2=''
                 for record in records:
                     print_records2 +=   str (record[2]) +"\n"
                  
                 print_records3=''
                 for record in records:
                     print_records3 +=   str (record[3]) +"\n"
                
                 print_records4=''
                 for record in records:
                     print_records4 +=   str (record[4]) +"\n"
                
                 print_records5=''
                 for record in records:
                     print_records5 +=   str (record[5]) +"\n"
                
                 print_records6=''
                 for record in records:
                     print_records6 +=   str (record[6]) +"\n"
                
                 print_records7=''
                 for record in records:
                     print_records7 +=   str (record[7]) +"\n"
                
                 print_records8=''
                 for record in records:
                     print_records8 +=   str (record[8]) +"\n"
                
                 print_records9=''
                 for record in records:
                     print_records9 +=   str (record[9]) +"\n"
                 
                 
                 Label(search,text = "ID" ,font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=0,pady=(10,0))
                 Label(search,text = "Last Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=1,pady=(10,0))
                 Label(search,text = "First Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=2,pady=(10,0))
                 Label(search,text = "Middle Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=3,pady=(10,0))
                 Label(search,text = "Age",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=4,pady=(10,0))
                 Label(search,text = "Birthdate",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 13).grid(row = 1,column=5,pady=(10,0))
                 Label(search,text = "Gender",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=6,pady=(10,0))
                 Label(search,text = "Address",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 30).grid(row = 1,column=7,pady=(10,0))
                 Label(search,text = "Email",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 20).grid(row = 1,column=8,pady=(10,0))
                 Label(search,text = "Contact Number",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=9,pady=(10,0))
                 Label(search, text = print_records0,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=0, pady=(10,0))
                 Label(search, text = print_records1,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=1, pady=(10,0))
                 Label(search, text = print_records2,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=2, pady=(10,0))
                 Label(search, text = print_records3,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=3, pady=(10,0))
                 Label(search, text = print_records4,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5).grid(row=2,column=4, pady=(10,0))
                 Label(search, text = print_records5,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=5, pady=(10,0))
                 Label(search, text = print_records6,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=6, pady=(10,0))
                 Label(search, text = print_records7,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=7, pady=(10,0))
                 Label(search, text = print_records8,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=8, pady=(10,0))
                 Label(search, text = print_records9,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5).grid(row=2,column=9, pady=(10,0))
         else:
              self.selectbox.set('')
              search.destroy()
              ms.showerror('Error!','NO RECORD FOUND')
          #commit changes 
         conn.commit()
         #close na connection
         conn.close()
          
    def update(self):
          conn = sqlite3.connect("FaceRecognition_Employee.db")
          #create a cursor
          c = conn.cursor()
          
          record_id = self.selectbox.get()
          c.execute("""UPDATE Employee_Record SET
                Last_Name = :lname,
                First_Name = :fname,
                Middle_Name = :mname,
                Age = :age,
                Birthdate = :birthdate,
                Gender = :gender,
                Address = :address,
                Email = :email,
                Contact_Number = :contact
                    
                WHERE oid = :oid """,
                {
                'oid' : record_id,
                'lname' : self.lname_editor.get(),
                'fname' : self.fname_editor.get(),
                'mname' : self.mname_editor.get(),
                'age' : self.age_editor.get(),
                'birthdate' : self.birthdate_editor.get(),
                'gender' : self.gender_editor.get(),
                'address' : self.address_editor.get(),
                'email' : self.email_editor.get(),
                'contact' : self.contact_editor.get()
                })
          
          ms.showinfo('Success!','Data Updated') 
          self.selectbox.set('')
          conn.commit()
          conn.close()
          
          editor.destroy()
         
         
    #para sa edit
    def edit(self):
         global editor
         global records
         editor = Tk()
         editor.title('Edit Employee Data')
         editor.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')
         app_width = 1550
         app_height = 720

         screen_width = editor.winfo_screenwidth()
         screen_height = editor.winfo_screenheight()

         x = (screen_width / 2) - (app_width / 2)
         y = (screen_height / 2) - (app_height / 2)
    

         editor.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
         editor.configure (bg='black')
         conn = sqlite3.connect("FaceRecognition_Employee.db")
        #create a cursor
         c = conn.cursor()
         
         
         record_id = self.selectbox.get()
         
         if record_id:
             c.execute("SELECT * FROM Employee_Record WHERE oid = " + record_id)
             records = c.fetchall()
         else:
            
             ms.showerror('Error!','Input ID')
         
         
             records = c.fetchall()
        
         
         self.head = Label(editor,text="Update Employee Records" , bg = "blue", width = "50", height = "1",font = ('Early GameBoy',25),fg = 'yellow',pady = 10).grid(columnspan = 20, sticky= 'nw')
         
         Frame(editor, padx = 10, pady = 10)    
         
         
         self.lname_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.lname_editor.grid(row=2, column=3, padx=30, pady = 5)
         self.fname_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.fname_editor.grid(row=3, column=3, padx=30, pady = 5)
         self.mname_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.mname_editor.grid(row=4, column=3, padx=30, pady = 5)
         self.age_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.age_editor.grid(row=5, column=3, padx=30, pady = 5)
         self.birthdate_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.birthdate_editor.grid(row=6, column=3, padx=30, pady = 5)
         self.gender_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.gender_editor.grid(row=7, column=3, padx=30, pady = 5)
         self.address_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.address_editor.grid(row=8, column=3, padx=30, pady = 5)
         self.email_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.email_editor.grid(row=9, column=3, padx=30, pady = 5)
         self.contact_editor = Entry(editor,width=20,font = ('monaco',15, 'bold'))
         self.contact_editor.grid(row=10, column=3, padx=30, pady = 5)
         

    #textboxlabels dito
       # Label(self.addf,text= "ID").grid(row=0,column=0, pady=(10,0))
         Label(editor,text= "Last Name             ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=2,column=2)
         Label(editor,text= "First Name            ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=3,column=2)
         Label(editor,text= "Middle Name           ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=4,column=2)
         Label(editor,text= "Age                   ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=5,column=2)
         Label(editor,text= "Birthdate (mm/dd/yyyy)",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=6,column=2)
         Label(editor,text= "Gender                ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=7,column=2)
         Label(editor,text= "Address               ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=8,column=2)
         Label(editor,text= "Email                 ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=9,column=2)
         Label(editor,text= "Contact Number        ",font = ('monaco',15, 'bold'),fg = 'yellow',bg ='black').grid(row=10,column=2)
         
          #loop thru results
         for record in records:
             self.lname_editor.insert(0, record[1])
             self.fname_editor.insert(0, record[2])
             self.mname_editor.insert(0, record[3])
             self.age_editor.insert(0, record[4])
             self.birthdate_editor.insert(0, record[5])
             self.gender_editor.insert(0, record[6])
             self.address_editor.insert(0, record[7])
             self.email_editor.insert(0, record[8])
             self.contact_editor.insert(0, record[9])
        
         #update/create&save button
         Button(editor, text="Update Record", command = self.update,font = ('Early GameBoy',10,'bold'),fg='yellow',pady = 10,bg ='blue').grid(row =11, column = 3, pady = 10,padx=10, ipadx=38)
         
    #para sa delete
    def delete(self):
        conn = sqlite3.connect("FaceRecognition_Employee.db")
        c = conn.cursor()
        
        #delete record
        c.execute("DELETE from Employee_Record WHERE ID =" + self.selectbox.get())
        
        self.selectbox.set('')
        ms.showinfo('Success!','Data Deleted') 
        conn.commit()
        conn.close()
    
    #para sa pag bubukas ng camera detector
    def detect(self):
        
        root.destroy()
        cv2.destroyAllWindows()
        cam.release()
        os.system('python admin_login.py')
       
    
    #para sa submit btn
    def submit(self):
        
        conn = sqlite3.connect("FaceRecognition_Employee.db")
        c = conn.cursor()
    
    #Insert na ng table
        c.execute("INSERT INTO Employee_Record (Last_Name, First_Name, Middle_Name, Age, Birthdate, Gender, Address, Email, Contact_Number) VALUES(:lname,:fname,:mname,:age,:birthdate,:gender,:address,:email,:contact)",
                  {
                      #'id' : self.id.get() ,
                      'lname' : self.lname.get(),
                      'fname' : self.fname.get(),
                      'mname' : self.mname.get(),
                      'age' : self.age.get(),
                      'birthdate' : self.birthdate.get(),
                      'gender' : self.gender.get(),
                      'address' : self.address.get(),
                      'email' : self.email.get(),
                      'contact' : self.contact.get()
                   })
       
       
        uid = c.lastrowid
        sampleNum = 0
        while True:
            ret, img = cam.read()
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize=(20, 20), flags =cv2.CASCADE_SCALE_IMAGE)
            for (x,y,w,h) in faces:
                sampleNum = sampleNum+1
                cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(random.randrange(256), random.randrange(256), random.randrange(256)),4)
                cv2.waitKey(100)
            cv2.imshow('img',img)
            cv2.waitKey(1);
            if sampleNum >= 20:
                ms.showinfo('Success!','Data Added') 
                #para to clear the boxes
        
                self.lname.set('')
                self.fname.set('')
                self.mname.set('')
                self.age.set('')
                self.birthdate.set('')
                self.gender.set('')
                self.address.set('')
                self.email.set('')
                self.contact.set('')
                break

    
    
        conn.commit()
        conn.close()
        
    
    
        
        
    def add(self):
        self.addf.pack_forget()
        self.addf.pack()
    
    def edits(self):
        self.editf.pack()
    
    def popup(self):
        self.popupf.pack()
    
    def digital(self):
        self.digitalf.pack()
    
    def train(self):
        os.system('python facetrainer.py')
        ms.showinfo('Success', 'Face Trained')
    
    def time(self):
        os.system('python opencsv.py')

    
        
        
        
    #query function
    def query(self):
        
         root = Tk()
         root.title('Employee Data Records')
         root.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')
         app_width = 1500
         app_height = 700

         screen_width = root.winfo_screenwidth()
         screen_height = root.winfo_screenheight()

         x = (screen_width / 2) - (app_width / 2)
         y = (screen_height / 2) - (app_height / 2)
    

         root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
         
         root.configure (bg='black')
        #create a connection
         conn = sqlite3.connect("FaceRecognition_Employee.db")
        #create a cursor
         c = conn.cursor()
         
         #query sa database
         c.execute("SELECT *, oid  FROM Employee_Record ")
         records = c.fetchall()
         #print(records)
         
         
         Label(root,text = "Employee Data Records", bg = "blue", width = "73", height = "1",font = ('Early GameBoy',15,'bold'),fg='yellow',pady = 10).grid(columnspan = 20,sticky="nw")
         
         #loop thru results
         print_records0=''
         for record in records:
             print_records0 +=   str (record[0]) +"\n"
             
         print_records1=''
         for record in records:
             print_records1 +=   str (record[1]) +"\n"
        
         print_records2=''
         for record in records:
             print_records2 +=   str (record[2]) +"\n"
          
         print_records3=''
         for record in records:
             print_records3 +=   str (record[3]) +"\n"
        
         print_records4=''
         for record in records:
             print_records4 +=   str (record[4]) +"\n"
        
         print_records5=''
         for record in records:
             print_records5 +=   str (record[5]) +"\n"
        
         print_records6=''
         for record in records:
             print_records6 +=   str (record[6]) +"\n"
        
         print_records7=''
         for record in records:
             print_records7 +=   str (record[7]) +"\n"
        
         print_records8=''
         for record in records:
             print_records8 +=   str (record[8]) +"\n"
        
         print_records9=''
         for record in records:
             print_records9 +=   str (record[9]) +"\n"
         
         
         Label(root,text = "ID" ,font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=0,pady=(10,0))
         Label(root,text = "Last Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=1,pady=(10,0))
         Label(root,text = "First Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=2,pady=(10,0))
         Label(root,text = "Middle Name",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=3,pady=(10,0))
         Label(root,text = "Age",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=4,pady=(10,0))
         Label(root,text = "Birthdate",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 13).grid(row = 1,column=5,pady=(10,0))
         Label(root,text = "Gender",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 5).grid(row = 1,column=6,pady=(10,0))
         Label(root,text = "Address",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 30).grid(row = 1,column=7,pady=(10,0))
         Label(root,text = "Email",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 20).grid(row = 1,column=8,pady=(10,0))
         Label(root,text = "Contact Number",font = ('monaco',11, 'bold'),pady=6,padx=5,bg ='blue',fg = 'yellow', width= 15).grid(row = 1,column=9,pady=(10,0))
         Label(root, text = print_records0,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=0, pady=(10,0))
         Label(root, text = print_records1,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=1, pady=(10,0))
         Label(root, text = print_records2,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=2, pady=(10,0))
         Label(root, text = print_records3,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=3, pady=(10,0))
         Label(root, text = print_records4,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5).grid(row=2,column=4, pady=(10,0))
         Label(root, text = print_records5,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=5, pady=(10,0))
         Label(root, text = print_records6,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=6, pady=(10,0))
         Label(root, text = print_records7,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=7, pady=(10,0))
         Label(root, text = print_records8,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5 ).grid(row=2,column=8, pady=(10,0))
         Label(root, text = print_records9,font = ('monaco',10, 'bold'),fg = 'white',bg='black',pady=6,padx=5).grid(row=2,column=9, pady=(10,0))
         
         
         #commit changes 
         conn.commit()
         #close na connection
         conn.close()
    
    def widgets(self): 
        
        #textboxes dito
        app_width =1550
        app_height = 720
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
    
        self.master.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.master.configure(bg='black')
        
        self.head = Label(self.master,text="Face Recognition System", bg = "blue", width = "100", height = "1",font = ('Early GameBoy',25,'bold'),fg = 'yellow',pady = 10)
        self.head.pack()
        
        self.addf = Frame(self.master, padx = 10, pady = 10)
        self.addf.configure (bg='black')
        #entry labels
        Entry(self.addf,textvariable = self.lname,width=20,font = ('monaco',15, 'bold')).grid(row=1, column=1, padx=30, pady=5)
        Entry(self.addf,textvariable = self.fname,width=20,font = ('monaco',15, 'bold')).grid(row=2, column=1, padx=30, pady=5)
        Entry(self.addf,textvariable = self.mname,width=20,font = ('monaco',15, 'bold')).grid(row=3, column=1, padx=30, pady=5)
        Entry(self.addf,textvariable = self.age,width=20,font = ('monaco',15, 'bold')).grid(row=4, column=1, padx=30, pady=5)
        Entry(self.addf,textvariable = self.birthdate,width=20,font = ('monaco',15, 'bold')).grid(row=5, column=1, padx=30, pady=5)
        Entry(self.addf,textvariable = self.gender,width=20,font = ('monaco',15, 'bold')).grid(row=6, column=1, padx=30, pady=10)
        Entry(self.addf,textvariable = self.address,width=20,font = ('monaco',15, 'bold')).grid(row=7, column=1, padx=30, pady=10)
        Entry(self.addf,textvariable = self.email,width=20,font = ('monaco',15, 'bold')).grid(row=8, column=1, padx=30, pady=10)
        Entry(self.addf,textvariable = self.contact,width=20,font = ('monaco',15, 'bold')).grid(row=9, column=1, padx=30, pady=10)
        
        Entry(self.addf,textvariable = self.selectbox,width=20,font = ('monaco',15, 'bold')).grid(row=1, column=5, padx=30, pady=10)

        #textboxlabels dito
        Label(self.addf,text= "Last Name             ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=1,column=0)
        Label(self.addf,text= "First Name            ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=2,column=0)
        Label(self.addf,text= "Middle Name           ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=3,column=0)
        Label(self.addf,text= "Age                   ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=4,column=0)
        Label(self.addf,text= "Birthdate (mm/dd/yyyy)",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=5,column=0)
        Label(self.addf,text= "Gender                ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=6,column=0)
        Label(self.addf,text= "Address               ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=7,column=0)
        Label(self.addf,text= "Email                 ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=8,column=0)
        Label(self.addf,text= "Contact Number        ",anchor="e", justify="left",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=9,column=0)

        Label(self.addf,text= "Select ID",anchor="w", justify="right",font = ('monaco',16, 'bold'),fg = 'yellow',bg ='black').grid(row=1,column=4)
        
        
        #submit btn 
        Button(self.addf, text="Add Record to DataBase", command = self.submit,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
        #show button
        #delete button
        Button(self.addf, text="Delete Record", command = self.delete,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =2, column = 5, columnspan = 5, pady = 5,padx=10, ipadx=34)
        #update btn
        Button(self.addf, text="Edit Record", command = self.edit,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =3, column = 5, columnspan = 5, pady = 5,padx=10, ipadx=47)
        # search id btn
        Button(self.addf, text="Search Record", command = self.search,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =4, column = 5, columnspan = 2, pady = 5,padx=10, ipadx=34)
        #train btn
        Button(self.addf, text="Train Images", command = self.train,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =24, column = 0, columnspan = 2, pady = 10,padx=10, ipadx=160)
        #show emp records btn
        Button(self.addf, text="Show Employee Records", command = self.query,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =24, column = 2, columnspan = 2, pady = 10,padx=10, ipadx=100)
        #time in btn
        Button(self.addf, text="Show Employee Time in", command = self.time,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =24, column = 4, columnspan = 2, pady = 10,padx=10, ipadx=50)
        #back btn
        Button(self.addf, text="Back", command = self.detect,font = ('monaco',15, 'bold'),fg ='yellow',bg = 'blue').grid(row =25, column = 2, columnspan = 2, pady = 10,padx=10, ipadx=105)
        self.addf.pack()
        

   
if __name__ == '__main__':
	#Create Object
	#and setup window
    root = Tk()
    root.title('Admin Window')
    root.iconbitmap('C:/Users/Ace/Desktop/1FACERECOGNITION/icons/face-recognition.ico')
    admin(root)
    root.mainloop()       

