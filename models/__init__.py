!/usr/bin/python3
"""A file that manages the fiile storage"""

from models.engine.file_storage import FileStorage

storage = FileStorage() # create a unique FileStorage instance
storage.reload() # call the reload method on the instance
