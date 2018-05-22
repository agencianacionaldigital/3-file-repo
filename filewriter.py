import os
import string
import random

from shutil import copyfile, copy2

class FileWriter:
    
    MAX_FOLDERS = 64
    
    def __init__(self, root_folder, current_folder):
        self.ROOT_FOLDER = root_folder
        self.CURRENT_FOLDER = current_folder

        if not os.path.exists(self.CURRENT_FOLDER):
            os.makedirs(self.CURRENT_FOLDER)

    
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
        #the file name is the same source file name
        destiny_file_basename = self.extract_filename(source_path)
        destiny_path = self.get_destiny_path()
        destiny_absolute_path = os.path.join(destiny_path, destiny_file_basename)

        if not os.path.exists(destiny_path):
            os.makedirs(destiny_path)

        copyfile(source_path, destiny_absolute_path)

        return destiny_absolute_path

    def extract_filename(self, path):
        return os.path.basename(path)

    def get_destiny_path(self):
        children = self.get_folders_count(self.CURRENT_FOLDER)
        parent = self.get_parent_folder(self.CURRENT_FOLDER)
        
        if children >= self.MAX_FOLDERS and parent == None:
            raise SystemError("The repository is full")
        elif children==0:
            self.create_folder(generate_name())
            pass
            #when only the ROOT_FOLDER exists


        return "files"

    def get_folders_count(self, path):
        """
            Gets the count children of one level depth only
        """
        folders = 0
        for x in os.listdir(path):
            if os.path.isdir(os.path.join(self.ROOT_FOLDER, x)):
                folders+=1
        return folders

    
    def get_parent_folder(self, path):
        """
            Gets the parent folder, None if path is root
        """
        parent = os.path.dirname(path)
        return parent if parent != '' else None

def generate_name(num=16):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(num))
        