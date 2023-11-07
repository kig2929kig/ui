from ytd import download_audio, download_video
from tkinter import *
from tkinter import ttk
import os

win_size_width = 450
win_size_height = 400
save_folder = 'mp3'

root = Tk()
root.geometry(str(win_size_width)+ 'x' + str(win_size_height))
root.title('YouTube Downloader')
root.resizable(False, False)

#func
def url_clear():
  url_entry.delete(0,END)
    
def show_folder():
  path = os.path.realpath(save_folder)
  os.startfile(path)
  
def ytd_download():
  pass

#Frame
url_Frame = LabelFrame(root, text='주소(URL)')
url_Frame.pack(padx=5, pady=5, fill='x', expand='yes')

progress_Frame = Frame(root)
progress_Frame.pack(padx=5, pady=5, fill='x', expand='yes')

dwnld_state_Frame = LabelFrame(progress_Frame, text='진행률')
dwnld_state_Frame.pack(padx=5, pady=5, fill='x', expand='yes', side='left')

select_mp3_or_mp4_frame = LabelFrame(progress_Frame, text='파일선택')
select_mp3_or_mp4_frame.pack(padx=5, pady=5, fill='y', side='left')

#Wedget
url_entry = Entry(url_Frame)
url_entry.pack(padx=5, pady=10, fill='both', expand='yes', side='left')
btn_url_clear = Button(url_Frame, text='x', command=url_clear)
btn_url_clear.pack(padx=2, side='left')
btn_show_folder = Button(url_Frame, text='...', command=show_folder)
btn_show_folder.pack(padx=5, side='left')

progress_current_value = DoubleVar()
progress_state_value = StringVar() 
progress_bar = ttk.Progressbar(dwnld_state_Frame, maximum=100, variable=progress_current_value)
progress_bar.pack(padx=1, pady=10, fill='both', expand='yes', side='left')
progress_state_label = Label(dwnld_state_Frame, textvariable=progress_state_value)
progress_state_label.pack(padx=2, side='left')
btn_download = Button(dwnld_state_Frame, text='다운로드', command=ytd_download)
btn_download.pack(padx=2, side='left')


radio_value = StringVar()
radio_value.set('mp3')
mp3_rd_btn = ttk.Radiobutton(select_mp3_or_mp4_frame, text='mp3', variable=radio_value)
mp4_rd_btn = ttk.Radiobutton(select_mp3_or_mp4_frame, text='mp4', variable=radio_value)
mp3_rd_btn.config(value='mp3')
mp4_rd_btn.config(value='mp4')
mp3_rd_btn.pack(side='left')
mp4_rd_btn.pack(side='left')

root.mainloop()



