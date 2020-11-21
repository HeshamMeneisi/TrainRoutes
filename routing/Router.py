import os
from .Segment import Segment


class Router(object):
    def __init__(self, routes_file_path):
        self.segments = self._read_routes_file(routes_file_path)
        self.stations = set([r.s1 for r in self.segments] + [r.s2 for r in self.segments])

    @staticmethod
    def _read_routes_file(routes_file_path) -> list[Segment]:
        if not os.path.exists(routes_file_path):
            raise FileNotFoundError
        if os.path.isdir(routes_file_path):
            raise IsADirectoryError

        with open(routes_file_path) as f:
            return [Segment.from_string(line) for line in f.readlines() if line]

    def has_station(self, station) -> bool:
        return station in self.stations
