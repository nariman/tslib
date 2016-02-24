#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.connection.

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

import sys
import logging
import threading
import time
from telnetlib import Telnet

from tslib.exception import ResponseExpectedError, UnexpectedLineError
from tslib.request import Request
from tslib.response import Event, Response

if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue
    from tslib.exception import ConnectionError

logger = logging.getLogger(__name__)
event_cls = threading.Event if sys.version_info >= (3, 0) else threading._Event


class Connection:
    """
    Connection class for TeamSpeak 3 servers/clients
    """
    __metaclass__ = type
    
    CONNECTION_TIMEOUT = 1
    KEEP_ALIVE_INTERVAL = 300

    """
    Main class methods
    """

    def __init__(self, host, port, timeout=None):
        """
        Constructor.

        :type host: str
        :param host: Domain or IP-address of TeamSpeak 3 server/client
        :type port: int
        :param port: Port (QueryPort) of TeamSpeak 3 server/client
        :type timeout: int
        :param timeout: Timeout on socket operations
        """
        self._host = host  # if host is not None else "localhost"
        self._port = port
        self._timeout = self.CONNECTION_TIMEOUT
        self._telnet = None
        self._keep_alive_thread = None
        self._keep_alive_interval = None
        self._keep_alive_stop_signal = None
        self._telnet_lock = threading.Lock()

        if timeout and timeout > 0:
            self._timeout = timeout

        self.open()

    def __del__(self):
        """
        Destructor.
        """
        self.close()

    def __str__(self):
        if self._telnet is not None:
            return "TeamSpeak 3 connection (established) - " \
                   "{0}:{1}".format(self._host, self._port)
        else:
            if self._host is not None:
                return "TeamSpeak 3 connection (not established) - " \
                       "{0}:{1}".format(self._host, self._port)
            else:
                return "TeamSpeak 3 connection (not established)"

    """
    Connection methods
    """

    def is_connected(self):
        """
        :rtype: bool
        :return: True, if connected, otherwise False
        """
        return self._telnet is not None

    def open(self, host=None, port=None, timeout=None):
        """
        Connect to the TeamSpeak 3 server/client.

        :type host: str
        :param host: Domain or IP-address of TeamSpeak 3 server/client
        :type port: int
        :param port: Port (QueryPort) of TeamSpeak 3 server/client
        :type timeout: int
        :param timeout: Timeout on socket operations

        :rtype: bool
        :return: True, if connection is successfully established

        :raises TimeoutError: If connections is not established
        :raises ConnectionError: If server/client address is not provided
        :raises ConnectionError: If it's not a TeamSpeak 3 server/client
        """
        if not self.is_connected():
            if host is None and self._host is None:
                raise ConnectionError("*Host* parameter is not provided")

            if host:
                self._host = host
            if port:
                self._port = port
            if timeout and timeout > 0:
                self._timeout = timeout

            self._telnet = Telnet(self._host, self._port, self._timeout)

            tmp = self._telnet.read_until(b"\n\r")
            if not tmp.startswith(b"TS3"):
                self._telnet.close()
                self._telnet = None
                raise ConnectionError("It's not a TeamSpeak 3 server/client")
            self._telnet.read_until(b"\n\r")

            logger.info("Connection is established - {0}:{1}".format(
                self._host, self._port))
        return True

    def close(self):
        """
        Закрывает соединение с сервером, предварительно отсылая команду
        ``quit`` TeamSpeak 3 серверу.

        :rtype: bool
        :return: True, если соединение с сервером было успешно закрыто
        """
        if self.is_connected():
            self.stop_keep_alive()
            with self._telnet_lock:
                self._telnet.write(b"quit\n\r")
                self._telnet.close()
                self._telnet = None
            logger.info("Connection is closed - {0}:{1}".format(self._host,
                                                                self._port))
        return True

    def _reset(self):
        """
        Принудительно очищает соединение. Необходим для случаев, когда
        удаленный сервер закрыл соединение, в результате чего текущий объект
        соединения становится бесполезным.

        :rtype: bool
        :return: True, если соединение было очищено
        """
        if self.is_connected():
            self.stop_keep_alive()
            self._telnet.close()
            self._telnet = None
            logger.info("Connection reset - {0}:{1}".format(self._host,
                                                            self._port))
        return True

    """
    Keep-Alive methods
    """

    def __keep_alive(self):
        stop_signal = self._keep_alive_stop_signal

        while not stop_signal.is_set():
            self.send("")
            logger.debug("Keep-Alive Beacon sent ({0} sec. interval) - "
                         "{1}:{2}".format(self._keep_alive_interval,
                                          self._host,
                                          self._port))
            time.sleep(self._keep_alive_interval)

    def start_keep_alive(self, interval=None):
        """
        Активирует таймер посылки каждые *interval* секунд сигнала
        Keep-Alive Beacon для поддержания соединения активным.

        :type interval: int
        :param interval: Интервал между каждой посылкой, в секундах

        :rtype: bool
        :return: True, если таймер успешно активирован
        """
        if not self.is_connected():
            return False

        if self._keep_alive_thread and self._keep_alive_interval == interval:
            return
        self.stop_keep_alive()
        self._keep_alive_interval = self.KEEP_ALIVE_INTERVAL
        self._keep_alive_stop_signal = threading.Event()

        if interval:
            self._keep_alive_interval = max(1, interval)

        self._keep_alive_thread = threading.Thread(
            target=self.__keep_alive, name="TeamSpeak 3 Beacon Sender Thread")
        self._keep_alive_thread.start()
        logger.info("Keep-Alive Beacon Sender with interval {0} sec. started - "
                    "{1}:{2}".format(self._keep_alive_interval, self._host,
                                     self._port))
        return True

    def stop_keep_alive(self):
        """
        Деактивирует таймер посылки сигналов Keep-Alive Beacon, если он был
        активирован ранее.

        :rtype: bool
        :return: False, если таймер даже не был активирован, иначе True
        """
        if self._keep_alive_thread:
            self._keep_alive_stop_signal.set()
            self._keep_alive_stop_signal = None
            self._keep_alive_thread = None
            logger.info(
                "Keep-Alive Beacon Sender with interval {0} sec. stopped - "
                "{1}:{2}".format(self._keep_alive_interval, self._host,
                                 self._port))
        return True

    """
    I/O methods
    """

    def send(self, data):
        """
        Отправляет *data* на сервер TeamSpeak 3. Не рекомендуется использовать
        данный метод напрямую без необходимости, т.к. экранирование данных в
        этом методе не производится.

        :type data: str
        :param data: Данные для отправки

        :raises TypeError: Если данные не являются строкой
        """
        if not isinstance(data, str):
            raise TypeError("*data* must be a string")

        with self._telnet_lock:
            if not self.is_connected():
                raise ConnectionError(
                    "Connection is already closed / not established yet")
            try:
                self._telnet.write(data.encode() + b"\n\r")
            except Exception:
                self._reset()
                raise

    # TODO: check all todos
    def recv(self):
        """
        Получает данные с сервера (строка).

        :rtype: str
        :return: Response string
        """
        if not self.is_connected():
            raise ConnectionError(
                "Connection is already closed / not established yet")
        try:
            # TODO: А если вернет не строку, будет ошибка метода `decode`...
            return self._telnet.read_until(b"\n\r").decode().rstrip()
        except Exception:
            self._reset()
            raise


class Interface:
    """
    TeamSpeak 3 Request Connection Interface
    """
    __metaclass__ = type
    
    RECV_DAEMON_INTERVAL = 0.1

    class Request(event_cls):
        def __init__(self, request):
            super(Interface.Request, self).__init__()
            self.request = request
            self.response = None

    """
    Main class methods
    """

    def __init__(self, host, port, timeout=None):
        """
        Constructor

        :type host: str
        :param host: Domain or IP-address of TeamSpeak 3 server/client
        :type port: int
        :param port: Port (QueryPort) of TeamSpeak 3 server/client
        :type timeout: int
        :param timeout: Timeout between connection attempts
        """
        self._conn = Connection(host, port, timeout)
        self._conn_lock = threading.Lock()
        self._queue = Queue()
        self._recv_thread = None
        self._recv_thread_stop_signal = None
        self._handlers = []

    def __enter__(self):
        if not self.is_connected():
            self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()

    """
    Connection manipulation methods
    """

    def is_connected(self):
        """
        :rtype: bool
        :return: True, if connected, otherwise False
        """
        return self._conn.is_connected()

    def open(self):
        """
        Open the connection

        :raises TimeoutError: If connections is not established
        :raises ConnectionError: If server/client address is not provided
        :raises ConnectionError: If it's not a TeamSpeak 3 server/client
        """
        return self._conn.open()

    def close(self):
        """
        Close the connection

        :rtype: bool
        :return: True, если соединение с сервером было успешно закрыто
        """
        self.stop_recv_thread()
        self._conn.close()
        return True

    """
    Methods for working with handlers
    """

    def register_handler(self, handler, *args, **kwargs):
        self._handlers.append((handler, args, kwargs))

    def unregister_handler(self, handler, *args, **kwargs):
        self._handlers.remove((handler, args, kwargs))

    def _event_handlers(self, event):
        def _():
            for handler, args, kwargs in self._handlers:
                handler(event=event, *args, **kwargs)

        threading.Thread(target=_).start()

    """
    Keep-Alive Methods
    """

    def start_keep_alive(self, interval=None):
        """
        Start sending Keep-Alive Beacons

        :type interval: int
        :param interval: Interval within sendings, in seconds
        :rtype: bool
        :return:
        """
        return self._conn.start_keep_alive(interval)

    def stop_keep_alive(self):
        """
        Stop sending Keep-Alive Beacons

        :rtype: bool
        :return:
        """
        return self._conn.stop_keep_alive()

    """
    I/O methods
    """

    def send(self, request):
        """
        Send request to the server

        :type request: :class:`tslib.request.Request`
        :param request:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if isinstance(request, Request):
            request = Interface.Request(request)
            if self._recv_thread and not self._recv_thread_stop_signal.is_set():
                self._queue.put(request)
                request.wait()
                return request.response
            else:
                # For order implementation
                with self._conn_lock:
                    self._queue.put(request)
                    self._recv()
                    return request.response
        else:
            raise TypeError("Parameter *request* must be Request object")

    def _recv(self):
        if not self._queue.empty():
            request = self._queue.get()
            lines = list()

            self._conn.send(request.request.request_string)

            while not request.is_set():
                # Read line
                line = self._conn.recv()

                # Nothing... we expected a data
                if not line:
                    request.set()
                    raise ResponseExpectedError
                # Notify
                elif line.startswith("notify"):
                    self._event_handlers(Event(line))
                    lines = list()
                # Status line
                elif line.startswith("error"):
                    lines.append(line)
                    request.response = Response(lines)
                    request.set()
                # Something from data body
                else:
                    lines.append(line)
        else:
            # Read line
            line = self._conn.recv()

            # Nothing... All correct
            if not line:
                return False
            # Notify
            elif line.startswith("notify"):
                self._event_handlers(Event(line))
            # Something unexpected data...
            else:
                raise UnexpectedLineError

        return True

    def __recv(self):
        stop_signal = self._recv_thread_stop_signal

        while not stop_signal.is_set():
            if not self._recv():
                time.sleep(self.RECV_DAEMON_INTERVAL)

    def start_recv_thread(self):
        """
        Активирует фоновое получение данных с сервера.

        :rtype: bool
        :return:
        """
        if self._recv_thread:
            return True

        self._recv_thread_stop_signal = threading.Event()
        self._recv_thread = threading.Thread(target=self.__recv(),
                                             name="TeamSpeak 3 Receiver Thread")
        self._recv_thread.start()

        logger.info("Receiver Thread started ({1})".format(self._conn))
        return True

    def stop_recv_thread(self):
        """
        Деактивирует фоновое получение данных с сервера.

        :rtype: bool
        :return:
        """
        if self._recv_thread:
            self._recv_thread_stop_signal.set()
            self._recv_thread.join()
            self._recv_thread_stop_signal = None
            self._recv_thread = None
            logger.info("Receiver Thread stopped ({1})".format(self._conn))
        return True
