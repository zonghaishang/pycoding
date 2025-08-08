import json

JSON_PATH = 'osconfeed-sample.json'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'


def load(path=JSON_PATH):
    records = {}
    with open(path) as fp:
        raw_data = json.load(fp)

    for collection, raw_records in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in raw_records:
            key = f'{record_type}.{record["serial"]}'
            records[key] = Record(**record)

    return records


if __name__ == '__main__':
    records = load(JSON_PATH)
    speaker = records['speaker.157509']
    print(speaker)
    print(speaker.name, speaker.twitter)
