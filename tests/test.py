import unittest
from FileWriter import FileWriter

class TestFileWriter(unittest.TestCase):

    def test_base(self):
        fw = FileWriter()
        self.assertTrue(True)
