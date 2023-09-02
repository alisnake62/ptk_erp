from datetime import datetime

class DateTimeUtil:

    def datetimify(self, datetime_str: str) -> datetime:

        datetime_str = datetime_str[:19]
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')

    def stringify(self, datetime_to_stringify: datetime) -> str:

        datetime_str = datetime_to_stringify.strftime('%Y-%m-%dT%H:%M:%S')
        return datetime_str + ".000Z"