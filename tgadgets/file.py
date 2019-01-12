# coding=utf-8
"""

v1.0.0

Gadgets for simple files manipulation during data processing:
1. get_files_list:
    return a list of datafiles info of all files matching a certain pattern for later use

"""
import os


def get_files_list(*, path: str, file_init: str, file_ext: str) -> list:
    print(">>> Listing files in folder:\n" +
          "--> [{}]\n".format(path) +
          "--> [INIT]:'{}'\t".format(file_init) + "[EXT]:'{}'\n--|".format(file_ext))
    files_list = []
    for (dir_name, dirs_here, files_here) in os.walk(path):
        for file in files_here:
            if file.endswith(file_ext) and file.startswith(file_init):
                file_path = os.path.join(dir_name, file)
                files_list.append({'path': file_path, 'dir': dir_name, 'name': file})
    for file in files_list[:7]:  # print heads
        print("--| %s" % file['name'])
    print("--|" + 6 * "...")
    for file in files_list[-7:]:  # print tails
        print("--| %s" % file['name'])
    print('--|\n--# [ ' + str(len(files_list)) + ' ] files found.')
    input("### Check sequence of data files, press Enter to continue...\n")
    return files_list
