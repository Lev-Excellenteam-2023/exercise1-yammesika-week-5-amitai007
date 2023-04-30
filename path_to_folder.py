# region path to a folder-this is the way
import os



    
def path_to_folder(path): 
    """function that receives a path to a folder,
    and returns the list of all files that start with the sequence of letters "deep" in that folder.
    """
    return [file for file in os.listdir(path) if file.startswith('deep')]



# endregion

if __name__ == '__main__':
    path = input('Enter path to folder: ')
    output = path_to_folder(path)
    print(output)
    
