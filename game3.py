from tkinter import *
from connectDB import cur, conn

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
  btn2 = Button(btn_frame, text="2번", width=12, height=2)
  btn2.grid(row=0, column=1, padx=10, pady=6)
  btn3 = Button(btn_frame, text="3번", width=12, height=2)
  btn3.grid(row=1, column=0, padx=10, pady=6)
  btn4 = Button(btn_frame, text="4번", width=12, height=2)
  btn4.grid(row=1, column=1, padx=10, pady=6)

def btn_click() :
  pass
  
root = Tk()
root.title('세계 나라별 국기 퀴즈')
root.geometry('300x400')

score_hp_frame, second_frame, img_frame, btn_frame = myFrame()
myWidget(score_hp_frame, second_frame, img_frame, btn_frame)

root.mainloop()