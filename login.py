from tkinter import *
import mysql.connector
from teamMenu import *
from adminMenu import *

log = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='pass_log')
c = log.cursor()

class login:
   flag = True
   u = False
   def __init__(self):
      self.root = Tk()
      self.root.geometry("250x150")
      self.root.title("Login Page")
      self.u = BooleanVar()
      self.user_var = StringVar(self.root)
      self.pass_var = StringVar(self.root)
      self.user_label = Label(self.root,text='Username: ').place(x=20,y=20)
      self.user_field = Entry(self.root,textvariable=self.user_var).place(x=100,y=20)
      self.pass_label = Label(self.root,text='Password: ').place(x=20,y=50)
      self.user_field = Entry(self.root,show='*',textvariable=self.pass_var).place(x=100,y=50)
      self.submit = Button(self.root, text='Login',command=self.verify).place(x=100,y=110)
      self.access_label = Label(self.root,text='Access: ').place(x=20,y=80)
      self.fan = Radiobutton(self.root,text="Fan",variable=self.u,value=True,command=lambda x=True: ufo(x)).place(x=70,y=78)
      self.admin = Radiobutton(self.root,text="Admin",state="normal",variable=self.u,value=False,command=lambda x=False:ufo(x)).place(x=130,y=78)
      def ufo(x):
         login.u = x
      self.root.mainloop()
    
   def verify(self):
      c.execute(f'SELECT * FROM main WHERE username = "{self.user_var.get()}" AND pass = "{self.pass_var.get()}";')
      result = c.fetchone()
      if result:
         if login.u:
            self.root.destroy()
            teamMenu()
         else:
            if result[2] == '1':
               self.root.destroy()
               adminMenu()
            else:
               if(login.flag):
                  self.error_label = Label(self.root,text="Incorrect password/username/access level").pack()
                  login.flag = False
      else:
         if(login.flag):
            self.error_label = Label(self.root,text="Incorrect password/username/access level").pack()
            login.flag = False
      
if __name__=="__main__":
   login()
