import os
from shutil import copyfile, copy2

class FileWriter:

    def __init__(self, root_folder, current_folder):
        self.ROOT_FOLDER = root_folder
        self.CURRENT_FOLDER = current_folder
    
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
        print('<==========================================>')
        print(children)
        # if children >= MAX_FOLDERS and parent == None:
		#     return None, "The repository tree is full"
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
        