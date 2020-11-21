from .Exceptions import InvalidRecordError


class Segment(object):
    def __init__(self, s1: str, s2: str, time: float):
        self.s1 = s1
        self.s2 = s2
        self.time = time

    @classmethod
    def from_string(cls, raw_record: str):
        record = [v.strip() for v in raw_record.split(",")[:3]]

        if len(record) < 3:
            raise InvalidRecordError(record, 'less than 3 values')

        try:
            time = float(record[2])
        except Exception:
            raise InvalidRecordError(record, 'third value (time) must be convertible to float')

        return cls(record[0], record[1], time)
