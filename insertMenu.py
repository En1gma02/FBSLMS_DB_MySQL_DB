from tkinter import *
from tkinter import messagebox
import mysql.connector
#team->standings, player->contract, sponsor->in|financ, stadium, employee gonna be inserted

data = mysql.connector.connect(user='Dragon', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class insertMenu:
   def __init__(self):
      def team_fun(): #to league standings
         def insert():
            if t_var.get() == "Team" or c_var.get() == "Coach":
               self.win.destroy()
               messagebox.showerror(title="Error",message=f"All important fields not filled")
            else:
               try:
                  c.execute(f"SELECT COUNT(t_name) FROM league_standings;")
                  d = int(c.fetchone()[0])
                  c.execute(f'INSERT INTO team(t_name, t_coach) VALUES("{t_var.get()}","{c_var.get()}");')
                  c.execute(f'INSERT INTO league_standings(t_name,ls_rank,ls_matches,ls_points,ls_wins,ls_loss) VALUES("{t_var.get()}",{d+1},0,0,0,0);')
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
         self.win = Tk()
         t_var = StringVar(self.win,value="Team")
         c_var = StringVar(self.win,value="Coach")
         self.win.title("Team Insertion")
         t_label = Label(self.win, text="Team Name: ").pack()
         t_entry = Entry(self.win, textvariable=t_var).pack()
         c_label = Label(self.win, text="Coach Name: ").pack()
         c_entry = Entry(self.win, textvariable=c_var).pack()
         but = Button(self.win, text="Insert Value", command=insert).pack()
         self.win.mainloop()
      def player_fun(): #to contract
         def insert():
            if t_var.get() == "Player's Team" or p_var == "Player Name" or "Unassigned" in [pId_var.get(), pos_var.get(), stat_var.get(), stat_var.get(), fee_var.get()]:
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
         p_var = StringVar(self.win,value="Player Name")
         t_var = StringVar(self.win,value="Player's Team")
         pos_var = StringVar(self.win,value="Unassigned")
         stat_var = StringVar(self.win,value="Unassigned")
         dur_var = StringVar(self.win,value="1 year")
         fee_var = StringVar(self.win,value="[Numeric value]")
         self.win.title("Player Insertion")
         pId_label = Label(self.win, text="Player ID: ").pack()
         pId_entry = Entry(self.win, textvariable=pId_var).pack()
         p_label = Label(self.win, text="Player Name: ").pack()
         p_entry = Entry(self.win, textvariable=p_var).pack()
         t_option = OptionMenu(self.win,t_var, *li).pack()
         dur_option = OptionMenu(self.win, dur_var, *yr).pack()
         fee_label = Label(self.win, text="Player Fee: ").pack()
         fee_entry = Entry(self.win, textvariable=fee_var).pack()
         pos_label = Label(self.win, text="Player position: ").pack()
         pos_entry = Entry(self.win, textvariable=pos_var).pack()
         stat_label = Label(self.win, text="Player Statistics: ").pack()
         stat_entry = Entry(self.win, textvariable=stat_var).pack()
         but = Button(self.win, text="Insert Value", command=insert).pack()
         self.win.mainloop()
      def sponsors_fun(): #to in|fin
         def insert():
            if t_var.get() == "Team Sponsored" or s_var == "Sponsor Name" or mon_var.get == "Provides":
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
         s_var = StringVar(self.win,value="Sponsor Name")
         t_var = StringVar(self.win,value="Team Sponsored")
         ty_var = StringVar(self.win,value="Financial Sponsor")
         dur_var = StringVar(self.win,value="2 years")
         mon_var = StringVar(self.win,value="Provides")
         self.win.title("Sponsor Insertion")
         s_label = Label(self.win, text="Sponsor Name: ").pack()
         s_entry = Entry(self.win, textvariable=s_var).pack()
         mon_label = Label(self.win, text="Services or amount: ").pack()
         mon_entry = Entry(self.win, textvariable=mon_var).pack()
         t_option = OptionMenu(self.win,t_var, *li).pack()
         ty_option = OptionMenu(self.win,ty_var, *ty).pack()
         dur_option = OptionMenu(self.win, dur_var, *yr).pack()
         but = Button(self.win, text="Insert Value", command=insert).pack()
         self.win.mainloop()
      def stadium_fun(): 
         def insert():
            if s_var.get() == "Stadium" or loc_var == "Unassigned" or "[Numeric value]" in [cap_var.get(), cost_var.get()]:
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
         s_var = StringVar(self.win,value="Stadium")
         loc_var = StringVar(self.win,value="Unassigned")
         cap_var = StringVar(self.win,value="[Numeric value]")
         cost_var = StringVar(self.win,value="[Numeric value]")
         self.win.title("Stadium Insertion")
         s_label = Label(self.win, text="Stadium Name: ").pack()
         s_entry = Entry(self.win, textvariable=s_var).pack()
         loc_label = Label(self.win, text="Location: ").pack()
         loc_entry = Entry(self.win, textvariable=loc_var).pack()
         cap_label = Label(self.win, text="Stadium Capacity: ").pack()
         cap_entry = Entry(self.win, textvariable=cap_var).pack()
         cost_label = Label(self.win, text="Stadium cost: ").pack()
         cost_entry = Entry(self.win, textvariable=cost_var).pack()
         but = Button(self.win, text="Insert Value", command=insert).pack()
         self.win.mainloop()
      def emp_fun():
         def insert():
            if e_var.get() == "Name" or mon_var.get() == "[Numeric value]":
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
         e_var = StringVar(self.win,value="Name")
         mon_var = StringVar(self.win,value="[Numeric Value]")
         self.win.title("Employee Insertion")
         e_label = Label(self.win, text="Employee Name: ").pack()
         e_entry = Entry(self.win, textvariable=e_var).pack()
         mon_label = Label(self.win, text="Salary: ").pack()
         mon_entry = Entry(self.win, textvariable=mon_var).pack()
         but = Button(self.win, text="Insert Value", command=insert).pack()
         self.win.mainloop()
      
      self.root = Tk()
      self.root.title("Insert Window")
      self.label = Label(self.root,text="Select relation to be inserted").pack()
      self.team_but = Button(self.root,text = "Team",command=team_fun).pack()
      self.stad_but = Button(self.root,text = "Stadium",command=stadium_fun).pack()
      self.spon_but = Button(self.root,text = "Sponsor",command=sponsors_fun).pack()
      self.emp_but = Button(self.root,text = "League Employee",command=emp_fun).pack()
      self.pla_but = Button(self.root,text = "Player",command=player_fun).pack()
      self.root.mainloop()
      
if __name__ == "__main__":
   insertMenu()