from tkinter import *
import mysql.connector
from teamMenu import *
from adminMenu import *

log = mysql.connector.connect(user='Dragon', password='1234',host='localhost',database='pass_log')
c = log.cursor()

class login:
   flag = True
   u = False
   def __init__(self):
      self.root = Tk()
      self.root.title("Hi")
      self.u = BooleanVar()
      self.user_var = StringVar(self.roots)
      self.pass_var = StringVar(self.root)
      self.user_label = Label(self.root,text='Username: ').pack()
      self.user_field = Entry(self.root,textvariable=self.user_var).pack()
      self.pass_label = Label(self.root,text='Password: ').pack()
      self.user_field = Entry(self.root,show='*',textvariable=self.pass_var).pack()
      self.submit = Button(self.root, text='Login',command=self.verify).pack()
      self.fan = Radiobutton(self.root,text="Fan",variable=self.u,value=True,command=lambda x=True: ufo(x)).pack()
      self.admin = Radiobutton(self.root,text="Admin",state="normal",variable=self.u,value=False,command=lambda x=False:ufo(x)).pack()
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
