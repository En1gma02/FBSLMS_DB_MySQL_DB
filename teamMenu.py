from tkinter import *
import mysql.connector
from queries import *

data = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class teamMenu:
   def __init__(self):
      self.root = Tk()
      self.root.geometry("300x340")
      self.root.title("Select Team")
      c.execute('SELECT t_name FROM team;')
      li = []
      for i in c.fetchall():
         li.append(str(i[0]))
      for i in li:
         Button(self.root,font=('Arial',12),text=i,command = lambda x = i: teamMenu.next(x,self.root)).pack(pady=5,fill='both')
      self.root.mainloop()
   def next(i,root):
      root.destroy()
      queries(i)
      teamMenu()
         
if __name__ == "__main__":
   teamMenu()
