from pytube import YouTube
vidurl = input("Video url: ")
vid = YouTube(vidurl)
vid1 = vid.streams.get_highest_resolution()
vid1.download()
input("Succesfully downloaded video")
