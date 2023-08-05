from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('C:\\Users\\HP\\Desktop\\ytDownPIP')


# run thru shell script
# run in ubuntu?
# #!/bin/zsh
# cd C:\Users\HP\PycharmProjects\YTdownloader
# python main.py $1