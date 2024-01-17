from tkinter import *
from tkinter import messagebox
import mysql.connector
#team, player, employee, stadium, sponsor name;  gonna be updated

data = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class updateMenu:
   def __init__(self):
      def update_fun(n):
         nam = ["Team","Stadium","Sponsor","Employee","Player"]
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
                  messagebox.showinfo(title="Inserted",message=f"Data updated succesfully")
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
         self.win.geometry("360x130")
         names = StringVar(self.win, value="None")
         new = StringVar(self.win, value="None")
         self.win.title(f"{nam[n]} Updation")
         l1 = Label(self.win,font=('Arial',12),text=f"Select {nam[n]}: ").place(x=20,y=20)
         o = OptionMenu(self.win, names, *li).place(x=150,y=16)
         l2 = Label(self.win,font=('Arial',12),text=f"New name: ").place(x=20,y=50)
         e = Entry(self.win,font=('Arial',12),textvariable=new).place(x=150,y=50)
         b = Button(self.win,font=('Arial',12),text="Update",command=update).place(x=120,y=80)
         self.win.mainloop()
      self.root = Tk()
      self.root.geometry("300x290")
      self.root.title("Updation")
      self.team_but = Button(self.root,text = "Team",font=('Arial',13),command=lambda x=0 : update_fun(x)).pack(pady=10)
      self.stad_but = Button(self.root,text = "Stadium",font=('Arial',13),command=lambda x=1 : update_fun(x)).pack(pady=10)
      self.spon_but = Button(self.root,text = "Sponsor",font=('Arial',13),command=lambda x=2 : update_fun(x)).pack(pady=10)
      self.emp_but = Button(self.root,text = "League Employee",font=('Arial',13),command=lambda x=3 : update_fun(x)).pack(pady=10)
      self.pla_but = Button(self.root,text = "Player",font=('Arial',13),command=lambda x=4 : update_fun(x)).pack(pady=10)
      self.root.mainloop()
      
if __name__=="__main__":
   updateMenu()
