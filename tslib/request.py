#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Server/Client Query Python Interface
tslib.request.

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

import logging
from collections import OrderedDict
from enum import Enum

logger = logging.getLogger(__name__)


class Request:
    """
    Request object
    """
    __metaclass__ = type

    # Escape Map. Order is important.
    _ESCAPE_MAP = [
        ("\\", r"\\"),  # \
        ("/", r"\/"),  # /
        (" ", r"\s"),  # Space
        ("|", r"\p"),  # |
        ("\a", r"\a"),  # Bell
        ("\b", r"\b"),  # Backspace
        ("\f", r"\f"),  # Form Feed
        ("\n", r"\n"),  # Newline
        ("\r", r"\r"),  # Carriage Return
        ("\t", r"\t"),  # Horizontal Tab
        ("\v", r"\v")  # Vertical Tab
    ]

    def __init__(self, command):
        """
        Constructor

        :type command: str
        :param command: Request command
        """
        self._command = command
        self._parameters = OrderedDict()
        self._list_of_parameters = list()
        self._options = list()
        self._request_string = None
        self._is_request_string_actual = False

    @property
    def request_string(self):
        """
        :rtype: str
        :return: Escaped string with provided data
        """
        if not self._is_request_string_actual:
            self._build_request_string()
        return self._request_string

    def add_parameter(self, key, val):
        """
        :type key: str|int|bool|Enum|None
        :param key:
        :type val: str|int|bool|Enum|None
        :param key:

        :rtype: :class:`tslib.request.Request`
        :return: Updated request object
        """
        if val is None:
            return self

        key = key.value if isinstance(key, Enum) else key
        val = val.value if isinstance(val, Enum) else val

        if not key:
            self._parameters.update({val: None})
        else:
            self._parameters.update({key: val})

        self._is_request_string_actual = False
        return self

    def add_parameters(self, **pairs):
        """
        :rtype: :class:`tslib.request.Request`
        :return: Updated request object
        """
        self._parameters.update(pairs)
        self._is_request_string_actual = False
        return self

    def add_list_of_parameters(self, data):
        """
        :type data: list of dicts|dict
        :param data:

        :rtype: :class:`tslib.request.Request`
        :return: Updated request object
        """
        if data is dict:
            self._list_of_parameters.append(data)
        else:
            self._list_of_parameters.extend(data)
        self._is_request_string_actual = False
        return self

    def add_option(self, option, val=True):
        """
        :type option: str
        :param option:
        :type val: bool
        :param val: If False, option will not be added

        :rtype: :class:`tslib.request.Request`
        :return: Updated request object
        """
        if val:
            self._options.append(option)
            self._is_request_string_actual = False
        return self

    def _build_request_string(self):
        """
        Generates request string with provided data

        :rtype: None
        :return: None
        """
        self._request_string = self._command

        if self._parameters:
            self._request_string = "{0} {1}".format(
                self._request_string, self.escape_dict(self._parameters))

        if self._list_of_parameters:
            self._request_string = "{0} {1}".format(
                self._request_string, self.escape_set(self._list_of_parameters))

        if self._options:
            self._request_string = "{0} {1}".format(
                self._request_string, self.escape_options(self._options))

        self._is_request_string_actual = True

    @staticmethod
    def escape(data):
        """
        Escapes data to the string

        :type data: None, bool, int, str
        :param data: Source data

        :rtype: str
        :return: Escaped data, string

        :raises TypeError: If data is of unsupported type
        """
        if not data:
            return str()
        elif isinstance(data, bool):
            return "1" if data else "0"
        elif isinstance(data, int):
            return str(data)
        elif isinstance(data, str):
            # Order is important
            for needle, escaped_needle in Request._ESCAPE_MAP:
                data = data.replace(needle, escaped_needle)
            return data
        else:
            raise TypeError(
                "Parameter *data* can be empty or only a bool/int/string")

    @staticmethod
    def escape_pair(data):
        """
        Converts a pair to the string representation

        :type data: tuple|list|dict
        :param data: Pair with key and value

        :rtype: str
        :return: Converted pair
        """
        # Key does not need to be escaped
        return "{0}={1}".format(data[0], Request.escape(data[1]))

    @staticmethod
    def escape_dict(data):
        """
        Escapes data (dictionary) to the string of pairs (key=val) (parameters
        list)

        :type data: dict|OrderedDict
        :param data: Dictionary

        :rtype: str
        :return: Escaped data, string

        :raises TypeError: If data is of unsupported type
        """
        if not data:
            return str()

        if isinstance(data, dict) or isinstance(data, OrderedDict):
            tmp = list()
            for key, val in data.items():
                if not key:
                    tmp.append(Request.escape(val))
                elif not val:
                    tmp.append(Request.escape(key))
                else:
                    # tmp.append(Request.escape_pair((key, val)))
                    tmp.append(
                        "{0}={1}".format(key.lower(), Request.escape(val)))
            return " ".join(tmp)
        else:
            raise TypeError(
                "Parameter *data* can be empty or only a dict/OrderedDict")

    @staticmethod
    def escape_set(data):
        """
        Escapes data (list of dictionaries) to the string with set of lists of
        pairs (key=val) (set of lists of parameters)

        :type data: list
        :param data: List of dictionaries

        :rtype: str
        :return: Escaped data, string

        :raises TypeError: If data is of unsupported type
        """
        if not data:
            return str()

        if isinstance(data, list):
            return "|".join(Request.escape_dict(group) for group in data)
        else:
            raise TypeError("Parameter *data* can be empty or only a list")

    @staticmethod
    def escape_options(data):
        """
        Prefixes flags with ``-`` symbol, if necessary

        :type data: list
        :param data: List with flags

        :rtype: str
        :return: List with flags
        """
        if not data:
            return str()

        tmp = list()
        for param in data:
            if param is None:
                continue
            elif not param.startswith("-"):
                param = "-" + param
            tmp.append(param)

        return " ".join(tmp)


class EnumRequest(Request):
    def __init__(self, command):
        self._enum_command = command
        super(EnumRequest, self).__init__(command.value)

    @property
    def enum_command(self):
        return self._enum_command
