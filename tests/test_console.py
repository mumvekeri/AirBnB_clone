#!/usr/bin/python3
"""This is a test file for console.py"""

import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommandTest(unittest.TestCase):

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_quit(self, mock_stdout):
        """Test do_quit exits the console."""
        command = HBNBCommand()
        self.assertTrue(command.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_EOF(self, mock_stdout):
        """Test do_EOF exits the console."""
        command = HBNBCommand()
        self.assertTrue(command.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_help(self, mock_stdout):
        """Test do_help prints the help message."""
        command = HBNBCommand()
        command.onecmd("help")
        self.assertEqual(mock_stdout.getvalue().startswith("Documented commands"), True)

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_create_user(self, mock_stdout):
        """Test do_create successfully creates a User instance."""
        command = HBNBCommand()
        command.onecmd("create User")
        self.assertTrue(mock_stdout.getvalue().startswith("**"))
        self.assertEqual(len(storage.all().values()), 1)
        instance = list(storage.all().values())[0]
        self.assertIsInstance(instance, User)

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_create_invalid_class(self, mock_stdout):
        """Test do_create prints error message for invalid class."""
        command = HBNBCommand()
        command.onecmd("create InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_all(self, mock_stdout):
        """Test do_all prints all instances of a class."""
        user1 = User()
        user2 = User()
        storage.save()
        command = HBNBCommand()
        command.onecmd("all User")
        output = mock_stdout.getvalue()
        self.assertIn(str(user1), output)
        self.assertIn(str(user2), output)

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_all_invalid_class(self, mock_stdout):
        """Test do_all prints error message for invalid class."""
        command = HBNBCommand()
        command.onecmd("all InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_count(self, mock_stdout):
        """Test do_count prints the number of instances of a class."""
        user1 = User()
        user2 = User()
        storage.save()
        command = HBNBCommand()
        command.onecmd("count User")
        self.assertEqual(mock_stdout.getvalue(), f"There are 2 instances of User\n")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_count_invalid_class(self, mock_stdout):
        """Test do_count prints error message for invalid class."""
        command = HBNBCommand()
        command.onecmd("count InvalidClass")
        self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")

    @mock.patch('sys.stdout', new=StringIO())
    def test_do_show(self, mock_stdout):
        """Test do_show prints the string representation of an instance."""
        user = User()
        storage.save()
        command = HBNBCommand()
        command.onecmd(f"show User {user.id}")
        self.assertIn(str(user), mock_stdout.getvalue())

    @mock.patch('sys.stdout', new=StringIO())

