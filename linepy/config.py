# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gwx.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gwx.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gwx.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
        'ANDROID': '8.14.2',
        'IOS': '8.14.2',
        'ANDROIDLITE': '2.1.0',
        'BIZANDROID': '1.7.2',
        'BIZIOS': '1.7.5',
        'BIZWEB': '1.0.22',
        'DESKTOPWIN': '5.9.0',
        'DESKTOPMAC': '5.9.0',
        'IOSIPAD': '8.14.2',
        'CHROMEOS': '2.1.5',
        'WIN10': '5.5.5',
        'DEFAULT': '8.11.0'
    }

    APP_TYPE    = 'IOS'
    APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'ShahZain'
    SYSTEM_VER  = '8.20.9'
    IP_ADDR     = '1.1.1.1'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self, appType=None):
        if appType:
            self.APP_TYPE = appType
            self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        self.APP_NAME = 'IOS 16.34 macOS 10.13'
        self.USER_AGENT = 'Line/2017.0731.2132 CFNetwork/609.1.4.Darwin/13.0.0'
