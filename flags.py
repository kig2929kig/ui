from tkinter import *
from tkinter import filedialog
from connectDB import cur, conn

root = Tk()
root.title("나라별 국기")
root.geometry("250x280")

############################################
# button function - start
def findImg() :
   country_Entry.delete(0,END) 
   imgFile = filedialog.askopenfilename(
       initialdir = 'path', \
       title = 'select file', \
       filetypes = (('png','*.png'),) )
   code = imgFile[-6:-4]

   sql = f"select * from worldPopulation where 국가코드 ='{code}'"
   cur.execute(sql)
   country = cur.fetchone()[2]
   country_Entry.insert(END, country)

# button function -end
############################################
# Frame - start
topFrame = Frame(root)
topFrame.pack()
imgFrame = Frame(root)
imgFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
# Frame - end
############################################
# topFrame - start                         
country_Lbl = Label(topFrame, text="국가", relief="ridge") 
country_Lbl.pack(side=LEFT, padx=5, pady=5)                

country = StringVar()
country_Entry = Entry(topFrame, textvariable=country)
country_Entry.pack(side=LEFT,padx=5, pady=5)

findBtn = Button(topFrame, text="찾기", command=findImg)
findBtn.pack(side=LEFT, padx=5, pady=5)
# topFrame - end                           
############################################
# imgFrame - start
imgFlag = PhotoImage()
imgLbl = Label(imgFrame, image = imgFlag, bg='yellow')
imgLbl.configure(width=200, height=200)
imgLbl.pack()
# imgFrame - end
############################################
# bottomFrame - start
prev_btn = Button(bottomFrame, text="<")
prev_btn.pack(side=LEFT, padx=5, pady=5)

page_Lbl = Label(bottomFrame, text="1 / 198")
page_Lbl.pack(side=LEFT, padx=15, pady=5)

next_btn = Button(bottomFrame, text=">")
next_btn.pack(side=LEFT, padx=5, pady=5)
# bottomFrame - end
############################################

root.mainloop()
