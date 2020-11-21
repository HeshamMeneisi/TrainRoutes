from typing import Iterator

from .Segment import Segment


class Route(object):
    path: list[Segment]

    def __init__(self, path: Iterator[Segment]):
        self.path = list(path)

    @property
    def stop_count(self) -> int:
        return max(0, len(self.path) - 1)

    @property
    def total_time(self) -> float:
        return sum([seg.time for seg in self.path])
