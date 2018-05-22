import os
import unittest
from filewriter import FileWriter

class TestFileWriter(unittest.TestCase):


    def setUp(self):
        self.ROOT = "files/"
        self.fw = FileWriter(self.ROOT)
        self.emptyDirs = []

    def test_create_folder(self):
        self.fw.create_folder("test")
        self.assertTrue(os.path.exists(self.ROOT + "test"))

    def test_copy_file_to_repo(self):
        file_path = self.fw.copy_file_to_repo("tests/dummy.pdf")
        self.assertTrue(os.path.isfile(file_path))
    
    def test_extract_filename(self):
        file_path =  "tests/dummy.pdf"
        self.fw.extract_filename(file_path)

    def test_get_folders_count(self):
        self.fw.create_folder("folder1")
        self.fw.create_folder("folder2")
        
        self.fw.create_folder("folder1/folder1.1")
        self.fw.create_folder("folder2/folder2.1")        

        folders = self.fw.get_folders_count(self.ROOT)
        self.assertEquals(folders, 2)

    def test_get_parent_folder_none(self):
        parent_folder = self.fw.get_parent_folder("files")
        self.assertIsNone(parent_folder)
    
    def test_get_parent_folder(self):
        self.fw.create_folder("parent")
        self.fw.create_folder("parent/child")
        parent_folder = self.fw.get_parent_folder("files/parent/child")
        self.assertEquals(parent_folder, "files/parent" )

        
    #Tear Down Code

    def tearDown(self):
        tree = os.walk(self.ROOT)
        emptyDirs = []

        for directory in tree:
            self.removeDirectory(directory)

        for dir in self.emptyDirs:
            print "Removing " + dir
            os.rmdir(dir)

    def deleteFiles(self, dirList, dirPath):
        for file in dirList:
            print "Deleting " + file
            os.remove(dirPath + "/" + file)

    def removeDirectory(self, dirEntry):
        print "Deleting files in " + dirEntry[0]
        self.deleteFiles(dirEntry[2], dirEntry[0])
        self.emptyDirs.insert(0, dirEntry[0])
        

