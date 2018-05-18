import os
import unittest
from filewriter import FileWriter

class TestFileWriter(unittest.TestCase):

    def setUp(self):
        self.ROOT = "files/"
        self.fw = FileWriter(self.ROOT)

    def test_create_folder(self):
        self.fw.create_folder("test")
        self.assertTrue(os.path.exists(self.ROOT + "test"))
    

