from datetime import date

import pytest

from models.date_range import DateRange


class TestDateRange:
    def test_valid_date_range(self):
        dr = DateRange(start_date=date(2023, 1, 1), end_date=date(2023, 12, 31))
        assert dr.start_date == date(2023, 1, 1)
        assert dr.end_date == date(2023, 12, 31)
    def test_invalid_date_range(self):
        with pytest.raises(ValueError):
            DateRange(start_date=date(2023, 12, 31), end_date=date(2023, 1, 1))