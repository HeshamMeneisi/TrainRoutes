import unittest

from routing.Exceptions import InvalidRecordError
from routing.Route import Route


class RouteTests(unittest.TestCase):
    def test_base_case(self):
        r = Route.from_string('A,B,1.01')
        self.assertEqual('A', r.s1)
        self.assertEqual('B', r.s2)
        self.assertEqual(1.01, r.time)

    def test_handling_spaces(self):
        r = Route.from_string(' A , B , 1.01 ')
        self.assertEqual('A', r.s1)
        self.assertEqual('B', r.s2)
        self.assertEqual(1.01, r.time)

    def test_handling_extra_values(self):
        r = Route.from_string('A,B,4,??')
        self.assertEqual('A', r.s1)
        self.assertEqual('B', r.s2)
        self.assertEqual(4, r.time)

    def test_with_int(self):
        r = Route.from_string('A,B,2')
        self.assertEqual(2, r.time)

    def test_error_handling(self):
        try:
            Route.from_string('A,B,C')
        except Exception as ex:
            self.assertEqual(InvalidRecordError, type(ex))

        try:
            Route.from_string('A,B')
        except Exception as ex:
            self.assertEqual(InvalidRecordError, type(ex))
