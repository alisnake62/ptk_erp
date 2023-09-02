
from datetime import datetime

from util.date import DateTimeUtil

class TestDatetime:

    def test_datetimify(self, mocker):

        datetime_util = DateTimeUtil()

        datetime_str = "2023-08-30T03:16:28.440Z"

        datetime_result = datetime_util.datetimify(datetime_str=datetime_str)

        assert datetime_result == datetime(year=2023, month=8, day=30, hour=3, minute=16, second=28)

    def test_stringify(self, mocker):

        datetime_util = DateTimeUtil()

        datetime_to_stringify = datetime(year=2023, month=8, day=30, hour=3, minute=16, second=28)

        datetime_str = datetime_util.stringify(datetime_to_stringify=datetime_to_stringify)

        assert datetime_str == "2023-08-30T03:16:28.000Z"