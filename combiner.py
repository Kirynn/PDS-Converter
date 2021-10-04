import os
from moviepy import *

L =[]

path = input("Please enter path.")
week = input("Please enter week.")

for root, dirs, files in os.walk(path):

    files.sort()
    #files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

final_clip = concatenate_videoclips(L)
final_clip.to_videofile(f"Week-{week}.mp4", fps=24, remove_temp=False)