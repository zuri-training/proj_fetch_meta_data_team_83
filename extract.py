import exiftool

files = ["pgAdmin1.gif"]
with exiftool.ExifTool() as et:
    metadata = et.get_metadata("/data/data/com.termux/files/home/zuriboard/proj_fetch_meta_data_team_83/pgAdmin1.gif")
for d in metadata:
    print("{:20.20} {:20.20}".format(d["SourceFile"],d["EXIF:DateTimeOriginal"]))
