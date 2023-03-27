# region path to a folder-this is the way
import os


def path_to_folder():
    """function that receives a path to a folder,
    and returns the list of all files that start with the sequence of letters "deep" in that folder.
    """
    path = input('Enter path to folder: ')
    list_of_files = os.listdir(path)
    for file in list_of_files:
        if file.startswith('deep'):
            print(file)
    return list_of_files


# endregion