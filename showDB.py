#_*_ coding:utf-8 _*_
from tkinter import *
from connectDB import cur, conn

root = Tk()
root.title("세계 나라")
root.geometry("600x400")

page = 1
####################################################################################
e=Label(root, width=5, text="순번", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=0)

e=Label(root, width=10, text="국가코드", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=1)

e=Label(root, width=20, text="나라", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=2)

e=Label(root, width=20, text="수도", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=3)

e=Label(root, width=20, text="인구", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=4)
####################################################################################
cur.execute("select * from worldPopulation order by 순번 asc")
i=1
for row in cur :
    for j in range(len(row)):
        e = Entry(root)
        if j==0 :
            e.configure(width=5)
        elif j==1 :
            e.configure(width=10)
        elif j==2 :
            e.configure(width=20)
        elif j==3 :
            e.configure(width=20)
        elif j==4 :
            e.configure(width=20)
        e.grid(row=i, column = j)
        e.insert(END, row[j])
    i=i+1
####################################################################################
root.mainloop()
