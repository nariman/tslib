#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.response.

The MIT License (MIT)

Copyright (c) 2015-2016 Nariman Safiulin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import abc
import logging
from collections import OrderedDict
from enum import Enum
from tslib.exception import UnknownEventTypeError

logger = logging.getLogger(__name__)


# TODO: Check all types of events
class EventType(Enum):
    SERVER_EDITED = "notifyserveredited"
    CHANNEL_CREATED = "notifychannelcreated"
    CHANNEL_EDITED = "notifychanneledited"
    CHANNEL_DESCRIPTION_CHANGED = "notifychanneldescriptionchanged"
    CHANNEL_PASSWORD_CHANGED = "notifychannelpasswordchanged"
    CHANNEL_MOVED = "notifychannelmoved"
    CHANNEL_DELETED = "notifychanneldeleted"
    CLIENT_ENTER = "notifycliententerview"
    CLIENT_LEFT = "notifyclientleftview"
    CLIENT_MOVED = "notifyclientmoved"
    TEXT_MESSAGE = "notifytextmessage"
    # Client Query Only ??
    TALK_STATUS_CHANGE = "notifytalkstatuschange"
    MESSAGE = "notifymessage"
    MESSAGE_LIST = "notifymessagelist"
    COMPLAIN_LIST = "notifycomplainlist"
    BAN_LIST = "notifybanlist"
    CLIENT_LEFT_VIEW = "notifyclientleftview"
    CLIENT_ENTER_VIEW = "notifycliententerview"
    CLIENT_POKE = "notifyclientpoke"
    CLIENT_CHAT_CLOSED = "notifyclientchatclosed"
    CLIENT_CHAT_COMPOSING = "notifyclientchatcomposing"
    CLIENT_UPDATED = "notifyclientupdated"
    CLIENT_IDS = "notifyclientids"
    CLIENT_DBID_FROM_UID = "notifyclientdbidfromuid"
    CLIENT_NAME_FROM_UID = "notifyclientnamefromuid"
    CLIENT_NAME_FROM_DBID = "notifyclientnamefromdbid"
    CLIENT_UID_FROM_CLID = "notifyclientuidfromclid"
    CONNECTION_INFO = "notifyconnectioninfo"
    SERVER_UPDATED = "notifyserverupdated"
    CHANNEL_LIST = "channellist"
    CHANNEL_LIST_FINISHED = "channellistfinished"
    CURRENT_SERVER_CONNECTION_CHANGED = "notifycurrentserverconnectionchanged"
    CONNECT_STATUS_CHANGE = "notifyconnectstatuschange"


class BaseResponse(object):
    """
    Base response object
    """
    __metaclass__ = abc.ABCMeta

    # Unescape Map. Order is important.
    _UNESCAPE_MAP = [
        ("\v", r"\v"),  # Vertical Tab
        ("\t", r"\t"),  # Horizontal Tab
        ("\r", r"\r"),  # Cariiage Return
        ("\n", r"\n"),  # Newline
        ("\f", r"\f"),  # Form Feed
        ("\b", r"\b"),  # Backspace
        ("\a", r"\a"),  # Bell
        ("|", r"\p"),  # |
        (" ", r"\s"),  # Space
        ("/", r"\/"),  # /
        ("\\", r"\\")  # \
    ]

    def __init__(self, raw, query=None):
        """
        Constructor

        :type raw: list
        :param raw: Raw data for parsing, list of lines
        :type query: :class:`tslib.request.Request`
        :param query: Request object
        """
        self._data = None
        self._error = None
        self._raw = raw
        self._query = query

        self._parse()

    @abc.abstractmethod
    def _parse(self):
        pass

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error

    @property
    def raw(self):
        return self.raw

    @property
    def query(self):
        return self._query

    def __getitem__(self, index):
        if self.data is not None:
            return self.data[index]
        return None

    def __len__(self):
        if self.data is not None:
            return len(self.data)
        return 0

    def __iter__(self):
        if self.data is not None:
            return iter(self.data)
        return iter(list())

    @staticmethod
    def unescape(raw):
        """
        Converts the escaped string

        :type raw: str
        :param raw: Escaped string

        :rtype: str
        :return: Converted string

        :raises TypeError: If string not provided
        """
        if isinstance(raw, str):
            # Order is important
            for needle, escaped_needle in BaseResponse._UNESCAPE_MAP:
                raw = raw.replace(escaped_needle, needle)
            return raw
        else:
            raise TypeError("Parameter *raw* must be a string")

    @staticmethod
    def parse_pair(raw):
        """
        Parses the pair from a string

        key=value
           ^ default (and only) separator

        Examples
        Input: parse_pair("key=value")
        Output: ('key', 'value')
        Input: parse_pair("singlekey")
        Output: ('singlekey', None)

        :type raw: str
        :param raw: String with key=value pair

        :rtype: tuple
        :return: Parsed pair (key, val)
        """
        if isinstance(raw, str):
            pair = raw.split("=", 1)
            if len(pair) == 1:
                key = pair[0]
                val = None
            else:
                key, val = pair
                # key does not need parsing
                val = BaseResponse.unescape(val)
            return key, val
        else:
            raise TypeError("Parameter *raw* must be a string")

    @staticmethod
    def parse_list(raw):
        """
        Parses the list of pairs from a string

        key=value key=value key=value ...
                 ^ default (and only) separator

        :type raw: str
        :param raw: String with list

        :rtype: dict
        :return: Parsed list

        :raises TypeError: If string not provided
        """
        if isinstance(raw, str):
            return OrderedDict(
                [BaseResponse.parse_pair(pair) for pair in raw.split()])
        else:
            raise TypeError("Parameter *raw* must be a string")

    @staticmethod
    def parse_set(raw):
        """
        Parses the set of lists of pairs from a string

        key=value key=value key=value|key=value ...|key=value ...
                                     ^ default (and only) separator

        :type raw: str
        :param raw: String with set

        :rtype: list
        :return: Parsed set

        :raises TypeError: If string not provided
        """
        if isinstance(raw, str):
            return [BaseResponse.parse_list(group) for group in raw.split("|")]
        else:
            raise TypeError("Parameter *raw* must be a string")


class Response(BaseResponse):
    """
    Request response
    """

    def _parse(self):
        if len(self._raw) == 2:
            self._data = self.parse_set(self._raw[0])
            if len(self._data) == 1:
                self._data = self._data[0]
            self._error = self.parse_list(self._raw[1].split(" ", 1)[1])
        else:
            self._error = self.parse_list(self._raw[0].split(" ", 1)[1])


class Event(BaseResponse):
    """
    Event response
    """

    def __init__(self, raw, query=None):
        self._type = None
        super(Event, self).__init__(raw, query)

    @property
    def type(self):
        return self._type

    def _parse(self):
        for member in EventType.__members__.values():
            if self.raw.startswith(member.value):
                self._type = member
                break
        else:
            raise UnknownEventTypeError(self)

        self._data = self.parse_set(self.raw.split(maxsplit=1)[1])
        if len(self._data) == 1:
            self._data = self._data[0]
