from tkinter import *
from teamMenu import *
from deleteMenu import *
from insertMenu import *
from updateMenu import *

class adminMenu:
   def __init__(self):
      def up_call():
         self.root.destroy()
         updateMenu()
         adminMenu()
      def del_call():
         self.root.destroy()
         deleteMenu()
         adminMenu()
      def in_call():
         self.root.destroy()
         insertMenu()
         adminMenu()
      def fan():
         self.root.destroy()
         teamMenu()
         adminMenu()
      self.root = Tk()
      self.root.geometry("270x200")
      self.root.title("Admin Commands")
      self.up_but = Button(self.root,font=('Arial',12),text = "Update Command",command=up_call).place(x=60,y=20)
      self.del_but = Button(self.root,font=('Arial',12),text = "Delete Command",command=del_call).place(x=61,y=60)
      self.in_but = Button(self.root,font=('Arial',12),text = "Insert Command",command=in_call).place(x=62,y=100)
      self.fan = Button(self.root,font=('Arial',12),text="View as a Fan",command=fan).place(x=70,y=140)
      self.root.mainloop()
     
if __name__=="__main__":
   adminMenu()