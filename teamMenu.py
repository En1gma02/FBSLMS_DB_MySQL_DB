from tkinter import *
import mysql.connector

data = mysql.connector.connect(user='Dragon', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class teamMenu:
   def __init__(self):
      self.root = Tk()
      self.root.title("Team Window")
      c.execute('SELECT t_name FROM team;')
      li = []
      for i in c.fetchall():
         li.append(str(i[0]))
      Label(self.root, text="Select a Team").pack()
      for i in li:
         Button(self.root,text=i,command = lambda x = i: teamMenu.next(x,self.root)).pack()
      self.root.mainloop()
   def next(i,root):
      root.withdraw()
      print(i)
      root.wm_deiconify()
         
if __name__ == "__main__":
   teamMenu()