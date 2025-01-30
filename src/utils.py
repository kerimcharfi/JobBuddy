import os

def txt_file_iter(directory):
    """
    A generator that yields the contents of each .txt file
    in the specified directory.
    """
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file ends with ".txt"
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            # Open and read the file contents
            with open(file_path, 'r', encoding='utf-8') as file:
                yield file.read()