from tkinter import *
import mysql.connector
from tkinter import messagebox
from showQ import *

data = mysql.connector.connect(user='aaron', password='1234',host='localhost',database='fbslms')
c = data.cursor()

class queries:
   def __init__(self,team):   
      userSees = ['Contracts of players',
                  'League Standings',
                  f'Past matches for {team}',
                  'Contract with the highest fees',
                  'Forward Players', 'Midfielders', 'Defenders', 'Goalkeepers',
                  'Goal Stats', 'Interception Stats', 'Assist Stats', 'Passing Stats', 'Tackle Stats', 'Clean Sheets Stats',
                  'Stadium with the largest capacity',
                  'Sponsor with the longest duration',
                  f'Sponsors In Kind for {team}',
                  f'Financial sponsors for {team}']#Insert heading of the fetched query here
      sql = [f"SELECT contract.*, player.p_name, team.t_name\
               FROM contract\
               JOIN player ON contract.p_id = player.p_id\
               JOIN team ON player.t_name = team.t_name\
               WHERE team.t_name = '{team}';", 
               "SELECT t_name, ls_rank, ls_points, ls_wins, ls_loss FROM league_standings ORDER BY ls_rank ASC;",
            f"SELECT matches.*, played_by.t_name, played_by.t_name2, played_by.winner\
               FROM matches\
               JOIN played_by ON matches.m_number = played_by.m_number\
               WHERE played_by.t_name = '{team}' OR played_by.t_name2 = '{team}';",
               "SELECT c_id, p_name, c_fees FROM contract JOIN player ON contract.p_id = player.p_id ORDER BY c_fees DESC LIMIT 5;",
               "SELECT * FROM player WHERE p_position = 'Forward';",
               "SELECT * FROM player WHERE p_position = 'Midfielder';",
               "SELECT * FROM player WHERE p_position = 'Defender';",      
               "SELECT * FROM player WHERE p_position = 'Goalkeeper';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Goals%';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Interceptions%';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Assists%';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Passing%';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Tackles%';",
               "SELECT p_name, p_stats FROM player WHERE p_stats LIKE '%Clean%';",
               "SELECT * FROM stadium ORDER BY s_capacity DESC LIMIT 5;",
               "SELECT sp_name, sp_duration FROM sponsors ORDER BY sp_duration DESC LIMIT 5;",
               "SELECT sponsors.*, IF(sp_type = 'i', ik.goodsServices, fn.amount) AS specialization\
               FROM sponsors\
               LEFT JOIN inKind ik ON sponsors.sp_name = ik.sp_name\
               LEFT JOIN financial fn ON sponsors.sp_name = fn.sp_name\
               WHERE sp_type = 'i';",
               "SELECT sponsors.*, IF(sp_type = 'i', ik.goodsServices, fn.amount) AS specialization\
               FROM sponsors\
               LEFT JOIN inKind ik ON sponsors.sp_name = ik.sp_name\
               LEFT JOIN financial fn ON sponsors.sp_name = fn.sp_name\
               WHERE sp_type = 'f';"]#write the code for the queries here
      col = [['Contract ID', 'Fees', 'Duration', 'Player ID', 'Name', 'Team'],
            ['Team', 'Rank', 'Points', 'Wins', 'Losses'],
            ['Match Number', 'Result', 'Match Time', 'Date', 'Stadium', 'Team1', 'Team 2', 'Winner'],
            ['Contract ID', 'Player Name', 'Fees'],
            ['Player ID', 'Name', 'Position', 'Stats', 'Team'],
            ['Player ID', 'Name', 'Position', 'Stats', 'Team'],
            ['Player ID', 'Name', 'Position', 'Stats', 'Team'],
            ['Player ID', 'Name', 'Position', 'Stats', 'Team'],
            ['Player Name', 'Stats'],
            ['Player Name', 'Stats'],
            ['Player Name', 'Stats'],
            ['Player Name', 'Stats'],
            ['Player Name', 'Stats'],
            ['Player Name', 'Stats'],
            ['Stadium', 'Location', 'Capacity', 'Cost'],
            ['Sponsor Name', 'Duration'],
            ['Sponsor Name', 'Duration', 'InKind', 'Team', 'Goods Sponsored'],
            ['Sponsor Name', 'Duration', 'Financial', 'Team', 'Funds Given']
            ]
      def query():
         try:
            i = userSees.index(var.get())
            c.execute(sql[i])
            d = c.fetchall()
            show(d,col[i],f"{userSees[i]} for team {team}")
         except:
            messagebox.showerror(title="Error",message="Please select a query")
      root = Tk()
      root.geometry("300x150")
      root.title("Fan Query")
      var = StringVar(root,"Query")
      men = OptionMenu(root,var,*userSees).pack(pady=10)
      but = Button(root,font=('Arial',12),text='Run Query',command=query).pack(pady=10)
      root.mainloop()


if __name__=="__main__":
   queries("Barcelona")
