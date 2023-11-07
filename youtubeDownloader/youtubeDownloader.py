from ytd import download_youtube
from yt_opts import opts_audio, opts_video
import reomve_ansi_escape_codes

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, subprocess
from threading import Thread
import platform

win_size_width = 450
win_size_height = 200
save_folder = 'mp3'

root = Tk()
root.geometry(str(win_size_width)+ 'x' + str(win_size_height))
root.title('YouTube Downloader')
root.resizable(False, False)

#func
def url_clear():
  url_entry.delete(0,END)
    
def show_folder():
  current_os = platform.system()
  
  if radio_value.get() == 'mp3':
    path = os.path.realpath('.//mp3/')
    if current_os == 'Windows':
      os.startfile(path) # window system
    else :
      subprocess.run(['nemo', path], bufsize=0) #linux system - hamoniKR
  elif radio_value.get() == 'mp4':
    path = os.path.realpath('.//mv/')
    if current_os == 'Windows':
      os.startfile(path) # window system
    else:
      subprocess.run(['nemo', path], bufsize=0) #linux system - hamoniKR

def complete_status(down):
  if down['status'] == 'finished':
    print('\n Download completed')
  if down['status'] == 'downloading':
    print(f"Downloading... {down['_percent_str']} complete")
    prgrss_value = down['_percent_str']
    pv_str = reomve_ansi_escape_codes.remove(prgrss_value)
    pv_float = float(pv_str[:-1])
    progress_state_value.set(reomve_ansi_escape_codes.remove(prgrss_value))
    progress_current_value.set(pv_float)
  if down['status'] == 'error':
    btn_download['state'] = 'active'
    messagebox.showerror("ERROR", "다운로드 중 에러가 발생했습니다.")
          
def post_complete_status(down):
  if down['status'] == 'finished':
    btn_download['state'] = 'active'
 
def threading() :
  btn_download_thread = Thread(target=ytd_download)
  btn_download_thread.start()
  
def ytd_download():
  btn_download['state'] = 'disable'
  if radio_value.get() == 'mp3':
    opts_audio_add = {'progress_hooks': [complete_status], 'postprocessor_hooks': [post_complete_status]}
    opts_audio.update(opts_audio_add)
    try:
      download_youtube(url_entry.get(), opts_audio)
    except :
      messagebox.showerror("ERROR", "입력한 주소가 잘못되었습니다.")
      btn_download['state'] = 'active'
  if radio_value.get() == 'mp4':
    opts_video_add = {'progress_hooks': [complete_status], 'postprocessor_hooks': [post_complete_status]}
    opts_video.update(opts_video_add)
    try:
      download_youtube(url_entry.get(), opts_video)
    except :
      messagebox.showerror("ERROR", "입력한 주소가 잘못되었습니다.")
      btn_download['state'] = 'active'
    
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
btn_download = Button(dwnld_state_Frame, text='다운로드', command=threading)
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



