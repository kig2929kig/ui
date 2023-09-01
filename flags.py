from tkinter import *
from tkinter import filedialog
from connectDB import cur, conn
from PIL import Image, ImageTk
import base64
from io import BytesIO

root = Tk()
root.title("나라별 국기")
root.geometry("250x280")

startPage = 1
totalPage = 0
img = None
code = ""

sql = "select count(*) from worldPopulation"
cur.execute(sql)
totalPage = cur.fetchone()[0]

############################################
# button function - start

##### img resize - start #####
def img_resize(startPage) :
    sql = f"select * from flag where 순번 = {startPage}"
    cur.execute(sql)
    try :
        no, code, get_img = cur.fetchone()
        print(no, code)
        if get_img == None :
            pass
        else :        
            get_img = base64.b64decode(get_img)
            get_img = Image.open(BytesIO(get_img))
                
            resizedImg = get_img.resize((200, 200))
            resizedImg = ImageTk.PhotoImage(resizedImg)
            imgLbl.configure(image = resizedImg)
            imgLbl.image = resizedImg
        
    except Exception as e :
        print(e)
     

##### img resize - end #####

##### saveImg func - start
def saveImg() :
    global code
    print(code)
    imgFileName = code + ".png"

    with open(imgFileName, "rb") as image :
        binary_image = image.read()
    binary_image = base64.b64encode(binary_image)
    binary_image = binary_image.decode('UTF-8')

    sql = f"select * from worldPopulation where 국가코드='{code}'"
    cur.execute(sql)
    no, code, country, city, population = cur.fetchone() 
    print(no, code, country, city, population)
    
    sql = "insert into flag values(%s, %s, %s)"
    cur.execute(sql, (no, code, binary_image))
    conn.commit()
##### saveImg func - end

##### findImg func - start
def findImg() :
   global startPage, img, code
   
   country_Entry.delete(0,END) 
   imgFile = filedialog.askopenfilename(
       initialdir = 'path', \
       title = 'select file', \
       filetypes = (('png','*.png'),) )
   code = imgFile[-6:-4]

   sql = f"select * from worldPopulation where 국가코드 ='{code}'"
   cur.execute(sql)
   result = cur.fetchone()
   country = result[2]
   country_Entry.insert(END, country)

   #img resized - start
   img = Image.open(imgFile)
   resizedImg = img.resize((200, 200))
   resizedImg = ImageTk.PhotoImage(resizedImg)
   imgLbl.configure(image = resizedImg)
   imgLbl.image = resizedImg
   #img reized -end
   
   startPage = result[0]
   pageView.set(str(startPage) + " / " + str(totalPage))
##### findImg func - end

##### prevPage func - start
def prevPage() :
    global startPage
        
    if startPage > 1 :
        startPage = startPage - 1
    pageView.set(str(startPage) + " / " + str(totalPage))
    sql = f"select * from worldPopulation where 순번 ='{startPage}'"
    cur.execute(sql)

    no, code, country, city, population = cur.fetchone() 
    print(no, code, country, city, population)
   
    country_Entry.delete(0,END)
    country_Entry.insert(END, country)
    imgLbl.configure(image = imgTemp)
    img_resize(startPage)
    
##### prevPage func - end

##### nextPage func - start
def nextPage() :
    global startPage, totalPage
    if startPage < totalPage :
        startPage = startPage + 1
    pageView.set(str(startPage) + " / " + str(totalPage))
    sql = f"select * from worldPopulation where 순번 ='{startPage}'"
    cur.execute(sql)

    no, code, country, city, population = cur.fetchone() 
    print(no, code, country, city, population)
    
    country_Entry.delete(0,END)
    country_Entry.insert(END, country)
    imgLbl.configure(image = imgTemp)
    img_resize(startPage)
    
##### nextPage func - end

   
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
country_Entry.configure(width=15)
country_Entry.pack(side=LEFT,padx=5, pady=5)

findBtn = Button(topFrame, text="찾기", command=findImg)
findBtn.pack(side=LEFT, padx=3, pady=5)

saveBtn = Button(topFrame, text="저장", command=saveImg)
saveBtn.pack(side=LEFT, padx=2, pady=5)
# topFrame - end                           
############################################
# imgFrame - start
imgTemp = PhotoImage() #빈이미지
imgLbl = Label(imgFrame, image=imgTemp, bg='yellow')
imgLbl.configure(width=200, height=200)
imgLbl.pack()
# imgFrame - end
############################################
# bottomFrame - start
prev_btn = Button(bottomFrame, text="<", command=prevPage)
prev_btn.pack(side=LEFT, padx=5, pady=5)

pageView = StringVar()
pageView.set(str(startPage) + " / " + str(totalPage))

page_Lbl = Label(bottomFrame, textvariable = pageView)
page_Lbl.pack(side=LEFT, padx=15, pady=5)

next_btn = Button(bottomFrame, text=">", command=nextPage)
next_btn.pack(side=LEFT, padx=5, pady=5)
# bottomFrame - end
############################################

prevPage()

root.mainloop()
