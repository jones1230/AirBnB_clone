#!/usr/bin/python3
"""
Initializes the package by creating an instance of FileStorage and
reloading any stored objects from the file.

Imports:
    - FileStorage: The class responsible for managing object storage in a
        JSON file.
"""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload any existing objects from the file
storage.reload()
