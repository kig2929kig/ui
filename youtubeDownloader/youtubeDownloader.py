from ytd import download_youtube
from yt_opts import opts_audio, opts_video
import reomve_ansi_escape_codes

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os, subprocess
from threading import Thread
import platform

import pygame
pygame.init()
pygame.mixer.init()
song = '' 
pause_flag = 0 # pause or unpause flag
music_list_index = 0

win_size_width = 450
win_size_height = 310

root = Tk()
root.geometry(str(win_size_width)+ 'x' + str(win_size_height))
root.title('YouTube Downloader')
root.resizable(False, False)

# start func ##############################################################################################
def url_clear():
  url_entry.delete(0,END)
    
def show_folder():
  current_os = platform.system()
  
  if radio_value.get() == 'mp3':
    path = os.path.realpath('.//mp3/')
    if current_os == 'Windows':
      try:
        os.startfile(path) # window system
      except:
        os.makedirs('./mp3/', exist_ok=True)
        os.startfile(path)
    else :
      subprocess.run(['nemo', path], bufsize=0) #linux system - hamoniKR
  elif radio_value.get() == 'mp4':
    path = os.path.realpath('.//mv/')
    if current_os == 'Windows':
      try:
        os.startfile(path) # window system
      except:
        os.makedirs('./mv/', exist_ok=True)
        os.startfile(path)
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
    file_list()
 
def threading() :
  btn_download_thread = Thread(target=ytd_download)
  btn_download_thread.start()

def show_folder_threading():
  show_folder_thread = Thread(target=show_folder)
  show_folder_thread.start()

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

def music_select(event):
  global song, music_list_index
  selection = f_list.curselection()
  music_list_index = selection[0]
  print(music_list_index)
  song = f_list.get(music_list_index)
  print(song)
  #play()
  btn_play.config(foreground='black')  
  btn_play['state'] = 'active'

def file_list():
  if not os.path.exists('./mp3'):
    os.mkdir('./mp3')
  else:
    pass
  f_list.delete(0,END)
  file_lst = os.listdir('./mp3')
  index = 0
  f_list.activate(index)
  f_list.select_set(index)
  f_list.select_anchor(index)
  for file in file_lst:
    if file.endswith('.mp3'):
      f_list.insert(index, str(file))
      index += 1

def play():
  global song, pause_flag
  path = f'./mp3/{song}'
  print(path)
  pygame.mixer.music.load(path)
  pygame.mixer.music.play()
  btn_play.config(foreground='gray')
  btn_play['state'] = 'disable'
  btn_stop.config(foreground="black")
  btn_stop["state"] = "active"
  btn_pause.config(foreground="black")
  btn_pause["state"] = "active"
  pause_flag = 0
  btn_pause.config(text='PAUSE')
  btn_prev.config(foreground="black")
  btn_prev["state"] = "active"
  btn_next.config(foreground="black")
  btn_next["state"] = "active"

def stop():
  global pause_flag
  pygame.mixer.music.stop()
  btn_stop.config(foreground="gray")
  btn_stop["state"] = "disable"
  btn_play.config(foreground='black')
  btn_play['state'] = 'active'
  btn_pause.config(foreground="gray")
  btn_pause["state"] = "disable"
  btn_pause.config(text='PAUSE', foreground='black')
  pause_flag = 0

def pause():
  global pause_flag  
  if pause_flag == 0:
    pygame.mixer.music.pause()
    btn_pause.config(text='UNPAUSE', foreground='red')
    pause_flag = 1
  else :
    pygame.mixer.music.unpause()
    btn_pause.config(text='PAUSE', foreground='black')
    pause_flag = 0

def prev():
  global music_list_index, song
  if music_list_index > 0:
    music_list_index -= 1
    print("music list number : ", music_list_index)
    song = f_list.get(music_list_index)
    f_list.select_clear(0, END)
    f_list.select_set(music_list_index)
    f_list.activate(music_list_index)
    f_list.see(music_list_index)
    play()
  else:
    btn_prev['state'] = 'disable'

def next():
  global music_list_index, song
  if music_list_index < f_list.size() -1:
    music_list_index += 1
    print("music list number : ", music_list_index)
    song = f_list.get(music_list_index)
    f_list.select_clear(0,END)
    f_list.select_set(music_list_index)
    f_list.activate(music_list_index)
    f_list.see(music_list_index)
    play()
  else:
    btn_next['state'] = 'disable'
# end func #######################################################################################################

#start Frame#########################################################################################
url_Frame = LabelFrame(root, text='주소(URL)')
url_Frame.pack(padx=5, pady=5, fill='x', expand='yes')

progress_Frame = Frame(root)
progress_Frame.pack(padx=5, pady=5, fill='x', expand='yes')

dwnld_state_Frame = LabelFrame(progress_Frame, text='진행률')
dwnld_state_Frame.pack(padx=5, pady=5, fill='x', expand='yes', side='left')

select_mp3_or_mp4_frame = LabelFrame(progress_Frame, text='파일선택')
select_mp3_or_mp4_frame.pack(padx=5, pady=5, fill='y', side='left')

folder_list_frame = LabelFrame(root, text='mp3 목록')
folder_list_frame.pack(padx=5, pady=5, fill='both', expand='yes')
# end Frame ##########################################################################################

# start Wedget #######################################################################################
url_entry = Entry(url_Frame)
url_entry.pack(padx=5, pady=10, fill='both', expand='yes', side='left')
btn_url_clear = Button(url_Frame, text='x', command=url_clear)
btn_url_clear.pack(padx=2, side='left')
btn_show_folder = Button(url_Frame, text='...', command=show_folder_threading)
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

f_list = Listbox(folder_list_frame, activestyle="none")
f_list.pack(fill='both', side='left', expand='yes')
f_list_scrollbar = Scrollbar(folder_list_frame, orient=VERTICAL)
f_list_scrollbar.pack(side='right', fill='y')
f_list.config(yscrollcommand=f_list_scrollbar.set)
f_list_scrollbar.config(command=f_list.yview)
file_list()
f_list.bind("<<ListboxSelect>>", music_select)

btn_play = Button(folder_list_frame, text="PLAY", command=play)
btn_play.pack(fill="x")
btn_stop = Button(folder_list_frame, text="STOP", command=stop, foreground="gray")
btn_stop.pack(fill="x")
btn_pause = Button(folder_list_frame, text="PAUSE", command=pause, foreground="gray")
btn_pause.pack(fill="x")
btn_prev = Button(folder_list_frame, text="Prev", command=prev, foreground="gray")
btn_prev.pack(fill="x")
btn_next = Button(folder_list_frame, text="Next", command=next, foreground="gray")
btn_next.pack(fill="x")

btn_pause['state'] = 'disable'
btn_stop['state'] = 'disable'
btn_prev['state'] = 'disable'
btn_next['state'] = 'disable'
# end Wedget ##########################################################################################

root.mainloop()



