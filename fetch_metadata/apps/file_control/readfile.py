

def read_file(file_path):
    """
    Read a .mttrck file and returns the lines.
    args:
    file_path = path to saved metadata file

    """

    with open(file_path, 'r') as f:
        file_content = f.readlines()
        result = [item.split(':', 1) for item in file_content]
        return result