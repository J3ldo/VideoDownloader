from pytube import YouTube
vid = YouTube("https://www.youtube.com/watch?v=XuDxt0WrG2I")
vid1 = vid.streams.get_highest_resolution()
vid1.download()
