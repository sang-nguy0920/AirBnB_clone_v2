#!/usr/bin/python3
""" module containts unittests for our console """

from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand
import os
import models
import unittest
import json
import sys
from unittest.mock import patch


class testConsole(unittest.TestCase):

    """ unittests for console """

    def test_created_console(self):
        """ Datetime at creation of an object from console """

    def test_updated_console(self):
        """ Datetime at update of an object from console """

    def test_create(self):
        """ Test creation of new instances in the console """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help create")

    def test_show(self):
        """ Test retrieval of data from show command """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help show")

    def test_destroy(self):
        """ Test to destroy instance from file storage """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help destroy")

    def test_all(self):
        """ Tests printing of all instances in storage with attributes """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help all")
            # self.assertEqual(file.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ Test update of instances from the console """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help update")

    def test_help(self):
        """ Test help commnand to display details of commands in console """
        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help")
