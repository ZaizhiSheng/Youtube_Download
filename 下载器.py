from pytube import YouTube

#Now, let’s try to download a video. 
#For this example, let’s take something like the YouTube Rewind video for 2019:


url = "https://www.youtube.com/watch?v=i12DHZ_-od8"
my_video = YouTube(url)
my_video = my_video.streams.get_highest_resolution()

my_video.download()
