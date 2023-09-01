from tkinter import *

root = Tk()
root.title('세계 나라별 국기 퀴즈')
root.geometry('300x400')

score = 0
max_score = 0

###################################################
# Frame - start #

score_hp_frame = Frame(root)
score_hp_frame.pack(fill='both')

second_frame = Frame(root)
second_frame.pack()

img_frame = Frame(root)
img_frame.pack()

btn_frame = Frame(root)
btn_frame.pack()

# Frame - end #
###################################################

## score_hp_frame - start ##

#score = StringVar()
#max_score = StringVar()
score_lbl_text = str(score) + ' / ' + str(max_score) 

score_lbl = Label(score_hp_frame, text=score_lbl_text, width = 15 )
score_lbl.configure(relief='ridge', height=2)
score_lbl.configure(font=('굴림', 12, 'bold'))
score_lbl.pack(side=LEFT, padx = 5, pady = 5)

hp_img = PhotoImage(file='hp.png')
hp_lbl = Label(score_hp_frame, image=hp_img, width = 90)
hp_lbl.configure(relief='ridge')
hp_lbl.pack(side=RIGHT, padx=5, pady = 5)

## score_hp_frame -end ##

###################################################


root.mainloop()
