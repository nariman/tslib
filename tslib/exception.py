#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.exception.

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

logger = logging.getLogger(__name__)


class TSLibException(Exception):
    """
    Base exception for package
    """
    pass


class ResponseExpectedError(TSLibException):
    """
    Исключение для случаев, когда мы не смогли дождаться ответа от сервера на
    наш запрос. Т.к. он может неожиданно прийти между началом обработки
    следующего запроса, и создать коллизию ответов от сервера, то вместо
    поддержания соединения будет создано исключение, а соединение разорвано.
    """
    pass


class UnexpectedLineError(TSLibException):
    """
    Исключение для случаев, когда мы не смогли дождаться ответа от сервера на
    наш запрос. Т.к. он может неожиданно прийти между началом обработки
    следующего запроса, и создать коллизию ответов от сервера, то вместо
    поддержания соединения будет создано исключение, а соединение разорвано.
    """
    pass


class RequestException(TSLibException):
    """
    Base exception for requests
    """
    def __init__(self, request=None):
        self._request = request

    @property
    def request(self):
        return self._request


class MissedParameterError(RequestException):
    pass


class ResponseException(TSLibException):
    """
    Base exception for responses
    """

    def __init__(self, response=None):
        self._response = response

    @property
    def response(self):
        return self._response


class UnknownEventTypeError(ResponseException):
    """
    Исключение для случаев, когда тип события не определен. В идеале, такой
    ошибки быть не должно, мы должны знать все типы событий. Если что-то
    упустили - время делать Pull Request.
    """

    def __init__(self, response):
        super().__init__(response)
