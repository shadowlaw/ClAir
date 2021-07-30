from enum import Enum


class AQIStatus(Enum):
    GD = 'GD'
    MD = 'MD'
    UHSG = 'UHSG'
    UH = 'UH'
    VUH = 'VUH'
    HDZ = 'HDZ'

    @staticmethod
    def get_status(reading):
        if 0 <= reading <= 50:
            return AQIStatus.GD
        if 51 <= reading <= 100:
            return AQIStatus.MD
        if 101 <= reading <= 150:
            return AQIStatus.UHSG
        if 151 <= reading <= 200:
            return AQIStatus.UH
        if 201 <= reading <= 300:
            return AQIStatus.VUH
        if 301 <= reading <= 500:
            return AQIStatus.HDZ
