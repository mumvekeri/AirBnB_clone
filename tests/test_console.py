#!/usr/bin/python3
"""These are test cases fo functions in console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertTrue("Documented commands (type help <topic>):" in output)

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Check if a valid UUID is returned

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as mock_stdout_show:
                self.console.onecmd(f"show BaseModel {obj_id}")
                output_show = mock_stdout_show.getvalue().strip()
                self.assertTrue(f"BaseModel {obj_id}" in output_show)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as mock_stdout_destroy:
                self.console.onecmd(f"destroy BaseModel {obj_id}")
                output_destroy = mock_stdout_destroy.getvalue().strip()
                self.assertTrue(len(output_destroy) == 0)  # Check if no output is returned

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            obj_id = mock_stdout.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as mock_stdout_update:
                self.console.onecmd(f"update BaseModel {obj_id} name 'NewName'")
                output_update = mock_stdout_update.getvalue().strip()
                self.assertTrue(len(output_update) == 0)  # Check if no output is returned

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            output_all = mock_stdout.getvalue().strip()
            self.assertTrue(output_all == "[]")  # Check if empty list is returned

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output_count = mock_stdout.getvalue().strip()
            self.assertTrue("There are 1 instances of BaseModel" in output_count)

    def test_default_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("nonexistent_command")
            output_default = mock_stdout.getvalue().strip()
            self.assertTrue("** command not recognized **" in output_default)

if __name__ == '__main__':
    unittest.main()

