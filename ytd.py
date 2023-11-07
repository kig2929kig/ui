import yt_dlp

def download_video(url):
  def complete_status(down):
    if down['status'] == 'finished':
      print('\n Download completed')
    if down['status'] == 'downloading':
      print(f"Downloading... {down['_percent_str']} complete")
        
  ydl_opts = {
    'format':'bestvideo[height>=1080][ext=mp4]+bestaudio[ext=m4a]/best[height>=1080][ext=mp4]',
    'outtmpl':'.//mv/%(title)s.%(ext)s',
    'progress_hooks': [complete_status],
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

def download_audio(url):
  def complete_status(down):
    if down['status'] == 'finished':
      print('\n Download completed')
    if down['status'] == 'downloading':
      print(f"Downloading... {down['_percent_str']} complete")
          
  ydl_opts = {
    'format':'bestaudio/best',
    'postprocessors': [{
      'key':'FFmpegExtractAudio',
      'preferredcodec':'mp3',
      'preferredquality':'192',
      }],
    'outtmpl':'.//mp3/%(title)s.%(ext)s',
    'progress_hooks': [complete_status],    
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  
def main():
  url = input('input : ')
  #download_video(url)
  download_audio(url)
if __name__ == "__main__":
  main()
  
  