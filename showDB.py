#_*_ coding:utf-8 _*_
from tkinter import *
from connectDB import cur, conn
from tkinter import messagebox

root = Tk()
root.title("세계 나라")
root.geometry("600x320")

p = 0 # 페이지 번호 0은 1페이지
page = 0 # 전체 페이지

bs = []
entrys = []



def rec_edit(r1,r2,r3,r4, r5) :
    
    print(entrys[r1].get(), entrys[r2].get(), entrys[r3].get(), entrys[r4].get(),entrys[r5].get() )
    
    sql = f'update worldPopulation set 국가 = "{entrys[r3].get()}" where 국가코드 = "{entrys[r2].get()}" '
    
    cur.execute(sql)
    conn.commit()
    
    messagebox.showinfo("레코드 변경", "레코드를 수정했습니다.")
    pageShow(p)


    
def next_page() :
    global p, page

    if p < page-1 :
        p = p + 1
        pageShow(p)
    ps.set(str(p+1) + " / " + str(page))
        
def prv_page() :
    global p, page

    if p > 0 :
        p = p - 1
        pageShow(p)
        
    ps.set(str(p+1) + " / " + str(page))
    
            
####################################################################################
def pageShow(p) :
    global page, bs, entrys
    bs=[]
    entrys=[]
   
    cur.execute("select * from worldPopulation order by 순번 asc")
    total_page = len(cur.fetchall()) # 레코드 수
    limit_page = 10 # 한페이지에 보여줄 레코드 수
    page = round(total_page/limit_page) # 총 페이지 수
    
    
    sql = "select * from worldPopulation order by 순번 asc limit %s OFFSET %s"
    cur.execute(sql, (limit_page, p * limit_page))

    for i in range(1,11) :
        row = cur.fetchone()
        
        for j in range(5):
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
           
            if row != None :
                e.insert(END, row[j])
                entrys.append(e)
                
                
            else :
                e.insert(END, "")
                entrys.append(e)
                
        b = Button(root, text="Edit")
        b.grid(row=i, column = 5, padx=5)
        
        bs.append(b)
     

    bs[0].configure(command=lambda : rec_edit(0,1,2,3,4))
    bs[1].configure(command=lambda : rec_edit(5,6,7,8,9))
    bs[2].configure(command=lambda : rec_edit(10,11,12,13,14))
    bs[3].configure(command=lambda : rec_edit(15,16,17,18,19))
    bs[4].configure(command=lambda : rec_edit(20,21,22,23,24))
    bs[5].configure(command=lambda : rec_edit(25,26,27,28,29))
    bs[6].configure(command=lambda : rec_edit(30,31,32,33,34))
    bs[7].configure(command=lambda : rec_edit(35,36,37,38,39))
    bs[8].configure(command=lambda : rec_edit(40,41,42,43,44))
    bs[9].configure(command=lambda : rec_edit(45,46,47,48,49))            
                    
        
####################################################################################



####################################################################################
e=Label(root, width=5, text="순번", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=0, pady=3)

e=Label(root, width=10, text="국가코드", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=1, pady=3)

e=Label(root, width=20, text="국가", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=2, pady=3)

e=Label(root, width=20, text="수도", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=3, pady=3)

e=Label(root, width=20, text="인구", relief='ridge', anchor='w', bg='yellow')
e.grid(row=0, column=4, pady=3)
####################################################################################

pageShow(p)

####################################################################################
btnFrame = Frame(root)
btnFrame.grid(row=11,column=0, columnspan=5)

prv_btn = Button(btnFrame, text="<", command=prv_page)
prv_btn.pack(side=LEFT, padx=10)

ps = StringVar()
ps.set(str(p+1) + " / " + str(page))
page_state = Label(btnFrame, textvariable =  ps )
page_state.pack(side=LEFT, padx=10 )

next_btn = Button(btnFrame, text=">", command=next_page)
next_btn.pack(side=LEFT, padx=10)
####################################################################################



root.mainloop()
