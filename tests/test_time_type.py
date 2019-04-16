"""
:author: Gatsby Lee
:since: 2019-04-10
"""
from mtdef import TimeType


def test_timetype_enum_value():
    """
    Test defined time_type enum value
    """

    assert TimeType.not_defined.value == -1
    assert TimeType.hour.value == 10
    assert TimeType.day.value == 20
    assert TimeType.week.value == 30
    assert TimeType.biweek.value == 40
    assert TimeType.month.value == 50
    assert TimeType.quarter.value == 60
    assert TimeType.semiyear.value == 70
    assert TimeType.year.value == 80


def test_timetype_lowercase_name():
    """
    Test defined time_type lowercase name
    """

    assert TimeType.not_defined.get_uppercase_name() == 'NOT_DEFINED'
    assert TimeType.hour.get_uppercase_name() == 'HOUR'
    assert TimeType.day .get_uppercase_name() == 'DAY'
    assert TimeType.week.get_uppercase_name() == 'WEEK'
    assert TimeType.biweek.get_uppercase_name() == 'BIWEEK'
    assert TimeType.month.get_uppercase_name() == 'MONTH'
    assert TimeType.quarter.get_uppercase_name() == 'QUARTER'
    assert TimeType.semiyear.get_uppercase_name() == 'SEMIYEAR'
    assert TimeType.year.get_uppercase_name() == 'YEAR'
