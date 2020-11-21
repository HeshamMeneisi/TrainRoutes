import unittest

from main import create_arg_parser


class TestCli(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCli, self).__init__(*args, **kwargs)
        self.parser = create_arg_parser()

    def test_default_args(self):
        args = self.parser.parse_args([])
        self.assertEqual('routes.csv', args.routes_file)

    def test_custom_file(self):
        args = self.parser.parse_args(['--routes-file', 'test.csv'])
        self.assertEqual('test.csv', args.routes_file)

    def test_origin_target(self):
        args = self.parser.parse_args(['--origin', 'A', '--dest', 'B'])
        self.assertEqual('A', args.origin)
        self.assertEqual('B', args.dest)
