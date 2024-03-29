"""
:author: Gatsby Lee
:since: 2019-04-16
"""
from enum import Enum, unique


@unique
class TimeType(Enum):
    not_defined = -1
    hour = 10
    day = 20
    week = 30
    biweek = 40
    month = 50
    quarter = 60
    semiyear = 70
    year = 80

    def get_uppercase_name(self):
        return self.name.upper()

    def get_shortlower_name(self):
        return SHORT_NAME[self]

    @staticmethod
    def get_list():
        return [c for c in TimeType]


SHORT_NAME = {
    TimeType.not_defined: 'n/a',
    TimeType.hour: 'hh',
    TimeType.day: 'dd',
    TimeType.week: 'wk',
    TimeType.biweek: 'biwk',
    TimeType.month: 'mm',
    TimeType.quarter: 'qt',
    TimeType.semiyear: 'semiyy',
    TimeType.year: 'yy',
}

__all__ = (
    'TimeType',
)
