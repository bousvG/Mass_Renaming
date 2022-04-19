"""Mass File Renamer
By Anthony, Nic, George, and Conor

If you want to rename some files, first determine your
naming scheme. Create a Scheme object that reflects this 
scheme.

Next, create Folder objects that represent the folders 
where your files are. You can use these folder objects to
spit out all or a of subset of the folder's contents as a 
list. This list will be input into the Renamer later.

Now, create a Renamer object with your scheme. This object
will be used to execute the renaming. Or rather, using the 
helper methods in the Renamer object, we instruct each file 
to rename itself a spefic name based on a given name scheme. 
"""


class File:

    def __init__(self, path=''):
        """File object
        An instance of this class represents a file.
        A file has a name, path, and extension.
        All a file can do is change it's own name.
        """
        # initialize member variables.
        self.path = path
        self.name = self.get_name_from_path()
        self.ext = self.get_ext_from_path

    def get_ext_from_path(self):
        """Get Extension From Path 
        Get the extension of this file from the path of this
        file.
        """
        pass

    def get_name_from_path(self):
        """Get Name From Path 
        Get the name of this file from the path of this file.
        """
        pass

    def change_name_to(self, new_name):
        """Changes this file's name to new_name.
        Returns nothing.
        """
        pass


class Folder:

    def __init__(self, path):
        """Folder object
        An instance of this class represents a Folder.
        A folder has a name, path, a list of folders it contains, 
        and list of files it contains.
        A folder can rename all the files to a spefic
        """

        # initialize member variables.
        self.path = path
        self.name = self.get_name_from_path()
        self.files, self.subfolders = self.read_in_contents()

    def get_name_from_path(self):
        """Set Name From Path
        Get the name of this folder
        """
        pass

    def read_in_contents(self):
        """Read in Files
        Reads in the data from all files and folders in this folder's
        path. 
        Returns a list of files and a list of subfolders.
        """
        pass

    def get_all_with_ext(self, criteria):
        """Get all with Extension
        Returns a list of all files in this folder with an extension
        that matches the given criteria.
        """
        pass

    def get_all_contains(self, criteria):
        """Get all Contains
        Returns a list of all files in this folder with a name that
        contains the given criteria.
        """
        pass


class Scheme:

    def __init__(self, base=None, prefix=None, suffix=None, replacement=None):
        """Scheme object
        An instance of this class represents a naming scheme.
        A Scheme has a base, a prefix object, a suffix object, 
        and a replacement object.

        Developers should think of these parameters as their 
        different options using this class. They can have all or 
        one or some combination. 

        Developers can use both prefixes and suffixes or neither 
        if they want all files to be named the same as the base.

        Developers can also choose to ommit the base and include 
        a replacement object. This will replace a string with 
        another specified string where it is found in a the file 
        name or file extension. 
        If the base is left as None but there is a prefix or suffix
        and a replacement then this system should make the 
        replacement, then set the new name to the base for the pefix
        or suffix.


        ~thoughts on design~
        The scheme is broken up into all those classes to make it 
        more readable and easier to understand when you were 
        coding. The alternative was having all the data that is 
        stored in those objects be a parameter in the constructor 
        of the scheme class, which would be unwieldy and might be 
        harder for a developer to conceptualize without more 
        concrete boundaries.
        """
        # initialize member variables.
        self.base = base
        self.prefix = prefix
        self.suffix = suffix
        self.replacement = replacement


class Renamer:

    def __init__(self, scheme):
        """Renamer object
        An instance of this class represents an object used to
        help rename files in bulk. A Renamer has a naming scheme 
        that dictates the way files are renamed.
        """
        # initialize member variables.
        self.scheme = scheme

    def rename_all(self, files):
        """Changes all the names of all files in the given list to 
        the new name from this object's name scheme.
        Returns nothing.
        """
        pass

    def rename_if_contains(self, criteria, files):
        """Changes all the names of all files in this folder that 
        contain a given name criteria to the new name from this
        object's name scheme.
        Returns nothing.
        """
        pass

    def rename_if_ext(self, criteria, files):
        """Changes all the names of all files in this folder that 
        match a given extension criteria to the new name from this
        object's name scheme.
        Returns nothing.
        """
        pass


class Prefix:

    def __init__(self, identifier='', separator='', change=None):
        """Prefix object
        An instance of this class represents a prefix of a name in a
        name scheme. It has a identifier, a separator, and the change
        over time. The change over time can be None, which will not 
        change 

        For example, in name scheme 
        """
        # initialize member variables.
        self.identifier = identifier
        self.separator = separator
        self.change = change


class Suffix:

    def __init__(self, identifier='', separator='', change=None):
        """Suffix object
        An instance of this class represents a suffix of a name in a
        name scheme. It has a identifier, a separator, and the change
        over time. The change over time can be None, which will not 
        change 

        For example, in name scheme 
        """
        # initialize member variables.
        self.identifier = identifier
        self.separator = separator
        self.change = change


class Replacement:

    def __init__(self, criteria, replace, text_type):
        """Replacement object
        An instance of this class represents the data in a replacement.
        A replacement consists of the criteria for a substring to be replaced
        and the string to replace it with. It also has the text_type, which 
        indicates if this replacement is happening to the file's extension,
        name or both. 
        """
        # initialize member variables.
        self.criteria = criteria
        self.replace = replace
        self.text_type = text_type
