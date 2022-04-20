from ast import Assert
from cgi import test
from genericpath import isfile
import unittest
import os
from mass_file_rename import File, Folder, Renamer, Scheme


class TestFile(unittest.TestCase):

    def test_file_rename(self):
        """Test File Rename
        This is a basic test for the change_name_to() function.
        changes a practice file named test1.txt to tester.txt.

        If this test does not pass, the tester.txt may not have
        been set back to test1.txt. It does not automatically
        reset because I wanted to actually see the file change
        to be sure. I will probably add something to automatically
        reset it later. 
        """

        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, './practice_files/test1.txt')

        test_file_obj = File(file_path)
        test_file_obj.change_name_to("tester")

        # assert file with old name is no longer there
        self.assertFalse(os.path.isfile(file_path))
        # assert file with new name is there
        self.assertTrue(os.path.isfile(test_file_obj.file_path))


if __name__ == '__main__':
    unittest.main()
