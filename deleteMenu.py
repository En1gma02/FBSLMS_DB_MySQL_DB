from tkinter import *
from tkinter import messagebox
import mysql.connector
#team, stadium, sponsors, player, matches, contract, league_emp gonna be deleted

data = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class deleteMenu():
   def __init__(self):
      def fun(n):
         nam = ["Team","Stadium","Sponsor","Employee","Player"]
         tab = ["team","stadium","sponsors","league_employees","player"]
         key = ["t_name","s_name","sp_name","e_name","p_name"]
         def dele():
            if va.get() == "None":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"{nam[n]} not selected")
            else:
               try:
                  c.execute(f'DELETE FROM {tab[n]} WHERE {key[n]} = "{va.get()}";')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Succesfull",message=f"{nam[n]} {va.get()} was sucessfully deleted")
               except:
                  print(nam[n],va.get(),key[n],tab[n])
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The {nam[n]} could not be deleted")
         c.execute(f'SELECT {key[n]} FROM {tab[n]};')
         li = []
         for i in c.fetchall():
            li.append(str(i[0]))
         self.win = Tk()
         va = StringVar(self.win, value="None")
         self.win.title("")
         self.win.geometry("220x100")
         l = Label(self.win,text=f"Delete {nam[n]}: ",font=('Arial',11)).place(x=7,y=10)
         o = OptionMenu(self.win, va, *li).place(x=125,y=6)
         b = Button(self.win,text="Delete",font=('Arial',11),command=dele).place(x=70,y=50)
         self.win.mainloop()
      def con_fun():
         def dele():
            if va.get() == "None":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"Contract's Player not selected")
            else:
               try:
                  c.execute(f'SELECT p_id FROM player WHERE p_name = "{va.get()}";')
                  d = c.fetchone()[0]
                  print(d)
                  c.execute(f'DELETE FROM contract WHERE p_id = "{d}";')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Succesfull",message=f"{va.get()}'s contract was sucessfully deleted")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The player's contract could not be deleted")
         c.execute(f'SELECT c.p_id, p_name from contract c,player p where p.p_id = c.p_id;')
         li = []
         for i in c.fetchall():
            li.append(i[1])
         self.win = Tk()
         self.win.geometry("200x100")
         va = StringVar(self.win, value="None")
         self.win.title("")
         l = Label(self.win,text="Delete Contract: ",font=('Arial',11)).place(x=10,y=10)
         o = OptionMenu(self.win, va, *li).place(x=120,y=6)
         b = Button(self.win,text="Delete",font=('Arial',11),command=dele).place(x=60,y=50)
         self.win.mainloop()
      self.root = Tk()
      self.root.geometry("300x350")
      self.root.title("Delete")
      self.team_but = Button(self.root,text = "Team",font=('Arial',13),command=lambda x=0: fun(x)).pack(pady=10)
      self.stad_but = Button(self.root,text = "Stadium",font=('Arial',13),command=lambda x=1: fun(x)).pack(pady=10)
      self.spon_but = Button(self.root,text = "Sponsor",font=('Arial',13),command=lambda x=2: fun(x)).pack(pady=10)
      self.emp_but = Button(self.root,text = "League Employee",font=('Arial',13),command=lambda x=3: fun(x)).pack(pady=10)
      self.emp_pla = Button(self.root,text = "Player",font=('Arial',13),command=lambda x=4: fun(x)).pack(pady=10)
      self.con_but = Button(self.root,text = "Contract",font=('Arial',13),command=con_fun).pack(pady=10)
      self.root.mainloop()
      

if __name__ == "__main__":
   deleteMenu() 
