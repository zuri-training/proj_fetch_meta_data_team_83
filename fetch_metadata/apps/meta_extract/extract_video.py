#pip install tinytag
#Run python extract_video.py


#accessing audio/video meta data
from tinytag import TinyTag
video = TinyTag.get("<video file name>")  ### replace <video file name> with your file name and should be in same directory

# attributes and display
print("Title:" + video.title)
print("Artist:" + video.artist)
print("Genre:" + video.genre)
print("Year Released:" + video.year)
print("Bitrate:" + str(video.bitrate) + " kBits/s")
print("Composer:" + video.composer)
print("Filesize:" + str(video.filesize) + " bytes")
print("AlbumArtist:" + str(video.albumartist))
print("Duration:" + str(video.duration) + " seconds")
print("trackTotal:" + str(video.track_total))
