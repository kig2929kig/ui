import pymysql
from tkinter import *
from tkinter import messagebox


def insertData():
    conn = pymysql.connect(host='3.39.233.42', \
                           port=54778, \
                           user='kig2929kig', \
                           password='ansan', \
                           db='com3100', \
                           charset='utf8')
    
    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get()
    data4 = edt4.get(); data5 = edt5.get(); data6 = edt6.get()
    sql = "insert into 수강 values('"+data1+"','" +data2+"','"+data3+"','"+data4+"','"+data5+"','"+data6+"')"
    
    cur = conn.cursor()
    cur.execute(sql)

    conn.commit()
    conn.close()

    messagebox.showinfo("수강 테이블", "수강 테이블에 레코드가 입력되었습니다.")
    
def selectData():
    strData1, strData2, strData3, strData4, strData5, strData6 = [],[],[],[],[], []    
    conn = pymysql.connect(host='3.39.233.42', \
                           port=54778, \
                           user='kig2929kig', \
                           password='ansan', \
                           db='com3100', \
                           charset='utf8')
    
    cur = conn.cursor()
    cur.execute("select * from 수강")

    strData1.append("학번");      strData2.append("과목번호");
    strData3.append("신청날짜");  strData4.append("중간성적");
    strData5.append("기말성적");  strData6.append("평가학점");
    strData1.append("----------"); strData2.append("----------");
    strData3.append("----------"); strData4.append("----------");
    strData5.append("----------"); strData6.append("----------");

    row = cur.fetchall()

        
    for r in row:        
        strData1.append(r[0]); strData2.append(r[1]);
        strData3.append(r[2]); strData4.append(r[3]);
        strData5.append(r[4]); strData6.append(r[5]);

    lstData1.delete(0, lstData1.size()-1); lstData2.delete(0, lstData2.size()-1);
    lstData3.delete(0, lstData3.size()-1); lstData4.delete(0, lstData4.size()-1);
    lstData5.delete(0, lstData5.size()-1); lstData6.delete(0, lstData6.size()-1);      

    for i1, i2, i3, i4, i5, i6 in zip(strData1, strData2, strData3, strData4, strData5, strData6):
        lstData1.insert(END, i1); lstData2.insert(END, i2)
        lstData3.insert(END, i3); lstData4.insert(END, i4);
        lstData5.insert(END, i5); lstData6.insert(END, i6);

    
    conn.commit()
    conn.close()
    
    
root = Tk()
root.title("컴퓨터과 3학년 1반 0번 강인구") 
edtFrame = Frame(root)
edtFrame.pack()

lstFrame = Frame(root)
lstFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10)
edt2 = Entry(edtFrame, width=10)
edt3 = Entry(edtFrame, width=10)
edt4 = Entry(edtFrame, width=10)
edt5 = Entry(edtFrame, width=10)
edt6 = Entry(edtFrame, width=10)

edt1.pack(side = LEFT, padx=10, pady=10)
edt2.pack(side = LEFT, padx=10, pady=10)
edt3.pack(side = LEFT, padx=10, pady=10)
edt4.pack(side = LEFT, padx=10, pady=10)
edt5.pack(side = LEFT, padx=10, pady=10)
edt6.pack(side = LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="입력", command = insertData)
btnInsert.pack(side = LEFT, padx=10, pady=10)

btnSelect = Button(edtFrame, text="조회", command = selectData)
btnSelect.pack(side = LEFT, padx=10, pady=10)

lstData1 = Listbox(lstFrame, bg = "yellowgreen")
lstData1.pack(side=LEFT, fill=BOTH, expand=1)

lstData2 = Listbox(lstFrame, bg = "yellowgreen")
lstData2.pack(side=LEFT, fill=BOTH, expand=1)

lstData3 = Listbox(lstFrame, bg = "yellowgreen")
lstData3.pack(side=LEFT, fill=BOTH, expand=1)

lstData4 = Listbox(lstFrame, bg = "yellowgreen")
lstData4.pack(side=LEFT, fill=BOTH, expand=1)

lstData5 = Listbox(lstFrame, bg = "yellowgreen")
lstData5.pack(side=LEFT, fill=BOTH, expand=1)

lstData6 = Listbox(lstFrame, bg = "yellowgreen")
lstData6.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()













