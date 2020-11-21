from heapq import heappush, heappop, heapify
from typing import TypeVar, Generic, Union, Iterator

T = TypeVar('T')
PriorityType = Union[int, float]


class Entry(Generic[T]):
    key: T
    priority: PriorityType
    deleted: bool

    def __init__(self, key: T, priority: PriorityType):
        self.key = key
        self.priority = priority
        self.deleted = False

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority


class PriorityQueue(Generic[T]):
    count: int
    pq: list[Entry]
    entry_lookup: dict[T, Entry]

    def __init__(self, values: Iterator[tuple[PriorityType, T]] = None):
        self.pq = [Entry(v[1], v[0]) for v in values] or []
        self.entry_lookup = {}

        if values:
            heapify(self.pq)
            for entry in self.pq:
                self.entry_lookup[entry.key] = entry
        self.count = len(self.pq)

    def __len__(self):
        return self.count

    def push(self, key: T, priority: PriorityType = 0) -> None:
        if key in self.entry_lookup:
            self.remove(key)
        entry = Entry(key, priority)
        self.entry_lookup[key] = entry
        heappush(self.pq, entry)
        self.count += 1

    def remove(self, key: T) -> None:
        entry = self.entry_lookup.pop(key)
        entry.deleted = True
        self.count -= 1

    def pop(self) -> (T, PriorityType):
        if not self.count:
            raise Exception('queue is empty')

        while True:
            entry = heappop(self.pq)
            if entry.deleted:
                continue
            del self.entry_lookup[entry.key]
            self.count -= 1
            return entry.key, entry.priority
    
    def update(self, key: T, new_priority: PriorityType):
        self.remove(key)
        self.push(key, new_priority)

    def priority(self, key: T) -> PriorityType:
        if key not in self.entry_lookup:
            return None
        return self.entry_lookup[key].priority
