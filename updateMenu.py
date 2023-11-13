from tkinter import *
from tkinter import messagebox
import mysql.connector
#team, player, employee, stadium, sponsor name;  gonna be updated

data = mysql.connector.connect(user='Dragon', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class updateMenu:
   def __init__(self):
      def update_fun(n):
         nam = ["Team","Stadium","Sponsor","League Employee","Player"]
         tab = ["team","stadium","sponsors","league_employees","player"]
         key = ["t_name","s_name","sp_name","e_name","p_name"]
         def update():
            if "None" in [names.get(),new.get()]:
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  c.execute(f'UPDATE {tab[n]} SET {key[n]} = "{new.get()}" WHERE {key[n]} = "{names.get()}";')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Inserted",message=f"Data inserted succesfully")
               except mysql.connector.errors.IntegrityError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Data already exits in realtion")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The required data could not be inserted")
         c.execute(f'SELECT {key[n]} FROM {tab[n]};')
         li = []
         for i in c.fetchall():
            li.append(str(i[0]))
         self.win = Tk()
         names = StringVar(self.win, value="None")
         new = StringVar(self.win, value="None")
         self.win.title(f"{nam[n]} Updation")
         l1 = Label(self.win,text=f"Select a {nam[n]}: ").pack()
         o = OptionMenu(self.win, names, *li).pack()
         l2 = Label(self.win,text=f"New name: ").pack()
         e = Entry(self.win,textvariable=new).pack()
         b = Button(self.win,text="Update",command=update).pack()
         self.win.mainloop()
      self.root = Tk()
      self.root.title("Update Window")
      self.label = Label(self.root,text="Select name to be updated").pack()
      self.team_but = Button(self.root,text = "Team",command=lambda x=0 : update_fun(x)).pack()
      self.stad_but = Button(self.root,text = "Stadium",command=lambda x=1 : update_fun(x)).pack()
      self.spon_but = Button(self.root,text = "Sponsor",command=lambda x=2 : update_fun(x)).pack()
      self.emp_but = Button(self.root,text = "League Employee",command=lambda x=3 : update_fun(x)).pack()
      self.pla_but = Button(self.root,text = "Player",command=lambda x=4 : update_fun(x)).pack()
      self.root.mainloop()
      
if __name__=="__main__":
   updateMenu()