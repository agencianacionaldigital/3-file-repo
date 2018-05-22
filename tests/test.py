import os
import unittest
from filewriter import FileWriter
from filewriter import generate_name

class TestFileWriter(unittest.TestCase):


    def setUp(self):
        self.ROOT = "files"
        self.CURRENT_FOLDER = "files"
        self.fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
        self.emptyDirs = []

    def test_generate_name(self):
        name = generate_name()
        self.assertIsInstance(name, str)

    # def test_create_folder(self):
    #     self.fw.create_folder("test")
    #     self.assertTrue(os.path.exists(self.ROOT + "/test"))

    # def test_copy_file_to_repo(self):
    #     file_path = self.fw.copy_file_to_repo("tests/dummy.pdf")
    #     self.assertTrue(os.path.isfile(file_path))

    # def test_repository_full(self):
    #     fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
    #     fw.MAX_FOLDERS = 1
    #     fw.create_folder(self.ROOT + "/test")
    #     with self.assertRaises(SystemError):
    #         fw.get_destiny_path()
    
    # def test_extract_filename(self):
    #     file_path =  "tests/dummy.pdf"
    #     self.fw.extract_filename(file_path)

    def test_get_folders_count(self):
        self.fw.create_folder(os.path.join(self.ROOT, "parent"))
        self.fw.create_folder(os.path.join(self.ROOT, "parent/child"))

    def test_get_files_count(self):
        count = self.fw.get_files_count("tests/files")
        self.assertEquals(count, 2)

    def test_get_parent_folder_none(self):
        parent_folder = self.fw.get_parent_folder("files")
        self.assertIsNone(parent_folder)
    
    def test_get_parent_folder(self):
        self.fw.create_folder(os.path.join(self.ROOT, "parent"))
        self.fw.create_folder(os.path.join(self.ROOT, "parent/child"))
        parent_folder = self.fw.get_parent_folder("files/parent/child")
        self.assertEquals(parent_folder, "files/parent" )


    def test_get_folder_level(self):
        level = self.fw.get_folder_level("files/parent/child")
        self.assertEquals(level, 3)

        level = self.fw.get_folder_level("files")
        self.assertEquals(level,1)


    def test_get_destiny_path(self):
        fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
        path = fw.get_destiny_path()

        level = fw.get_folder_level(fw.CURRENT_FOLDER)
        self.assertEquals(level, fw.MAX_DEPTH)

    def test_subfolder_is_full(self):
        fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
        fw.MAX_FILES = 1
        fw.copy_file_to_repo("tests/files/a.pdf")
        file_path = fw.get_destiny_path()
        self.assertTrue(os.path.isdir(file_path))

    def test_subfolder_and_sibblings_are_full(self):
        fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
        fw.MAX_FILES = 1
        fw.MAX_FOLDERS = 2
        fw.copy_file_to_repo("tests/files/a.pdf")
        fw.copy_file_to_repo("tests/files/b.pdf")
        file_path = fw.get_destiny_path()
        self.assertTrue(os.path.isdir(file_path))

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
        

