import unittest

from routing import Router, InvalidRecordError, InvalidStationError


class RouteTests(unittest.TestCase):
    @classmethod
    def _test_routing_case(cls, case: tuple[str, str, int, float], router: Router, context: unittest.TestCase):
        print(f'Testing case {case}')
        route = router.find_route(case[0], case[1])
        if case[2] is None:
            context.assertIsNone(route)
        else:
            context.assertIsNotNone(route)
            context.assertEqual(case[2], route.stop_count)
            context.assertEqual(case[3], route.total_time)

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

    def test_routing_cases(self):
        router = Router('tests/data/test_case_1.csv')
        cases = [
            ('A', 'A', 0, 0),
            ('A', 'B', 0, 5),
            ('A', 'C', 1, 10),
            ('E', 'J', 2, 30),
            ('A', 'D', 0, 15),
            ('H', 'I', 0, 10),
            ('A', 'J', None),
            ('C', 'G', None)
        ]

        for case in cases:
            self._test_routing_case(case, router, self)

    def test_error_handling(self):
        router = Router('tests/data/test_case_1.csv')

        try:
            router.find_route('A', 'Z')
        except Exception as ex:
            self.assertEqual(InvalidStationError, type(ex))

        try:
            router.find_route(None, '')
        except Exception as ex:
            self.assertEqual(InvalidStationError, type(ex))
