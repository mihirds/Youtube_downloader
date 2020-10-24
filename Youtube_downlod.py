from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print("Title: " , yt.title) # title

print("number of views ", yt.views) # views

print("length of video ", yt.length, "seconds") # runtime(seconds)

print("description: ", yt.description)

print("Rating: ", yt.rating)



print(yt.streams)
print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()
ys = yt.streams.get_by_itag('22')


#download process

print("downloading")

ys.download('/Users/mihirshah/Desktop/yt_dowloads')
print("download complete!")

