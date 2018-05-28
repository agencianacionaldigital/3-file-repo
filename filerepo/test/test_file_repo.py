import os
import unittest
from filerepo.repomanager import RepoManager
from filerepo.repomanager import generate_name
# from filewriter import FileWriter
# from filewriter import generate_name

class TestFileWriter(unittest.TestCase):


    def setUp(self):
        self.ROOT = "files"
        self.CURRENT_FOLDER = "files"
        self.rm = RepoManager(self.ROOT, self.CURRENT_FOLDER)
        self.emptyDirs = []

    def test_generate_name(self):
        name = generate_name(6)
        self.assertIsInstance(name, str)
        self.assertEqual(len(name), 6)

    def test_create_folder(self):
        self.rm.create_folder(os.path.join(self.ROOT,"test"))
        self.assertTrue(os.path.exists(os.path.join(self.ROOT,"test")))


    def test_repository_full(self):
        rm = RepoManager(self.ROOT, self.CURRENT_FOLDER)
        rm.MAX_FOLDERS = 1
        rm.create_folder(self.ROOT + "/test")
        with self.assertRaises(SystemError):
            rm.get_destiny_path()
    
    def test_extract_filename(self):
        file_path =  "filerepo/test/dummy.pdf"
        self.rm.extract_filename(file_path)

    def test_get_folders_count(self):
        self.rm.create_folder(os.path.join(self.ROOT, "parent"))
        self.rm.create_folder(os.path.join(self.ROOT, "parent/child"))


    def test_get_parent_folder_none(self):
        parent_folder = self.rm.get_parent_folder("files")
        self.assertIsNone(parent_folder)
    
    def test_get_parent_folder(self):
        self.rm.create_folder(os.path.join(self.ROOT, "parent"))
        self.rm.create_folder(os.path.join(self.ROOT, "parent/child"))
        parent_folder = self.rm.get_parent_folder("files/parent/child")
        self.assertEquals(parent_folder, "files/parent" )

    def test_get_folder_level(self):
        rm = RepoManager("files/carpeta/test", "files/carpeta/test")
        level = rm.get_folder_level("files/carpeta/test")
        self.assertEquals(level, 1)

        rm = RepoManager("files/carpeta/test", "files/carpeta/test")
        level = rm.get_folder_level("files/carpeta/test/3434")
        self.assertEquals(level, 2)

    


    # def test_get_destiny_path(self):
    #     fw = RepoManager(self.ROOT)
    #     path = fw.get_destiny_path()

    #     level = fw.get_folder_level(fw.CURRENT_FOLDER)
    #     print(level)

        #self.assertEquals(level, fw.MAX_DEPTH)

    # def test_subfolder_is_full(self):
    #     fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
    #     fw.MAX_FILES = 1
    #     fw.copy_file_to_repo("tests/files/a.pdf")
    #     file_path = fw.get_destiny_path()
    #     self.assertTrue(os.path.isdir(file_path))

    # def test_subfolder_and_sibblings_are_full(self):
    #     fw = FileWriter(self.ROOT, self.CURRENT_FOLDER)
    #     fw.MAX_FILES = 1
    #     fw.MAX_FOLDERS = 2
    #     fw.copy_file_to_repo("tests/files/a.pdf")
    #     fw.copy_file_to_repo("tests/files/b.pdf")
    #     file_path = fw.get_destiny_path()
    #     self.assertTrue(os.path.isdir(file_path))

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
        

