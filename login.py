from tkinter import *
import mysql.connector

log = mysql.connector.connect(user='abc', password='1234',host='localhost',database='pass_log')
c = log.cursor()

class login:
   flag = True
   u = False
   def __init__(self,root):
      self.root = root
      self.u = BooleanVar()
      self.user_var = StringVar()
      self.pass_var = StringVar()
      self.f = Frame(root).pack()
      self.user_label = Label(root,text='Username: ').pack()
      self.user_field = Entry(root,textvariable=self.user_var).pack()
      self.pass_label = Label(root,text='Username: ').pack()
      self.user_field = Entry(root,show='*',textvariable=self.pass_var).pack()
      self.submit = Button(root, text='Login',command=self.verify).pack()
      self.fan = Radiobutton(root,text="Fan",variable=self.u,value=True,command=lambda x=True: ufo(x)).pack()
      self.admin = Radiobutton(root,text="Admin",state="normal",variable=self.u,value=False,command=lambda x=False:ufo(x)).pack()
      def ufo(x):
         login.u = x
    
   def verify(self):
      print(self.user_var.get(),self.pass_var.get())
      c.execute(f'SELECT * FROM main WHERE username = "{self.user_var.get()}" AND pass = "{self.pass_var.get()}";')
      result = c.fetchone()
      print(type(result))
      if result:
         if login.u:
            print("fan")
         else:
            if result[2] == '1':
               print("Admin")
               #call function for admin
            else:
               if(login.flag):
                  self.error_label = Label(self.root,text="Incorrect password/username/access level").pack()
                  login.flag = False
      else:
         if(login.flag):
            self.error_label = Label(self.root,text="Incorrect password/username/access level").pack()
            login.flag = False
      
window = Tk()
window.title("Hi")
ob = login(window)
window.mainloop()