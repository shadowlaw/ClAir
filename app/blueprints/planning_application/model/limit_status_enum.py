from enum import Enum


class LimitStatus(Enum):
    UNDER_LIMIT = 'UL'
    OVER_LIMIT = 'OL'

    @staticmethod
    def get_safe_limit_status(safe_level, actual_level):
        return LimitStatus.OVER_LIMIT if float(safe_level) - float(actual_level) < 0 else LimitStatus.UNDER_LIMIT
