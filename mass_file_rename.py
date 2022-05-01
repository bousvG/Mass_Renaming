"""Mass File Rename
By Anthony, Nic, George, and Conor

This package allows for the mass renaming of files at a given directory
following a defined name scheme. 
"""

import os


class File:

    def __init__(self, file_path=''):
        """File Object
        An instance of this class represents a file.
        A file has a name, path, and extension.
        All a file can do is change it's own name.
        Comprised of a path, root_path, name, and ext.
        """
        # initialize member variables.
        self.file_path = file_path
        self.set_name_ext_root_dir()

    def set_name_ext_root_dir(self):
        """Set Name, Extension, and Root Directory
        Set the extension, name, and root directory of
        this file based on self.file_path
        """
        split_file = os.path.splitext(self.file_path)
        self.ext = split_file[1]
        self.root_dir, self.name = os.path.split(split_file[0])

    def change_name_to(self, new_name=''):
        """Change Name to New Name
        Changes this file's name to new_name.
        Returns nothing.
        """
        # create the new file path from the root_dir and new_name
        renamed_file_path = os.path.join(
            self.root_dir, f"{new_name}{self.ext}")

        # if self.file_path is a file that exists
        if os.path.isfile(self.file_path):
            # if new_name is not already taken
            if not os.path.isfile(renamed_file_path):
                # execute rename of file in system
                os.rename(self.file_path, renamed_file_path)

                # set new name, path, and ext for this file obj
                self.file_path = renamed_file_path
                self.set_name_ext_root_dir()
            else:
                print(f"~~~NAME '{new_name}{self.ext}' ALREADY TAKEN~~~")
        else:
            print(f"~~~NO FILE FOUND AT '{self.file_path}'~~~")

    def change_ext_to(self, new_ext=''):
        """Change Extension to New Extension
        Changes this file's extension to new_ext.
        Returns nothing.
        """
        self.ext = new_ext

    def get_name(self):
        return self.name

    def get_ext(self):
        return self.ext


class Folder:

    def __init__(self, folder_path):
        """Folder Object
        An instance of this class represents a Folder.
        A folder has a name, path, a list of folders it contains,
        and list of files it contains.
        A folder is used to organize and extract the group of files
        you are looking to rename. 
        """
        # initialize member variables.
        self.folder_path = folder_path
        self.name = self.get_name_from_path()
        self.files = self.read_in_files_at_path()

    def get_name_from_path(self):
        """Get Name From Path
        Get the name of this folder from the path it was initialized with.
        Return string representing the name of this folder. 
        """
        return os.path.split(self.folder_path)[1]

    def read_in_files_at_path(self):
        """Read in Files at Path
        Reads in the data from all files in this folder's path.
        Returns a list of files.
        """
        # get a list of the names of all files in this folder
        list_of_file_names = [f for f in os.listdir(
            self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

        list_of_file_objects = []
        # for every file in this folder
        for file_name in list_of_file_names:
            # create a new file object with the path to this file
            file = File(file_path=os.path.join(self.folder_path, file_name))

            # add this file to the list of file objects
            list_of_file_objects.append(file)

        # return complete list of all files in this folder
        return list_of_file_objects

    def get_all_with_ext(self, criteria):
        """Get all with Extension
        Returns a list of all files in this folder with an extension
        that matches the given criteria.
        """
        returnFiles = []
        allFiles = self.get_all()
        for fileObj in allFiles:
            if criteria in fileObj.get_ext():
                returnFiles.append(fileObj)

        return returnFiles

    def get_all_contains(self, criteria):
        """Get all Contains
        Returns a list of all files in this folder with a name that
        contains the given criteria.
        """
        returnFiles = []
        allFiles = self.get_all()
        for fileObj in allFiles:
            if criteria in fileObj.get_name():
                returnFiles.append(fileObj)
        return returnFiles

    def get_all(self):
        """Get all
        Returns a list of all files in this folder.
        """
        return self.files


class Renamer:

    def __init__(self, scheme):
        """Renamer Object
        An instance of this class represents an object used to
        help rename files in bulk. A Renamer has a naming scheme
        that dictates the way files are renamed.
        """
        # initialize member variables.
        self.scheme = scheme

    def rename_all(self, files):
        """Rename All
        Changes all the names of all files in the given list to
        the new name from this object's name scheme.
        Returns nothing.
        """
        # for every file in the given list of files
        for file in files:
            # get the new name from this object's name scheme
            new_name = self.scheme.construct_new_name(file.name)
            #
            file.change_name_to(new_name)

    def rename_if_contains(self, criteria, files):
        """Rename If Contains
        Changes all the names of all files in this folder that
        contain a given name criteria to the new name from this
        object's name scheme.
        Returns nothing.
        """
        # for every file in the given list of files
        for file in files:
            # if this file's name contians a given criteria
            if criteria in file.get_name():
                # for every new name generated by our name scheme
                new_name = self.scheme.construct_new_name(file.name)
                file.change_name_to(new_name)

    def rename_if_ext(self, criteria, files):
        """Rename If Extension
        Changes all the names of all files in this folder that
        match a given extension criteria to the new name from this
        object's name scheme.
        Returns nothing.
        """
        # for every file in the given list of files
        for file in files:
            # if this file's name contians a given criteria
            if criteria in file.get_ext():
                # for every new name generated by our name scheme
                new_name = self.scheme.construct_new_name(file.name)
                file.change_name_to(new_name)


class Scheme:

    def __init__(self, root=None, prefix=None, suffix=None, replacement=None):
        """Scheme Object
        An instance of this class represents a naming scheme.
        A Scheme has a root, a prefix object, a suffix object,
        and a replacement object.

        Developers should think of these parameters as their
        different options using this class. They can have all or
        one or some combination of the four.

        Developers can use both prefixes and suffixes, or neither
        if they want all files to be named the same as the root.

        Developers can also choose to ommit the root and include
        a replacement object. This will replace a string with
        another specified string where it is found in a the file
        name or file extension.

        If the root is left as None but there is a prefix or suffix
        and a replacement then this system should make the
        replacement, then set the new name to the root for the pefix
        or suffix.
        """
        # initialize member variables.
        self.root = root
        self.prefix = prefix
        self.suffix = suffix
        self.replacement = replacement

    def construct_new_name(self, file_name):
        """Construct New Name
        This method will contruct and return the next name in this name
        scheme. file_name is not needed for name schemes without 
        replacements.
        Returns a new name.
        """
        # complete the appropriate actions for all scheme parameters
        # replacement
        if self.replacement is not None:
            new_name = self.replacement.get_new_name(file_name)
            self.root = new_name

        # prefix
        pre = self.prefix.get_new_prefix() if self.prefix is not None else ''

        # suffix
        suf = self.suffix.get_new_suffix() if self.suffix is not None else ''

        # return fully constructed new name
        return f'{pre}{self.root}{suf}'


class Replacement:

    def __init__(self, criteria, replace):
        """Replacement Object
        An instance of this class represents the data in a replacement.
        A replacement consists of the criteria for a substring to be replaced
        and the string to replace it with. 
        """
        # initialize member variables.
        self.criteria = criteria
        self.replace = replace

    def get_new_name(self, current_name):
        """Get New Name
        This method will replace the first occurence of whatever substring in the 
        current_name specified by this class' criteria value with this class' 
        replace value.
        Returns this modified version of current_name.
        """
        return current_name.replace(self.criteria, self.replace, 1)


class Prefix:

    def __init__(self, identifier=None, separator=''):
        """Prefix Object
        An instance of this class represents a prefix of a name in a
        name scheme. It has a identifier and a separator.

        The identifier can be a just a string, or it can be one of the
        Identifier classes in this package (NumericalIdentifier and
        AlphabeticalIdentifier). The separator must be a string and can
        be left as whitespace if it is not needed.
        """
        # initialize member variables.
        self.identifier = identifier
        self.separator = separator

    def get_new_prefix(self):
        """Get New Prefix
        This method will return the combination of this class' separator
        and whatever the next identifier value is.
        """
        # get the next identifier in the sequence
        idf = self.identifier.get_next_id()

        # return constructed suffix
        return idf + self.separator


class Suffix:

    def __init__(self, identifier=None, separator=''):
        """Suffix Object
        An instance of this class represents a suffix of a name in a
        name scheme. It has a identifier and a separator.

        The identifier can be a just a string, or it can be one of the
        Identifier classes in this package (NumericalIdentifier and
        AlphabeticalIdentifier). The separator must be a string and can
        be left as whitespace if it is not needed.
        """
        # initialize member variables.
        self.identifier = identifier
        self.separator = separator

    def get_new_suffix(self):
        """Get New Suffix
        This method will return the combination of this class' separator
        and whatever the next identifier value is.
        """
        # get the next identifier in the sequence
        idf = self.identifier.get_next_id()

        # return constructed suffix
        return self.separator + idf


class NumericalIdentifier:

    def __init__(self, start=1, increment=1, character_length=None):
        """Numerical Identifier Object
        An instance of this class represents an identifier for a suffix or
        prefix that increases a number over time. This number has a starting
        value, a number to increment by for each sequential naming, and a
        character length that the identifier will adhere to (EX: length 4 would
        look like 0001, 0002, 0003, etc. Length None is the normal 1, 2, 3, etc.).
        """
        self.start = start
        self.increment = increment
        self.character_length = character_length
        self.current_identifier_value = start

        # lowest value for increment allowed is 1
        if increment <= 0:
            self.increment = 1

    def increment_id(self):
        """Increment Identifier
        This method will increase the current_identifier_value_by the interval specified
        by self.increment.
        Returns nothing.
        """
        self.current_identifier_value += self.increment

    def get_next_id(self):
        """Get Next Identifier
        Prepares and returns the value of current_identifier_value, and increments
        current_identifier_value member variable of this object.
        If this id must be of a certain character length, then the extra space
        is filled in by zeros.
        """
        # get current id in string form
        str_id = str(self.current_identifier_value)

        # if this id needs to be of a certain character length
        if self.character_length is not None:
            # if this id is not at the length it should be already
            if len(str_id) < self.character_length:
                # fill id with zeros to correct the character length
                str_id = str_id.rjust(self.character_length, '0')

        # increment id
        self.increment_id()

        # return prepared id
        return str_id


class AlphabeticalIdentifier:

    def __init__(self, start='A', increment=1, caps=True):
        """Alphabetical Identifier Object
        An instance of this class represents an identifier for a suffix or
        prefix that increases a letter over time. This letter has a starting
        value, a number of letters to increment by for each sequential naming,
        and a value that represents whether or not this identifier is using
        capital letters or lower case letters.
        Starts at A. Can be customized to start at any letter, and even sequences
        of letters (like 'AAAA'). Increments are only allowed to be integers greater 
        than 0. All else will be initialized to 1. Alphabetical Identifiers only 
        increase.
        """
        self.increment = increment
        self.start = start
        self.caps = caps
        self.current_identifier_value = start

        # lowest value for increment allowed is 1
        if (type(increment) is not int()) or (increment <= 0):
            self.increment = 1

    def get_next_id(self):
        """Get Next Identifier
        Prepares and returns the current_identifier_value, which should be the
        next id in the sequence for this name scheme. Corrects for upper or 
        lower case identifiers.
        """
        # if this object has been configured to use all capital letters
        if self.caps:
            # capture current id value as a string
            str_id = self.current_identifier_value.upper()
        # else this object has been configured to use all lowercase letters
        else:
            # capture current id value as a string
            str_id = self.current_identifier_value.lower()

        # increment identifier member variable for this object
        self.increment_id()

        # return prepared string id
        return str_id

    def increment_id(self):
        """Increment Identifier
        This method will increase the current_identifier_value by the interval specified
        by the increment parameter of this class.
        Returns nothing.
        """
        # get the next id for however many steps defined by the increment parameter
        for _ in range(self.increment):
            next_id = self.get_next_letter(self.current_identifier_value)

        # set this object's current id value to this incremented id
        self.current_identifier_value = next_id

    def get_next_letter(self, letter_id):
        """Get Next Letter
        This method uses recursion to get the next letter in a sequence of letters.
        Can rollover value in the case that the current letter is z, so the next
        letters would be aa. Cases with more that two letters will work rollover
        similarly (EX: ABZ -> ACA, etc.)
        Returns the next letter or letter in the sequence.
        """
        if letter_id == '':
            return 'A'

        # initialize a list of letters in alphabetic order
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        # initialize front of id and last letter id
        last_letter = list(letter_id)[-1]
        front_letters = ''

        # if this letter_id is longer than 1 character, we may need to roll over
        if (len(letter_id) > 1):
            # for the string of all letters before the last letter
            for letter in list(letter_id):
                # add the next letter to front_letters
                front_letters = front_letters + letter

                # break when all letters have been added besides the last
                if len(front_letters) == (len(letter_id) - 1):
                    break  # the purpose of this is to produce a

        # for every letter of the alphabet (in alphabetical order)
        for i in range(len(letters)):
            # if the current id val ends with the current letter
            if last_letter.casefold() == letters[i].casefold():
                # if this letter is A through Y
                if i < (len(letters) - 1):
                    # concatenate the next letter with the front letters
                    return front_letters + letters[i+1]
                # else this letter is Z, we will rollover to add a new letter to the front
                else:
                    # concatenate with the rolled over front letters
                    return f'{self.get_next_letter(front_letters)}A'
