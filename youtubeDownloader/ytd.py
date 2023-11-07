import yt_dlp

def download_youtube(url, opts):
  with yt_dlp.YoutubeDL(opts) as ydl:
    ydl.download([url])
  
def main():
  from yt_opts import opts_audio, opts_video
  
  url = input('youtube address : ')
  
  #download_youtube(url, opts_audio)
  download_youtube(url, opts_video)
  
if __name__ == "__main__":
  main()
  
  