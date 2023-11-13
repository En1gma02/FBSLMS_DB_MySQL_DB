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
      self.root.title("Admin Window")
      self.up_but = Button(self.root,text = "Update",command=up_call).pack()
      self.del_but = Button(self.root,text = "Delete",command=del_call).pack()
      self.in_but = Button(self.root,text = "Insert",command=in_call).pack()
      self.fan = Button(self.root,text="View as Fan",command=fan).pack()
      self.root.mainloop()
     
if __name__=="__main__":
   adminMenu()