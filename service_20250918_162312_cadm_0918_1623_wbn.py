# 代码生成时间: 2025-09-18 16:23:12
import os
import streamlit as st
from pathlib import Path

"""
Folder Structure Organizer App
==================

This application is designed to take a directory path as input, and it will attempt to organize the folder structure,
whereby moving all files to a 'Files' sub-folder and all sub-directories to a 'Folders' sub-folder.

Attributes:
    source_path (str): The path of the directory to be organized.

Methods:
    validate_path(path): Validates whether the provided path is a valid directory.
    move_files_to_subfolder(files, dest_folder): Moves all files to the specified sub-folder.
    move_folders_to_subfolder(folders, dest_folder): Moves all sub-directories to the specified sub-folder.
    organize_folder_structure(source_path): Organizes the folder structure by separating files and folders.

Example:
    To use this application, run it using Streamlit and provide a directory path. The application will organize the folder accordingly.
"""

# Streamlit components
st.title('Folder Structure Organizer')

# User input for source directory path
source_path = st.text_input('Enter the directory path:', '')

if st.button('Organize Folder Structure'):
    # Validate the provided path
    if source_path and validate_path(source_path):
        # Organize the folder structure
        organize_folder_structure(source_path)
        st.success('Folder structure organized successfully!')
    else:
        st.error('Invalid directory path provided.')


def validate_path(path):
    """
    Validates whether the provided path is a valid directory.

    Args:
        path (str): The directory path to be validated.

    Returns:
        bool: True if the path is a valid directory, False otherwise.
    """
    return Path(path).is_dir()


def move_files_to_subfolder(files, dest_folder):
    """
    Moves all files to the specified sub-folder.

    Args:
        files (list): List of file paths to be moved.
        dest_folder (str): Path of the destination sub-folder.
    """
    for file in files:
        dest_path = os.path.join(dest_folder, os.path.basename(file))
        os.rename(file, dest_path)


def move_folders_to_subfolder(folders, dest_folder):
    """
    Moves all sub-directories to the specified sub-folder.

    Args:
        folders (list): List of folder paths to be moved.
        dest_folder (str): Path of the destination sub-folder.
    """
    for folder in folders:
        dest_path = os.path.join(dest_folder, os.path.basename(folder))
        os.rename(folder, dest_path)


def organize_folder_structure(source_path):
    """
    Organizes the folder structure by separating files and folders.

    Args:
        source_path (str): The path of the directory to be organized.
    """
    # Create 'Files' and 'Folders' sub-folders if they don't exist
    files_folder = os.path.join(source_path, 'Files')
    folders_folder = os.path.join(source_path, 'Folders')
    os.makedirs(files_folder, exist_ok=True)
    os.makedirs(folders_folder, exist_ok=True)

    # Separate files and folders
    files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
    folders = [f for f in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, f))]

    # Move files to 'Files' sub-folder
    move_files_to_subfolder(files, files_folder)

    # Move folders to 'Folders' sub-folder
    move_folders_to_subfolder(folders, folders_folder)

    # Move 'Files' and 'Folders' sub-folders to the root of the source_path if they are empty
    if not os.listdir(files_folder):
        os.rmdir(files_folder)
    if not os.listdir(folders_folder):
        os.rmdir(folders_folder)