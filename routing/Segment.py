from .Exceptions import InvalidRecordError
from typing import Union


class Segment(object):
    s1: str
    s2: str
    time: Union[int, float]

    def __init__(self, s1: str, s2: str, time: Union[int, float]):
        self.s1 = s1
        self.s2 = s2
        self.time = time

    def __str__(self):
        return f'{self.s1} --({self.time})--> {self.s2}'

    @classmethod
    def from_string(cls, raw_record: str):
        record = [v.strip() for v in raw_record.split(",")[:3]]

        if len(record) < 3:
            raise InvalidRecordError(record, 'less than 3 values')

        try:
            time = int(record[2])
        except:
            try:
                time = float(record[2])
            except Exception:
                raise InvalidRecordError(record, 'third value (time) must be convertible to int/float')

        return cls(record[0], record[1], time)
