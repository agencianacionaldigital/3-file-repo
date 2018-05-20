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
        

