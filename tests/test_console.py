#!/usr/bin/python3
""" module containts unittests for our console """


import unittest
import json
from .models.base_model import BaseModel
from .models.engine.file_storage import FileStorage
from unittest.mock import patch


class TestConsole(unittest.TestCase):

    """ unittests for console """

    def test_created_console(self):
        """ Datetime at creation of an object from console """

    def test_updated_console(self):
        """ Datetime at update of an object from console """

    def test_create(self):
        """ Test creation of new instances in the console """
        with patch('sys.stdout', new=STRINGIO()) as file:
            HBNBCommand.().omecmd("create said NAH")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_show(self):
        """ Test retrieval of data from show command """
        with patch('sys.stdout', new=STRINGIO()) as file:
            HBNBCommand().onecmd("show said NAH")
            self.assertEqual(file.getvalue(), "\n** class name missing **\n")

    def test_destroy(self):
        """ Test to destroy instance from file storage """
        with patch('sys.stdout', new=STRINGIO()) as file:
            HBNBCommand().onecmd("destroy said NAH")
            self.assertEqual(file.getvalue(), "\n** class name missing **\n")

    def test_all(self):
        """ Tests printing of all instances in storage with attributes """
        with patch('sys.stdout', new=STRINGIO()) as file:
            HBNBCommand().onecmd("test all said NAH")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ Test update of instances from the console """
        with patch('sys.stdout', new=STRINGIO()) as file:
            HBNBCommand().onecmd("update said NAH")
            self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_EOF(self):
        """ EOF to quit console """

    def test_help(self):
        """ Test help commnand to display details of commands in console """

    def test_quit(self):
        """ Test that quit exits console """


if __name__ == "__main__":
    testConsole()
