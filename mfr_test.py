import unittest
import os
from mass_file_rename import File, Folder, Renamer, Scheme


class TestFile(unittest.TestCase):

    def setUp(self):
        """Set up practice_folder to have three files contained 
        with the name scheme 'test1.txt', 'test2.txt', and 
        'test3.txt'.
        These are the initial conditions for all our basic tests.
        """
        # get the directory of this project
        current_dir = os.path.dirname(__file__)
        pratice_files_path = os.path.join(current_dir, './practice_files')

        # get a list of files in this directory
        files_names_in_pf_folder = [f for f in os.listdir(
            pratice_files_path) if os.path.isfile(os.path.join(pratice_files_path, f))]

        # if there are files in practice_files
        if files_names_in_pf_folder != []:
            for file in files_names_in_pf_folder:
                # delete any files that are currently in this folder
                file_path = os.path.join(pratice_files_path, file)
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Error: {file_path} : {e.strerror}")

        # now there are no files in practice_files, so fill with proper files
        # if the practice_files_path is a valid path
        if os.path.exists(pratice_files_path):
            # make test1, test2, test3
            open(os.path.join(pratice_files_path, 'test1.txt'), 'w').close
            open(os.path.join(pratice_files_path, 'test2.txt'), 'w').close
            open(os.path.join(pratice_files_path, 'test3.txt'), 'w').close

    def test_file_rename(self):
        """Test File Rename
        This is a basic test for the change_name_to() function.
        changes a practice file named test1.txt to tester.txt.

        SetUp() now will start this test with a fresh practice
        files folder. There will always be three files named
        'test1.txt' to 'test3.txt'.
        """
        # get the directory of this project
        current_dir = os.path.dirname(__file__)

        # append the path to the test file
        file_path = os.path.join(current_dir, './practice_files/test1.txt')

        # create test file object and execute naming
        test_file_obj = File(file_path=file_path)
        test_file_obj.change_name_to("tester")

        # assert file with old name is no longer there
        self.assertFalse(os.path.isfile(file_path))
        # assert file with new name is there
        self.assertTrue(os.path.isfile(test_file_obj.file_path))


class TestFolder(unittest.TestCase):

    def setUp(self):
        """Set up practice_folder to have three files contained 
        with the name scheme 'test1.txt', 'test2.txt', and 
        'test3.txt'.
        These are the initial conditions for all our basic tests.
        """
        # get the directory of this project
        current_dir = os.path.dirname(__file__)
        pratice_files_path = os.path.join(current_dir, './practice_files')

        # get a list of files in this directory
        files_names_in_pf_folder = [f for f in os.listdir(
            pratice_files_path) if os.path.isfile(os.path.join(pratice_files_path, f))]

        # if there are files in practice_files
        if files_names_in_pf_folder != []:
            for file in files_names_in_pf_folder:
                # delete any files that are currently in this folder
                file_path = os.path.join(pratice_files_path, file)
                try:
                    os.remove(file_path)
                except OSError as e:
                    print(f"Error: {file_path} : {e.strerror}")

        # now there are no files in practice_files, so fill with proper files
        # if the practice_files_path is a valid path
        if os.path.exists(pratice_files_path):
            # make test1, test2, test3
            open(os.path.join(pratice_files_path, 'test1.txt'), 'w').close
            open(os.path.join(pratice_files_path, 'test2.txt'), 'w').close
            open(os.path.join(pratice_files_path, 'test3.txt'), 'w').close

    def test_folder_init(self):
        """Test Folder Initializer
        Tests the __init__() if the folder class. A folder should 
        immediately read in its contents on creation. 
        """
        # make a usable path for the folder object
        current_dir = os.path.dirname(__file__)
        fol_path = os.path.join(current_dir, './practice_files')

        # create new folder object
        test_fol = Folder(folder_path=fol_path)

        # check folder object has the right number of files in practice_files
        self.assertEqual(len(test_fol.files), 3)


if __name__ == '__main__':
    unittest.main()
