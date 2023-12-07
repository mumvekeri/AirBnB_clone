#!/usr/bin/python3
"""This is a test file for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    """A class to test the console"""

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(output.getvalue()) > 0)
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
