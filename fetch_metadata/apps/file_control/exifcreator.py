import os
import subprocess

input_file = "fetch_metadata/apps/meta_extract/sample.csv"

file_ext = ".mttrck" #metatrack file extension for saving metadata
root_file_name = os.path.splitext(input_file)[0] #file name without extension

output_file = str(root_file_name) + str(file_ext)

with open(output_file, "w") as output:
    exiftool_command = ["exiftool", input_file]
    subprocess.run(exiftool_command, stdout=output)

