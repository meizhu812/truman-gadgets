# coding=utf-8
"""

"""
import os


def get_file(*, path: str, file_init: str, file_ext: str) -> str:
    for (dir_name, dirs_here, files_here) in os.walk(path):
        for file in files_here:
            if file.endswith(file_ext) and file.startswith(file_init):
                file_path = os.path.join(dir_name, file)
                return file_path


def get_files_list(*, path: str, file_init: str, file_ext: str) -> list:
    files_list = []
    for (dir_name, dirs_here, files_here) in os.walk(path):
        for file in files_here:
            if file.endswith(file_ext) and file.startswith(file_init):
                file_path = os.path.join(dir_name, file)
                files_list.append(file_path)
    return files_list
