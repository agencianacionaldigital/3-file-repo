import os
from shutil import copyfile, copy2

class FileWriter:

    def __init__(self, root_folder):
        self.ROOT_FOLDER = root_folder
    
    def get_absolute_uri(self, uri):
        return os.path.join(self.ROOT_FOLDER, uri)

    def create_folder(self, name):
        """
            Creates folder if it does not exist
        """
        uri = self.get_absolute_uri(name)
        if os.path.exists(uri):
            s = "The folder's name: {} already exists.".format(name)
            raise ValueError(s)

        os.makedirs(uri)
    
    def copy_file_to_repo(self,source_path):
        """
            Copy file from path given to an available repository tree folder
        """
        destiny_path = self.get_destiny_path()

        if not os.path.exists(destiny_path):
            os.makedirs(destiny_path)

        copyfile(source_path, "files/hola.pdf")

        return "files/hola.pdf" 

    def get_destiny_path(self):
        return "files"

        