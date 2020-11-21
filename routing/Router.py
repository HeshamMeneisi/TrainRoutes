import os
from typing import Union
from generic import PriorityQueue
from .Exceptions import InvalidStationError

from .Segment import Segment
from .Route import Route


class Router(object):
    _segments: list[Segment]
    _stations: set[str]
    _outgoing_seg_lookup: dict[str, (str, Union[int, float])]

    def __init__(self, routes_file_path):
        self._segments = self._read_routes_file(routes_file_path)
        self._stations = set([r.s1 for r in self._segments] + [r.s2 for r in self._segments])
        self._outgoing_seg_lookup = {}
        for seg in self._segments:
            if seg.s1 not in self._outgoing_seg_lookup:
                self._outgoing_seg_lookup[seg.s1] = []
            self._outgoing_seg_lookup[seg.s1].append(seg)

    @staticmethod
    def _read_routes_file(routes_file_path) -> list[Segment]:
        if not os.path.exists(routes_file_path):
            raise FileNotFoundError
        if os.path.isdir(routes_file_path):
            raise IsADirectoryError

        with open(routes_file_path) as f:
            return [Segment.from_string(line) for line in f.readlines() if line]

    def has_station(self, station) -> bool:
        return station in self._stations

    def find_route(self, origin, dest) -> Union[Route, None]:
        if not len(self._segments):
            return None
        if not self.has_station(origin):
            raise InvalidStationError(origin)
        if not self.has_station(dest):
            raise InvalidStationError(dest)

        priority_list = [(0 if st == origin else float('inf'), st) for st in self._stations]

        st_queue = PriorityQueue(priority_list)
        prev_lookup = dict([(st, None) for st in self._stations])
        min_dist_record = {}

        while len(st_queue):
            st, dist = st_queue.pop()
            min_dist_record[st] = dist

            if st not in self._outgoing_seg_lookup:
                continue
            for seg in self._outgoing_seg_lookup[st]:
                n_st = seg.s2
                n_dist = st_queue.priority(n_st)
                if n_dist is None:
                    continue
                alt_dist = dist + seg.time
                if alt_dist < n_dist:
                    prev_lookup[n_st] = st
                    st_queue.update(n_st, alt_dist)

            if st == dest:
                break

        path = []
        st = dest
        while st != origin:
            prev_st = prev_lookup[st]
            if not prev_st:
                return None
            path.append(Segment(prev_st, st, min_dist_record[st] - min_dist_record[prev_st]))
            st = prev_st

        return Route(reversed(path))
