

opts_video = {
    'format':'bestvideo[height>=1080][ext=mp4]+bestaudio[ext=m4a]/best[height>=1080][ext=mp4]',
    'outtmpl':'.//mv/%(title)s.%(ext)s',
    'nooverwrites': False,
}

opts_audio = {
    'format':'bestaudio/best',
    'postprocessors': [{
      'key':'FFmpegExtractAudio',
      'preferredcodec':'mp3',
      'preferredquality':'192',
      }],
    'nooverwrites': False,
    'outtmpl':'.//mp3/%(title)s.%(ext)s',
}
