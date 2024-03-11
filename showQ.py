import pandas as pd
import tkinter  as tk 
from tkinter import *
from tkinter import ttk


class show:
    def __init__(self,data,col,tit):
        def trv_refresh(): 
            style = ttk.Style()
            style.configure('my.Treeview.Heading', background='gray', font=('Arial Bold', 10))
            r_set=df.to_numpy().tolist() 
            trv=ttk.Treeview(my_w,selectmode='browse',height=10,show='headings',columns=l1,style='my.Treeview')
            trv.grid(row=4,column=1,columnspan=3,padx=10,pady=20)
            for i in l1:
                trv.column(i,width=150,anchor='c')
                trv.heading(i,text=str(i))
            for dt in r_set:
                v=[r for r in dt]
                trv.insert("",'end',iid=v[0],values=v)
                
            vs = ttk.Scrollbar(my_w,orient="vertical", command=trv.yview)
            trv.configure(yscrollcommand=vs.set) 
            vs.grid(row=4,column=4,sticky='ns') 
        df = pd.DataFrame(data,columns=col)
        l1=list(df)


        my_w = tk.Tk()
        my_w.geometry(f"{df.shape[1]*160}x260")  
        my_w.title(tit)
        trv_refresh() 
        my_w.mainloop()  
        
if __name__ == "__main__":    
    test1 = [('Marc-Andre ter Stegen', 'Goalkeeper', 'Clean Sheets: 15'), ('Gavi', 'Midfielder', 'Passing Accuracy: 88%'), ('Pedri Gonzalez', 'Midfielder', 'Goals: 8'), ('Frenkie de Jong', 'Midfielder', 'Assists: 10'), ('Yamal Khoukhi', 'Midfielder', 'Assists: 15'), ('Joao Cancelo', 'Defender', 'Assists: 5'), ('Boubacar Kamara', 'Defender', 'Clean Sheets: 12'), ('Ronald Araujo', 'Defender', 'Interceptions: 25'), ('Jules Kounde', 'Defender', 'Tackles: 30'), ('Joao Felix', 'Forward', 'Goals: 18'), ('Robert Lewandowski', 'Forward', 'Goals: 25')]
    test2 = ["Name","Position","Stats"]
    tit = "All players"
    show(test1,test2,tit)