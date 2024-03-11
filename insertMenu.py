from tkinter import *
from tkinter import messagebox
import mysql.connector
#team->standings, player->contract, sponsor->in|financ, stadium, employee gonna be inserted

data = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class insertMenu:
   def __init__(self):
      def team_fun(): #to league standings
         def insert():
            if t_var.get() == "Team" or c_var.get() == "Coach":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               #try:
                  c.execute(f"SELECT COUNT(t_name) FROM league_standings;")
                  d = int(c.fetchone()[0])+1
                  c.execute(f'INSERT INTO team(t_name, t_coach) VALUES("{t_var.get()}","{c_var.get()}");')
                  c.execute(f'INSERT INTO league_standings(t_name,ls_rank,ls_matches,ls_points,ls_wins,ls_loss) VALUES("{t_var.get()}",{d},0,0,0,0);')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Inserted",message=f"Data inserted succesfully")
               # except mysql.connector.errors.IntegrityError:
               #    data.rollback()
               #    self.win.destroy()
               #    messagebox.showerror(title="Error",message=f"Data already exits in realtion")
               # except:
               #    data.rollback()
               #    self.win.destroy()
               #    messagebox.showerror(title="Error",message=f"The required data could not be inserted") 
         self.win = Tk()
         t_var = StringVar(self.win,value="Team")
         c_var = StringVar(self.win,value="Coach")
         self.win.title("Team Insertion")
         self.win.geometry("340x140")
         t_label = Label(self.win, font=('Arial',12), text="Team Name: ").place(x=20,y=20)
         t_entry = Entry(self.win, font=('Arial',12), textvariable=t_var).place(x=130,y=20)
         c_label = Label(self.win, font=('Arial',12), text="Coach Name: ").place(x=20,y=50)
         c_entry = Entry(self.win, font=('Arial',12), textvariable=c_var).place(x=130,y=50)
         but = Button(self.win, text="Insert Value", font=('Arial',12), command=insert).place(x=120,y=80)
         self.win.mainloop()
      def player_fun(): #to contract
         def insert():
            if "None" in [t_var.get(), p_var.get()] or "Unassigned" in [pId_var.get(), pos_var.get(), stat_var.get(), stat_var.get(), fee_var.get()]:
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  c.execute(f"SELECT COUNT(p_id) FROM contract;")
                  d = 'c'+str(int(c.fetchone()[0])+1)
                  c.execute(f'INSERT INTO player(p_id,p_name,p_position,p_stats,t_name) VALUES ("{pId_var.get()}","{p_var.get()}","{pos_var.get()}","{stat_var.get()}","{t_var.get()}");')
                  c.execute(f'INSERT INTO contract(c_id,c_fees,c_duration,p_id) VALUES ("{d}",{int(fee_var.get())},"{dur_var.get()}","{pId_var.get()}");')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Inserted",message=f"Data inserted succesfully")
               except mysql.connector.errors.IntegrityError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Data already exits in realtion")
               except ValueError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Please input numeric data in the Fee field")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The required data could not be inserted") 
         c.execute("SELECT t_name FROM team;")
         yr = ["1 year","2 years", "3 years", "4 years"]
         li = []
         for i in c.fetchall():
            li.append(str(i[0]))
         self.win = Tk()
         pId_var = StringVar(self.win,value="Unassigned")
         p_var = StringVar(self.win,value="None")
         t_var = StringVar(self.win,value="None")
         pos_var = StringVar(self.win,value="Unassigned")
         stat_var = StringVar(self.win,value="Unassigned")
         dur_var = StringVar(self.win,value="1 year")
         fee_var = StringVar(self.win,value="[Numeric value]")
         
         self.win.title("Player Insertion")
         self.win.geometry("370x330")
         pId_label = Label(self.win, font=('Arial',12), text="Player ID: ").place(x=20,y=0)
         pId_entry = Entry(self.win, font=('Arial',12), textvariable=pId_var).place(x=155,y=0)
         p_label = Label(self.win, font=('Arial',12), text="Player Name: ").place(x=20,y=40)
         p_entry = Entry(self.win, font=('Arial',12), textvariable=p_var).place(x=155,y=40)
         p_label = Label(self.win, font=('Arial',12), text="Player Team: ").place(x=20,y=80)
         t_option = OptionMenu(self.win,t_var, *li).place(x=155,y=78)
         p_label = Label(self.win, font=('Arial',12), text="Contract Duration: ").place(x=20,y=120)
         dur_option = OptionMenu(self.win, dur_var, *yr).place(x=155,y=118)
         fee_label = Label(self.win, font=('Arial',12), text="Player Fee: ").place(x=20,y=160)
         fee_entry = Entry(self.win, font=('Arial',12), textvariable=fee_var).place(x=155,y=160)
         pos_label = Label(self.win, font=('Arial',12), text="Player position: ").place(x=20,y=200)
         pos_entry = Entry(self.win,font=('Arial',12), textvariable=pos_var).place(x=155,y=200)
         stat_label = Label(self.win, font=('Arial',12),text="Player Statistics: ").place(x=20,y=240)
         stat_entry = Entry(self.win,font=('Arial',12), textvariable=stat_var).place(x=155,y=240)
         but = Button(self.win, text="Insert Value",font=('Arial',12), command=insert).place(x=100,y=280)
         self.win.mainloop()
      def sponsors_fun(): #to in|fin
         def insert():
            if "None" in [t_var.get(),s_var.get(),mon_var.get()]:
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  if ty_var.get() == "Financial Sponsor":
                     c.execute(f'INSERT INTO sponsors(sp_name,sp_duration,sp_type,t_name) VALUES ("{s_var.get()}","{dur_var.get()}","f","{t_var.get()}");')
                     c.execute(f'INSERT INTO financial(sp_name, amount) VALUES ("{s_var.get()}","{mon_var.get()}");')
                  else:
                     c.execute(f'INSERT INTO sponsors(sp_name,sp_duration,sp_type,t_name) VALUES ("{s_var.get()}","{dur_var.get()}","i","{t_var.get()}");')
                     c.execute(f'INSERT INTO inKind(sp_name, goodsServices) VALUES ("{s_var.get()}","{mon_var.get()}");')
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
         c.execute("SELECT t_name FROM team;")
         yr = ["1 year","2 years", "3 years", "4 years","5 years", "6 years", "7 years", "8 years", "9 years", "10 years"]
         ty = ["In Kind Sponsor", "Financial Sponsor"]
         li = []
         for i in c.fetchall():
            li.append(str(i[0]))
         self.win = Tk()
         self.win.geometry("370x270")
         s_var = StringVar(self.win,value="None")
         t_var = StringVar(self.win,value="None")
         ty_var = StringVar(self.win,value="Financial Sponsor")
         dur_var = StringVar(self.win,value="2 years")
         mon_var = StringVar(self.win,value="None")
         self.win.title("Sponsor Insertion")
         s_label = Label(self.win, font=('Arial',13),text="Sponsor Name: ").place(x=20,y=0)
         s_entry = Entry(self.win, font=('Arial',13),textvariable=s_var).place(x=155,y=0)
         mon_label = Label(self.win, font=('Arial',13),text="Services/Amount: ").place(x=20,y=40)
         mon_entry = Entry(self.win,font=('Arial',13), textvariable=mon_var).place(x=155,y=40)
         t_label = Label(self.win, font=('Arial',13),text="Sponsored team: ").place(x=20,y=80)
         t_option = OptionMenu(self.win,t_var, *li).place(x=155,y=78)
         ty_label = Label(self.win,font=('Arial',13), text="Sponsor Type: ").place(x=20,y=120)
         ty_option = OptionMenu(self.win,ty_var, *ty).place(x=155,y=118)
         dur_label = Label(self.win, font=('Arial',13),text="Sponsor Duration: ").place(x=20,y=160)
         dur_option = OptionMenu(self.win, dur_var, *yr).place(x=155,y=158)
         but = Button(self.win, text="Insert Value", font=('Arial',13),command=insert).place(x=100,y=200)
         self.win.mainloop()
      def stadium_fun(): 
         def insert():
            if s_var.get() == "None" or loc_var == "Unassigned" or "[Numeric value]" in [cap_var.get(), cost_var.get()]:
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  c.execute(f'INSERT INTO stadium(s_name,s_location,s_capacity,s_cost) VALUES ("{s_var.get()}","{loc_var.get()}",{int(cap_var.get())},{int(cost_var.get())});')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Inserted",message=f"Data inserted succesfully")
               except mysql.connector.errors.IntegrityError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Data already exits in realtion")
               except ValueError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Please input numeric data in the required fields")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The required data could not be inserted") 
         self.win = Tk()
         self.win.geometry("370x200")
         s_var = StringVar(self.win,value="None")
         loc_var = StringVar(self.win,value="Unassigned")
         cap_var = StringVar(self.win,value="[Numeric value]")
         cost_var = StringVar(self.win,value="[Numeric value]")
         self.win.title("Stadium Insertion")
         s_label = Label(self.win, font=('Arial',13), text="Stadium Name: ").place(x=20,y=0)
         s_entry = Entry(self.win, font=('Arial',13), textvariable=s_var).place(x=158,y=0)
         loc_label = Label(self.win,  font=('Arial',13),text="Location: ").place(x=20,y=40)
         loc_entry = Entry(self.win, font=('Arial',13), textvariable=loc_var).place(x=158,y=40)
         cap_label = Label(self.win, font=('Arial',13), text="Stadium Capacity: ").place(x=20,y=80)
         cap_entry = Entry(self.win,  font=('Arial',13),textvariable=cap_var).place(x=158,y=78)
         cost_label = Label(self.win,  font=('Arial',13),text="Stadium cost: ").place(x=20,y=120)
         cost_entry = Entry(self.win,  font=('Arial',13),textvariable=cost_var).place(x=158,y=118)
         but = Button(self.win,  font=('Arial',13),text="Insert Value", command=insert).place(x=100,y=160)
         self.win.mainloop()
      def emp_fun():
         def insert():
            if e_var.get() == "None" or mon_var.get() == "[Numeric value]":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  c.execute(f"SELECT COUNT(e_id) FROM league_employees;")
                  d = int(c.fetchone()[0])+1
                  c.execute(f'INSERT INTO league_employees(e_id,e_name,e_salary) VALUES ({d},"{e_var.get()}",{int(mon_var.get())});')
                  data.commit()
                  self.win.destroy()
                  messagebox.showinfo(title="Inserted",message=f"Data inserted succesfully")
               except mysql.connector.errors.IntegrityError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Data already exits in realtion")
               except ValueError:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"Please input numeric data in the salary field")
               except:
                  data.rollback()
                  self.win.destroy()
                  messagebox.showerror(title="Error",message=f"The required data could not be inserted") 
         self.win = Tk()
         self.win.geometry("300x140")
         e_var = StringVar(self.win,value="None")
         mon_var = StringVar(self.win,value="[Numeric Value]")
         self.win.title("Employee Insertion")
         e_label = Label(self.win, font=('Arial',13), text="Name: ").place(x=20,y=20)
         e_entry = Entry(self.win, font=('Arial',13), textvariable=e_var).place(x=80,y=20)
         mon_label = Label(self.win, font=('Arial',13), text="Salary: ").place(x=20,y=50)
         mon_entry = Entry(self.win, font=('Arial',13), textvariable=mon_var).place(x=80,y=50)
         but = Button(self.win, text="Insert Value", font=('Arial',13), command=insert).place(x=90,y=80)
         self.win.mainloop()
      
      self.root = Tk()
      self.root.geometry("300x290")
      self.root.title("Insertion")
      self.team_but = Button(self.root,text = "Team",font=('Arial',13),command=team_fun).pack(pady=10)
      self.stad_but = Button(self.root,text = "Stadium",font=('Arial',13),command=stadium_fun).pack(pady=10)
      self.spon_but = Button(self.root,text = "Sponsor",font=('Arial',13),command=sponsors_fun).pack(pady=10)
      self.emp_but = Button(self.root,text = "League Employee",font=('Arial',13),command=emp_fun).pack(pady=10)
      self.pla_but = Button(self.root,text = "Player",font=('Arial',13),command=player_fun).pack(pady=10)
      self.root.mainloop()
      
if __name__ == "__main__":
   insertMenu()
