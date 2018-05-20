import os
from shutil import copyfile

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
    
    def copy_file(self, original):
        copy_file(original, "hola.pdf")

        