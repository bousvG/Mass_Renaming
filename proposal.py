"""Conor's proposal.
I wanted to flesh out the structure of the package. I think a few classes
would help us organize our code better. Here's what I came up with:

If you want to rename some files, first determine your
naming scheme. Create a Scheme object that reflects this 
scheme.

Next, create Folder objects that represent the folders 
where your files are. You can use these folder objects to
spit out a of subset of the folder's contents to be renamed.

Now, create a Renamer object with your scheme. This object
will be used to execute the renaming. Or rather, instruct
each file to rename itself a spefic name. The renamer will
use the provided naming scheme to rename the files.
"""


class File:

    # relevant data about a file
    name = ''
    ext = ''
    path = ''

    def __init__(self, path):
        """File object
        An instance of this class represents a file.
        A file has a name, path, and extension.
        All a file can do is change it's own name.
        """
        self.path = path
        # derive the name and extension from the path

    def change_name_to(self, new_name):
        """Changes this file's name to new_name.
        Returns nothing.
        """
        pass


class Folder:

    # relevant data about a folder
    name = ''
    path = ''
    files = []
    subfolders = []

    def __init__(self, path):
        """Folder object
        An instance of this class represents a Folder.
        A folder has a name, path, a list of folders it contains, 
        and list of files it contains.
        A folder can rename all the files to a spefic
        """
        self.path = path
        # derive the name from the path
        # read in all files contained in this folder for files


class Scheme:

    # relevant data about a scheme
    base = ''
    prefix_start = ''
    suffix_start = ''
    change_prefix_by = ''
    change_suffix_by = ''

    def __init__(self, base='', prefix_start='', suffix_start='',
                 change_prefix_by='', change_suffix_by=''):
        """Scheme object
        An instance of this class represents a naming scheme.
        A Scheme has a base, prefix, suffix, and how to change
        the prefix/suffix with each new file.

        So if you want to name your files image1, image2, etc.,
        your base = image, your suffix_start = 1, and 
        change_suffix_by = 1. 
        If you want to name your files image200, image199, etc.,
        your base = image, your suffix_start = 200, and 
        change_suffix_by = -1. 

        So if you want to name your files imagea, imageb, etc.,
        your base = image, your suffix_start = a, and 
        change_suffix_by = 1. 
        If you want to name your files imagez, imagey, etc.,
        your base = image, your suffix_start = z, and 
        change_suffix_by = -1. 

        Same same rules apply to prefixes. User can use both
        prefixes and suffixes or neither if they want all
        files to be names the same as the base.
        """
        self.base = base
        self.prefix_start = prefix_start
        self.suffix_start = suffix_start
        self.change_prefix_by = change_prefix_by
        self.change_suffix_by = change_suffix_by


class Renamer:

    def __init__(self, scheme):
        """Renamer object
        An instance of this class represents an object used to re.
        A folder has a naming scheme that dictates the way files
        are renamed.
        """
        self.scheme = scheme

    def rename_all(self, new_name, files):
        """Changes all the names of all files in this folder to 
        new_name.
        Returns nothing.
        """
        pass

    def rename_if_contains(self, criteria, new_name, files):
        """Changes all the names of all files in this folder that 
        match a given name criteria to new_name.
        Returns nothing.
        """
        pass

    def rename_if_ext(self, criteria, new_name, files):
        """Changes all the names of all files in this folder that 
        match a given extension criteria to new_name.
        Returns nothing.
        """
        pass
