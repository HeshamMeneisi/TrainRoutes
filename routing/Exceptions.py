class InvalidRecordError(Exception):
    def __init__(self, record: list, reason: str):
        super(InvalidRecordError, self).__init__(f'Record: {record} is invalid. Reason: {reason}')
