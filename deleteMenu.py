from tkinter import *
from tkinter import messagebox
import mysql.connector
#team, stadium, sponsors, player, matches, contract, league_emp gonna be deleted

data = mysql.connector.connect(user='Dragon', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class deleteMenu():
   def __init__(self):
      def fun(n):
         nam = ["Team","Stadium","Sponsor","League Employee","Player"]
         tab = ["team","stadium","sponsors","league_employees","player"]
         key = ["t_name","s_name","sp_name","e_name","p_name"]
         def dele():
            if va.get() == "None":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"{nam[n]} not selected")
            else:
               try:
                  c.execute(f'DELETE FROM team WHERE {key[n]} = "{va.get()}";')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Succesfull",message=f"{nam[n]} {va.get()} was sucessfully deleted")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The {nam[n]} could not be deleted")
         c.execute(f'SELECT {key[n]} FROM {tab[n]};')
         li = []
         for i in c.fetchall():
            li.append(str(i[0]))
         self.win = Tk()
         va = StringVar(self.win, value="None")
         self.win.title(f"{nam[n]} Deletion")
         l = Label(self.win,text=f"Select a {nam[n]}: ").pack()
         o = OptionMenu(self.win, va, *li).pack()
         b = Button(self.win,text="Delete",command=dele).pack()
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
         va = StringVar(self.win, value="None")
         self.win.title(f"Contract Deletion")
         l = Label(self.win,text=f"Select player whose contract you want to delete: ").pack()
         o = OptionMenu(self.win, va, *li).pack()
         b = Button(self.win,text="Delete",command=dele).pack()
         self.win.mainloop()
      self.root = Tk()
      self.root.title("Delete Window")
      self.label = Label(self.root,text="Select relation to be deleted").pack()
      self.team_but = Button(self.root,text = "Team",command=lambda x=0: fun(x)).pack()
      self.stad_but = Button(self.root,text = "Stadium",command=lambda x=1: fun(x)).pack()
      self.spon_but = Button(self.root,text = "Sponsor",command=lambda x=2: fun(x)).pack()
      self.emp_but = Button(self.root,text = "League Employee",command=lambda x=3: fun(x)).pack()
      self.emp_pla = Button(self.root,text = "Player",command=lambda x=4: fun(x)).pack()
      self.con_but = Button(self.root,text = "Contract",command=con_fun).pack()
      self.root.mainloop()
      

if __name__ == "__main__":
   deleteMenu() 