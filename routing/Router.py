import os
from routing.Route import Route


class Router(object):
    def __init__(self, routes_file_path):
        self.routes = self._read_routes_file(routes_file_path)

    @staticmethod
    def _read_routes_file(routes_file_path) -> list[Route]:
        if not os.path.exists(routes_file_path):
            raise FileNotFoundError
        if os.path.isdir(routes_file_path):
            raise IsADirectoryError

        with open(routes_file_path) as f:
            return [Route.from_string(line) for line in f.readlines()]
