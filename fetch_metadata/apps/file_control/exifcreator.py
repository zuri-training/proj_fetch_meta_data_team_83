import os
from time import sleep
from django.core.files import File
import subprocess



def create_meta_file(input_file):
    sleep(1)
    file_ext = ".mttrck" #metatrack file extension for saving metadata
    root_file_name = os.path.splitext(input_file)[0] #file name without extension

    output_file = str(root_file_name) + str(file_ext)

    with open(output_file, "wb") as output:
        """
        Open a file and write the metadata into it
        """
        exiftool_command = ["exiftool", input_file]
        result = subprocess.run(exiftool_command, stdout=PIPE) #File(output))
        data = result.stdout
        print (data.decode("utf-8"))
        output.write(data)
        print(output.name)
        return File(output)
    
