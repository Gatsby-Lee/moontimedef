"""
:author: Gatsby Lee
:since: 2019-04-10
"""
from mtimedef import TimeType


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


def test_timetype_name():
    """
    Test defined time_type lowercase name
    """

    assert TimeType.not_defined.name == 'not_defined'
    assert TimeType.hour.name == 'hour'
    assert TimeType.day.name == 'day'
    assert TimeType.week.name == 'week'
    assert TimeType.biweek.name == 'biweek'
    assert TimeType.month.name == 'month'
    assert TimeType.quarter.name == 'quarter'
    assert TimeType.semiyear.name == 'semiyear'
    assert TimeType.year.name == 'year'


def test_timetype_uppercase_name():
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


def test_timetype_enum_by_value():
    """
    Test defined time_type enum value
    """

    assert TimeType(-1) == TimeType.not_defined
    assert TimeType(10) == TimeType.hour
    assert TimeType(20) == TimeType.day
    assert TimeType(30) == TimeType.week
    assert TimeType(40) == TimeType.biweek
    assert TimeType(50) == TimeType.month
    assert TimeType(60) == TimeType.quarter
    assert TimeType(70) == TimeType.semiyear
    assert TimeType(80) == TimeType.year


def test_get_shortlower_name():
    """
    Test shorten and lower cased name.
    """

    assert TimeType.not_defined.get_shortlower_name() == 'n/a'
    assert TimeType.hour.get_shortlower_name() == 'hh'
    assert TimeType.day .get_shortlower_name() == 'dd'
    assert TimeType.week.get_shortlower_name() == 'wk'
    assert TimeType.biweek.get_shortlower_name() == 'biwk'
    assert TimeType.month.get_shortlower_name() == 'mm'
    assert TimeType.quarter.get_shortlower_name() == 'qt'
    assert TimeType.semiyear.get_shortlower_name() == 'semiyy'
    assert TimeType.year.get_shortlower_name() == 'yy'
