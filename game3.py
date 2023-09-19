import random, base64
from tkinter import *
from connectDB import cur, conn
from io import BytesIO
from PIL import Image, ImageTk


RAND_COUNTRY_LIST = []
PROBLEM = 0


## START 화면 구현 ## 
def myFrame():
  score_hp_frame = Frame(root)
  score_hp_frame.pack(fill='both')

  second_frame = Frame(root)
  second_frame.pack()

  img_frame = Frame(root)
  img_frame.pack()

  btn_frame = Frame(root)
  btn_frame.pack()
  return score_hp_frame, second_frame, img_frame, btn_frame

def myWidget(score_hp_frame, second_frame, img_frame, btn_frame):
  current_score = 0
  max_score = 0
  
  score_lbl_text = str(current_score) + ' / ' + str(max_score) 
  score_lbl = Label(score_hp_frame, text=score_lbl_text, width = 15 )
  score_lbl.configure(relief='ridge', height=2)
  score_lbl.configure(font=('굴림', 12, 'bold'))
  score_lbl.pack(side=LEFT, padx = 5, pady = 5)
  
  score_lbl_text = str(current_score) + ' / ' + str(max_score) 
  score_lbl = Label(score_hp_frame, text=score_lbl_text, width = 15 )
  score_lbl.configure(relief='ridge', height=2)
  score_lbl.configure(font=('굴림', 12, 'bold'))
  score_lbl.pack(side=LEFT, padx = 5, pady = 5)

  hp_img = PhotoImage(file='hp.png')
  hp_lbl = Label(score_hp_frame, image=hp_img, width = 90)
  hp_lbl.configure(relief='ridge')
  hp_lbl.pack(side=RIGHT, padx=5, pady = 5)
  
  time = 5
  second_lbl = Label(second_frame, text=(str(time)))
  second_lbl.configure(font=('굴림', 20, 'bold'))
  second_lbl.pack()
  
  imgTemp = PhotoImage() #빈이미지
  img_lbl = Label(img_frame, image=imgTemp, bg='yellow')
  img_lbl.configure(width=200, height=200)
  img_lbl.pack(pady=5)  

  btn1 = Button(btn_frame, text="1번", width=12, height=2, command=btn_click)
  btn1.grid(row=0, column=0, padx=10, pady=6)
  btn2 = Button(btn_frame, text="2번", width=12, height=2, command=btn_click)
  btn2.grid(row=0, column=1, padx=10, pady=6)
  btn3 = Button(btn_frame, text="3번", width=12, height=2, command=btn_click)
  btn3.grid(row=1, column=0, padx=10, pady=6)
  btn4 = Button(btn_frame, text="4번", width=12, height=2, command=btn_click)
  btn4.grid(row=1, column=1, padx=10, pady=6)
  
  return img_lbl, btn1, btn2, btn3, btn4
## END 화면 구현 ##

## START 문제 리스트 ##
def randCountryList():
  rnd = random.sample(range(1,50), 10)
  
  for r in rnd :
    sql = f'select * from worldPopulation where 순번 = {r}'
    cur.execute(sql)
    RAND_COUNTRY_LIST.append(cur.fetchone())
## END 문제 리스트 ##  

def showImg(PROBLEM):
  
  sql = f'select * from flag where 순번 = {PROBLEM}'
  cur.execute(sql)
  no, code, img = cur.fetchone()
  
  if img == None :
    pass
  else :
    img = base64.b64decode(img)
    img = Image.open(BytesIO(img))
    resizedImg = img.resize((200,200))
    resizedImg = ImageTk.PhotoImage(resizedImg)
    img_lbl.configure(image=resizedImg)
    img_lbl.image = resizedImg
  
def btn_click() :
  global PROBLEM
  PROBLEM = PROBLEM + 1
  showImg(RAND_COUNTRY_LIST[PROBLEM][0])
  wrongAnser(PROBLEM)

def wrongAnser(PROBLEM):
  answer = RAND_COUNTRY_LIST[PROBLEM][2]
  wAnser = []
  for wa in RAND_COUNTRY_LIST:
    wAnser.append(wa[2])
  wAnser.remove(answer)
  
  btn1_c, btn2_c, btn3_c, btn4_c = random.sample(wAnser,4)
  btn1.configure(text=btn1_c)
  btn2.configure(text=btn2_c)
  btn3.configure(text=btn3_c)
  btn4.configure(text=btn4_c)
  
  answer_num = random.sample(range(1,4),1)
  print(answer, answer_num)
  if answer_num[0] == 1 :
    btn1.configure(text=answer)
  elif answer_num[0] == 2 :
    btn2.configure(text=answer)
  elif answer_num[0] == 3 :
    btn3.configure(text=answer)
  elif answer_num[0] == 4 :
    btn4.configure(text=answer)    
    

def playGame() :
  randCountryList()
  print(RAND_COUNTRY_LIST)
  showImg(RAND_COUNTRY_LIST[0][0])
  wrongAnser(PROBLEM) 
  
  
  
  
  
root = Tk()
root.title('세계 나라별 국기 퀴즈')
root.geometry('300x400')

score_hp_frame, second_frame, img_frame, btn_frame = myFrame()
img_lbl, btn1, btn2, btn3, btn4 = myWidget(score_hp_frame, second_frame, img_frame, btn_frame)

playGame()

root.mainloop()