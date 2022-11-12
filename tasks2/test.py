import os


def file_name(filenames: list, directory: str):
    """
        function gets filenames - list of file names in repository
        NEEDED:
            -find the longest name in list and save as parameter
            ??-check for unique symbols in filename??
            -compare lengths of other files w/parameter and add correct number of "_" for  demanded length
    """
    for name in filenames:
        f_name = name.partition('.')[0]
        set_name = set(f_name)
        if len(f_name) == len(set_name):
            print(f"symbols are unique in {name}")
        else:
            print(f"symbols are not unique in {name}")

    max_length = 0
    for name in filenames:
        f_name = name.partition('.')[0]
        if len(f_name) > max_length:
            max_length = len(f_name)

    for name in filenames:
        f_name = name.partition('.')[0]
        ext = name.partition('.')[2]
        if len(f_name) < max_length:
            old_name = directory + '/' + name
            new_name = directory + '/' + f_name + (max_length - len(f_name)) * '_' + '.' + ext
            os.rename(old_name, new_name)
            print(f"file {name} renamed into {f_name + (max_length - len(f_name)) * '_'}")
