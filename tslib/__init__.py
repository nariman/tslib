#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.

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

__version__ = "0.1.0"

import logging
from tslib.client import Client
from tslib.connection import Connection, Interface
from tslib.request import Request
from tslib.response import Response, Event
from tslib.server import Server

logging.basicConfig(format="%(filename)s:%(lineno)d # %(levelname)s "
                           "[%(asctime)s] %(message)s",
                    level=logging.DEBUG)
