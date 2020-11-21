import unittest

from routing import Router, InvalidRecordError


class RouteTests(unittest.TestCase):
    def test_initialization(self):
        try:
            Router('non_existent_file.csv')
        except Exception as ex:
            self.assertEqual(FileNotFoundError, type(ex))

        try:
            Router('tests/data')
        except Exception as ex:
            self.assertEqual(IsADirectoryError, type(ex))

        try:
            Router('tests/data/invalid_file.csv')
        except Exception as ex:
            self.assertEqual(InvalidRecordError, type(ex))
