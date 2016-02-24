#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.server.

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
from enum import Enum
from tslib.connection import Interface
from tslib.exception import MissedParameterError
from tslib.request import EnumRequest as Request

logger = logging.getLogger(__name__)

"""
Enumerations
"""


class Command(Enum):
    HELP = "help"
    QUIT = "quit"
    LOGIN = "login"
    LOGOUT = "logout"
    VERSION = "version"
    HOST_INFO = "hostinfo"
    INSTANCE_INFO = "instanceinfo"
    INSTANCE_EDIT = "instanceedit"
    BINDING_LIST = "bindinglist"
    USE = "use"
    SERVER_LIST = "serverlist"
    SERVER_ID_GET_BY_PORT = "serveridgetbyport"
    SERVER_DELETE = "serverdelete"
    SERVER_CREATE = "servercreate"
    SERVER_START = "serverstart"
    SERVER_STOP = "serverstop"
    SERVER_PROCESS_STOP = "serverprocessstop"
    SERVER_INFO = "serverinfo"
    SERVER_REQUEST_CONNECTION_INFO = "serverrequestconnectioninfo"
    SERVER_TEMP_PASSWORD_ADD = "servertemppasswordadd"
    SERVER_TEMP_PASSWORD_DEL = "servertemppassworddel"
    SERVER_TEMP_PASSWORD_LIST = "servertemppasswordlist"
    SERVER_EDIT = "serveredit"
    SERVER_GROUP_LIST = "servergrouplist"
    SERVER_GROUP_ADD = "servergroupadd"
    SERVER_GROUP_DEL = "servergroupdel"
    SERVER_GROUP_COPY = "servergroupcopy"
    SERVER_GROUP_RENAME = "servergrouprename"
    SERVER_GROUP_PERM_LIST = "servergrouppermlist"
    SERVER_GROUP_ADD_PERM = "servergroupaddperm"
    SERVER_GROUP_DEL_PERM = "servergroupdelperm"
    SERVER_GROUP_ADD_CLIENT = "servergroupaddclient"
    SERVER_GROUP_DEL_CLIENT = "servergroupdelclient"
    SERVER_GROUP_CLIENT_LIST = "servergroupclientlist"
    SERVER_GROUPS_BY_CLIENT_ID = "servergroupsbyclientid"
    SERVER_GROUP_AUTO_ADD_PERM = "servergroupautoaddperm"
    SERVER_GROUP_AUTO_DEL_PERM = "servergroupautodelperm"
    SERVER_SNAPSHOT_CREATE = "serversnapshotcreate"
    SERVER_SNAPSHOT_DEPLOY = "serversnapshotdeploy"
    SERVER_NOTIFY_REGISTER = "servernotifyregister"
    SERVER_NOTIFY_UNREGISTER = "servernotifyunregister"
    SEND_TEXT_MESSAGE = "sendtextmessage"
    LOG_VIEW = "logview"
    LOG_ADD = "logadd"
    GM = "gm"
    CHANNEL_LIST = "channellist"
    CHANNEL_INFO = "channelinfo"
    CHANNEL_FIND = "channelfind"
    CHANNEL_MOVE = "channelmove"
    CHANNEL_CREATE = "channelcreate"
    CHANNEL_DELETE = "channeldelete"
    CHANNEL_EDIT = "channeledit"
    CHANNEL_GROUP_LIST = "channelgrouplist"
    CHANNEL_GROUP_ADD = "channelgroupadd"
    CHANNEL_GROUP_DEL = "channelgroupdel"
    CHANNEL_GROUP_COPY = "channelgroupcopy"
    CHANNEL_GROUP_RENAME = "channelgrouprename"
    CHANNEL_GROUP_ADD_PERM = "channelgroupaddperm"
    CHANNEL_GROUP_PERM_LIST = "channelgrouppermlist"
    CHANNEL_GROUP_DEL_PERM = "channelgroupdelperm"
    CHANNEL_GROUP_CLIENT_LIST = "channelgroupclientlist"
    SET_CLIENT_CHANNEL_GROUP = "setclientchannelgroup"
    CHANNEL_PERM_LIST = "channelpermlist"
    CHANNEL_ADD_PERM = "channeladdperm"
    CHANNEL_DEL_PERM = "channeldelperm"
    CLIENT_LIST = "clientlist"
    CLIENT_INFO = "clientinfo"
    CLIENT_FIND = "clientfind"
    CLIENT_EDIT = "clientedit"
    CLIENT_DB_LIST = "clientdblist"
    CLIENT_DB_INFO = "clientdbinfo"
    CLIENT_DB_FIND = "clientdbfind"
    CLIENT_DB_EDIT = "clientdbedit"
    CLIENT_DB_DELETE = "clientdbdelete"
    CLIENT_GET_IDS = "clientgetids"
    CLIENT_GET_DB_ID_FROM_UID = "clientgetdbidfromuid"
    CLIENT_GET_NAME_FROM_UID = "clientgetnamefromuid"
    CLIENT_GET_NAME_FROM_DB_ID = "clientgetnamefromdbid"
    CLIENT_SET_SERVER_QUERY_LOGIN = "clientsetserverquerylogin"
    CLIENT_UPDATE = "clientupdate"
    CLIENT_MOVE = "clientmove"
    CLIENT_KICK = "clientkick"
    CLIENT_POKE = "clientpoke"
    CLIENT_PERM_LIST = "clientpermlist"
    CLIENT_ADD_PERM = "clientaddperm"
    CLIENT_DEL_PERM = "clientdelperm"
    CHANNEL_CLIENT_PERM_LIST = "channelclientpermlist"
    CHANNEL_CLIENT_ADD_PERM = "channelclientaddperm"
    CHANNEL_CLIENT_DEL_PERM = "channelclientdelperm"
    PERMISSION_LIST = "permissionlist"
    PERM_ID_GET_BY_NAME = "permidgetbyname"
    PERM_OVERVIEW = "permoverview"
    PERM_GET = "permget"
    PERM_FIND = "permfind"
    PERM_RESET = "permreset"
    PRIVILEGE_KEY_LIST = "privilegekeylist"
    PRIVILEGE_KEY_ADD = "privilegekeyadd"
    PRIVILEGE_KEY_DELETE = "privilegekeydelete"
    PRIVILEGE_KEY_USE = "privilegekeyuse"
    MESSAGE_LIST = "messagelist"
    MESSAGE_ADD = "messageadd"
    MESSAGE_DEL = "messagedel"
    MESSAGE_GET = "messageget"
    MESSAGE_UPDATE_FLAG = "messageupdateflag"
    COMPLAIN_LIST = "complainlist"
    COMPLAIN_ADD = "complainadd"
    COMPLAIN_DEL_ALL = "complaindelall"
    COMPLAIN_DEL = "complaindel"
    BAN_CLIENT = "banclient"
    BAN_LIST = "banlist"
    BAN_ADD = "banadd"
    BAN_DEL = "bandel"
    BAN_DEL_ALL = "bandelall"
    FT_INIT_UPLOAD = "ftinitupload"
    FT_INIT_DOWNLOAD = "ftinitdownload"
    FT_LIST = "ftlist"
    FT_GET_FILE_LIST = "ftgetfilelist"
    FT_GET_FILE_INFO = "ftgetfileinfo"
    FT_STOP = "ftstop"
    FT_DELETE_FILE = "ftdeletefile"
    FT_CREATE_DIR = "ftcreatedir"
    FT_RENAME_FILE = "ftrenamefile"
    CUSTOM_SEARCH = "customsearch"
    CUSTOM_INFO = "custominfo"
    WHO_AM_I = "whoami"
    # Aliases
    INSTANCEINFO = "instanceinfo"
    INSTANCEEDIT = "instanceedit"
    BINDINGLIST = "bindinglist"
    SERVERLIST = "serverlist"
    SERVERIDGETBYPORT = "serveridgetbyport"
    SERVERDELETE = "serverdelete"
    SERVERCREATE = "servercreate"
    SERVERSTART = "serverstart"
    SERVERSTOP = "serverstop"
    SERVERPROCESSSTOP = "serverprocessstop"
    SERVERINFO = "serverinfo"
    SERVERREQUESTCONNECTIONINFO = "serverrequestconnectioninfo"
    SERVERTEMPPASSWORDADD = "servertemppasswordadd"
    SERVERTEMPPASSWORDDEL = "servertemppassworddel"
    SERVERTEMPPASSWORDLIST = "servertemppasswordlist"
    SERVEREDIT = "serveredit"
    SERVERGROUPLIST = "servergrouplist"
    SERVERGROUPADD = "servergroupadd"
    SERVERGROUPDEL = "servergroupdel"
    SERVERGROUPCOPY = "servergroupcopy"
    SERVERGROUPRENAME = "servergrouprename"
    SERVERGROUPPERMLIST = "servergrouppermlist"
    SERVERGROUPADDPERM = "servergroupaddperm"
    SERVERGROUPDELPERM = "servergroupdelperm"
    SERVERGROUPADDCLIENT = "servergroupaddclient"
    SERVERGROUPDELCLIENT = "servergroupdelclient"
    SERVERGROUPCLIENTLIST = "servergroupclientlist"
    SERVERGROUPSBYCLIENTID = "servergroupsbyclientid"
    SERVERGROUPAUTOADDPERM = "servergroupautoaddperm"
    SERVERGROUPAUTODELPERM = "servergroupautodelperm"
    SERVERSNAPSHOTCREATE = "serversnapshotcreate"
    SERVERSNAPSHOTDEPLOY = "serversnapshotdeploy"
    SERVERNOTIFYREGISTER = "servernotifyregister"
    SERVERNOTIFYUNREGISTER = "servernotifyunregister"
    SENDTEXTMESSAGE = "sendtextmessage"
    LOGVIEW = "logview"
    LOGADD = "logadd"
    CHANNELLIST = "channellist"
    CHANNELINFO = "channelinfo"
    CHANNELFIND = "channelfind"
    CHANNELMOVE = "channelmove"
    CHANNELCREATE = "channelcreate"
    CHANNELDELETE = "channeldelete"
    CHANNELEDIT = "channeledit"
    CHANNELGROUPLIST = "channelgrouplist"
    CHANNELGROUPADD = "channelgroupadd"
    CHANNELGROUPDEL = "channelgroupdel"
    CHANNELGROUPCOPY = "channelgroupcopy"
    CHANNELGROUPRENAME = "channelgrouprename"
    CHANNELGROUPADDPERM = "channelgroupaddperm"
    CHANNELGROUPPERMLIST = "channelgrouppermlist"
    CHANNELGROUPDELPERM = "channelgroupdelperm"
    CHANNELGROUPCLIENTLIST = "channelgroupclientlist"
    SETCLIENTCHANNELGROUP = "setclientchannelgroup"
    CHANNELPERMLIST = "channelpermlist"
    CHANNELADDPERM = "channeladdperm"
    CHANNELDELPERM = "channeldelperm"
    CLIENTLIST = "clientlist"
    CLIENTINFO = "clientinfo"
    CLIENTFIND = "clientfind"
    CLIENTEDIT = "clientedit"
    CLIENTDBLIST = "clientdblist"
    CLIENTDBINFO = "clientdbinfo"
    CLIENTDBFIND = "clientdbfind"
    CLIENTDBEDIT = "clientdbedit"
    CLIENTDBDELETE = "clientdbdelete"
    CLIENTGETIDS = "clientgetids"
    CLIENTGETDBIDFROMUID = "clientgetdbidfromuid"
    CLIENTGETNAMEFROMUID = "clientgetnamefromuid"
    CLIENTGETNAMEFROMDBID = "clientgetnamefromdbid"
    CLIENTSETSERVERQUERYLOGIN = "clientsetserverquerylogin"
    CLIENTUPDATE = "clientupdate"
    CLIENTMOVE = "clientmove"
    CLIENTKICK = "clientkick"
    CLIENTPOKE = "clientpoke"
    CLIENTPERMLIST = "clientpermlist"
    CLIENTADDPERM = "clientaddperm"
    CLIENTDELPERM = "clientdelperm"
    CHANNELCLIENTPERMLIST = "channelclientpermlist"
    CHANNELCLIENTADDPERM = "channelclientaddperm"
    CHANNELCLIENTDELPERM = "channelclientdelperm"
    PERMISSIONLIST = "permissionlist"
    PERMIDGETBYNAME = "permidgetbyname"
    PERMOVERVIEW = "permoverview"
    PERMGET = "permget"
    PERMFIND = "permfind"
    PERMRESET = "permreset"
    PRIVILEGEKEYLIST = "privilegekeylist"
    PRIVILEGEKEYADD = "privilegekeyadd"
    PRIVILEGEKEYDELETE = "privilegekeydelete"
    PRIVILEGEKEYUSE = "privilegekeyuse"
    MESSAGELIST = "messagelist"
    MESSAGEADD = "messageadd"
    MESSAGEDEL = "messagedel"
    MESSAGEGET = "messageget"
    MESSAGEUPDATEFLAG = "messageupdateflag"
    COMPLAINLIST = "complainlist"
    COMPLAINADD = "complainadd"
    COMPLAINDELALL = "complaindelall"
    COMPLAINDEL = "complaindel"
    BANCLIENT = "banclient"
    BANLIST = "banlist"
    BANADD = "banadd"
    BANDEL = "bandel"
    BANDELALL = "bandelall"
    FTINITUPLOAD = "ftinitupload"
    FTINITDOWNLOAD = "ftinitdownload"
    FTLIST = "ftlist"
    FTGETFILELIST = "ftgetfilelist"
    FTGETFILEINFO = "ftgetfileinfo"
    FTSTOP = "ftstop"
    FTDELETEFILE = "ftdeletefile"
    FTCREATEDIR = "ftcreatedir"
    FTRENAMEFILE = "ftrenamefile"
    CUSTOMSEARCH = "customsearch"
    CUSTOMINFO = "custominfo"
    WHOAMI = "whoami"


class GroupType(Enum):
    CHANNEL_GUEST = 10
    SERVER_GUEST = 15
    QUERY_GUEST = 20
    CHANNEL_VOICE = 25
    SERVER_NORMAL = 30
    CHANNEL_OPERATOR = 35
    CHANNEL_ADMIN = 40
    SERVER_ADMIN = 45
    QUERY_ADMIN = 50


class EventType(Enum):
    SERVER = "server"
    CHANNEL = "channel"
    TEXT_SERVER = "textserver"
    TEXT_CHANNEL = "textchannel"
    TEXT_PRIVATE = "textprivate"
    ANY = "any"
    # Aliases
    TEXTSERVER = "textserver"
    TEXTCHANNEl = "textchannel"
    TEXTPRIVATE = "textprivate"


class HostMessageMode(Enum):
    LOG = 1  # 1: display message in chatlog
    MODAL = 2  # 2: display message in modal dialog
    MODAL_QUIT = 3  # 3: display message in modal dialog and close connection
    # Aliases
    MODALQUIT = 3  # 3: display message in modal dialog and close connection


class HostBannerMode(Enum):
    NO_ADJUST = 0  # 0: do not adjust
    IGNORE_ASPECT = 1  # 1: adjust but ignore aspect ratio (like TeamSpeak 2)
    KEEP_ASPECT = 2  # 2: adjust and keep aspect ratio
    # Aliases
    NOADJUST = 0  # 0: do not adjust
    IGNOREASPECT = 1  # 1: adjust but ignore aspect ratio (like TeamSpeak 2)
    KEEPASPECT = 2  # 2: adjust and keep aspect ratio


class Codec(Enum):
    SPEEX_NARROWBAND = 0  # 0: speex narrowband (mono, 16bit, 8kHz)
    SPEEX_WIDEBAND = 1  # 1: speex wideband (mono, 16bit, 16kHz)
    SPEEX_ULTRAWIDEBAND = 2  # 2: speex ultra-wideband (mono, 16bit, 32kHz)
    CELT_MONO = 3  # 3: celt mono (mono, 16bit, 48kHz)


class CodecEncryptionMode(Enum):
    CRYPT_INDIVIDUAL = 0  # 0: configure per channel
    CRYPT_DISABLED = 1  # 1: globally disabled
    CRYPT_ENABLED = 2  # 2: globally enabled


class TextMessageTargetMode(Enum):
    CLIENT = 1  # 1: target is a client
    CHANNEL = 2  # 2: target is a channel
    SERVER = 3  # 3: target is a virtual server


class LogLevel(Enum):
    ERROR = 1  # 1: everything that is really bad
    WARNING = 2  # 2: everything that might be bad
    DEBUG = 3  # 3: output that might help find a problem
    INFO = 4  # 4: informational output


class ReasonIdentifier(Enum):
    REASON_KICK_CHANNEL = 4  # 4: kick client from channel
    REASON_KICK_SERVER = 5  # 5: kick client from server


class PermissionGroupDatabaseTypes(Enum):
    TEMPLATE = 0  # 0: template group (used for new virtual servers)
    REGULAR = 1  # 1: regular group (used for regular clients)
    QUERY = 2  # 2: global query group (used for ServerQuery clients)


class PermissionGroupTypes(Enum):
    SERVER_GROUP = 0  # 0: server group permission
    GLOBAL_CLIENT = 1  # 1: client specific permission
    CHANNEL = 2  # 2: channel specific permission
    CHANNEL_GROUP = 3  # 3: channel group permission
    CHANNEL_CLIENT = 4  # 4: channel-client specific permission


class TokenType(Enum):
    SERVER_GROUP = 0  # 0: server group token (id1={groupID} id2=0)
    CHANNEL_GROUP = 1  # 1: channel group token (id1={groupID} id2={channelID})


"""
Interface
"""


class Server(Interface):
    """
    TeamSpeak 3 ServerQuery Connection Interface
    """

    def __init__(self, host, port=10011, timeout=None):
        self._RECV_DAEMON_START_REQUIRED = [
            Command.SERVER_NOTIFY_REGISTER,
            Command.SERVERNOTIFYREGISTER
        ]
        super().__init__(host, port, timeout)

    def send(self, request):
        if request.enum_command in self._RECV_DAEMON_START_REQUIRED:
            self.start_recv_thread()
        return super().send(request)

    def help(self, command=None):
        """
        Provides information about ServerQuery commands. Used without
        parameters, help lists and briefly describes every command.

        :type command: str
        :param command: Command

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if command:
            if isinstance(command, Command):
                return self.send(Request(Command.HELP)
                                 .add_parameter(None, command.value))
            else:
                return self.send(Request(Command.HELP)
                                 .add_parameter(None, command))
        return self.send(Request(Command.HELP))

    def quit(self):
        """
        Closes the ServerQuery connection to the TeamSpeak 3 Server instance.

        :rtype: None
        :return:
        """
        self.close()

    def login(self, client_login_name, client_login_password):
        """
        Authenticates with the TeamSpeak 3 Server instance using given
        ServerQuery login credentials.

        :type client_login_name: str
        :param client_login_name: Username
        :type client_login_password: str
        :param client_login_password: Password

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.LOGIN)
                         .add_parameter("client_login_name", client_login_name)
                         .add_parameter("client_login_password",
                                        client_login_password))

    def logout(self):
        """
        Deselects the active virtual server and logs out from the server
        instance.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.LOGOUT))

    def version(self):
        """
        Displays the servers version information including platform and build
        number.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.VERSION))

    def host_info(self):
        """
        Displays detailed connection information about the server instance
        including uptime, number of virtual servers online, traffic information,
        etc.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.HOST_INFO))

    def instance_info(self):
        """
        Displays the server instance configuration including database revision
        number, the file transfer port, default group IDs, etc.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.INSTANCE_INFO))

    def instance_edit(self, **instance_properties):
        """
        Changes the server instance configuration using given properties.

        Available properties:
        - serverinstance_guest_serverquery_group
        - serverinstance_template_serveradmin_group
        - serverinstance_filetransfer_port
        - serverinstance_max_download_total_bandwitdh
        - serverinstance_max_upload_total_bandwitdh
        - serverinstance_template_serverdefault_group
        - serverinstance_template_channeldefault_group
        - serverinstance_template_channeladmin_group
        - serverinstance_serverquery_flood_commands
        - serverinstance_serverquery_flood_time
        - serverinstance_serverquery_flood_ban_time

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.INSTANCE_EDIT)
                         .add_parameters(**instance_properties))

    def binding_list(self):
        """
        Displays a list of IP addresses used by the server instance on
        multi-homed machines.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.BINDING_LIST))

    def use(self, sid=None, port=None, virtual=False):
        """
        Selects the virtual server specified with *sid* or *port* to allow
        further interaction. The ServerQuery client will appear on the virtual
        server and acts like a real TeamSpeak 3 Client, except it's unable to
        send or receive voice data.
        If your database contains multiple virtual servers using the same UDP
        port, use will select a random virtual server using the specified port.

        :type sid: int
        :param sid: Server ID
        :type port: int
        :param port: Server port
        :type virtual: bool
        :param virtual:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if sid:
            return self.send(Request(Command.USE)
                             .add_parameter("sid", sid)
                             .add_option("virtual", virtual))
        return self.send(Request(Command.USE)
                         .add_parameter("port", port)
                         .add_option("virtual", virtual))

    def server_list(self, uid=False, short=False, all=False,
                    only_offline=False):
        """
        Displays a list of virtual servers including their ID, status, number of
        clients online, etc. If you're using the *-all* option, the server will
        list all virtual servers stored in the database. This can be useful when
        multiple server instances with different machine IDs are using the same
        database. The machine ID is used to identify the server instance a
        virtual server is associated with.
        The status of a virtual server can be either online, offline, deploy
        running, booting up, shutting down and virtual online. While most of
        them are self-explanatory, virtual online is a bit more complicated.
        Please note that whenever you select a virtual server which is currently
        stopped, it will be started in virtual mode which means you are able to
        change its configuration, create channels or change permissions, but no
        regular TeamSpeak 3 Client can connect. As soon as the last ServerQuery
        client deselects the virtual server, its status will be changed back to
        offline.

        :type uid: bool
        :param uid:
        :type short: bool
        :param short:
        :type all: bool
        :param all:
        :type only_offline: bool
        :param only_offline:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_LIST)
                         .add_option("uid", uid)
                         .add_option("short", short)
                         .add_option("all", all)
                         .add_option("onlyoffline", only_offline))

    def server_id_get_by_port(self, virtualserver_port):
        """
        Displays the database ID of the virtual server running on the UDP port
        specified by *virtualserver_port*.

        :type virtualserver_port: int
        :param virtualserver_port: Server port

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_ID_GET_BY_PORT)
                         .add_parameter("virtualserver_port",
                                        virtualserver_port))

    def server_delete(self, sid):
        """
        Deletes the virtual server specified with *sid*. Please note that only
        virtual servers in stopped state can be deleted.

        :type sid: int
        :param sid: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_DELETE)
                         .add_parameter("sid", sid))

    def server_create(self, virtualserver_name, **virtualserver_properties):
        """
        Creates a new virtual server using the given properties and displays its
        ID, port and initial administrator privilege key. If
        *virtualserver_port* is not specified, the server will test for the
        first unused UDP port.
        The first virtual server will be running on UDP port 9987 by default.
        Subsequently started virtual servers will be running on increasing UDP
        port numbers.

        :type virtualserver_name: str
        :param virtualserver_name: Server name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_CREATE)
                         .add_parameter("virtualserver_name",
                                        virtualserver_name)
                         .add_parameters(**virtualserver_properties))

    def server_start(self, sid):
        """
        Starts the virtual server specified with *sid*. Depending on your
        permissions, you're able to start either your own virtual server only or
        all virtual servers in the server instance.

        :type sid: int
        :param sid: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_START)
                         .add_parameter("sid", sid))

    def server_stop(self, sid):
        """
        Stops the virtual server specified with *sid*. Depending on your
        permissions, you're able to stop either your own virtual server only or
        all virtual servers in the server instance.

        :type sid: int
        :param sid: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_STOP)
                         .add_parameter("sid", sid))

    def server_process_stop(self):
        """
        Stops the entire TeamSpeak 3 Server instance by shutting down the
        process.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_PROCESS_STOP))

    def server_info(self):
        """
        Displays detailed configuration information about the selected virtual
        server including unique ID, number of clients online, configuration,
        etc.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_INFO))

    def server_request_connection_info(self):
        """
        Displays detailed connection information about the selected virtual
        server including uptime, traffic information, etc.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_REQUEST_CONNECTION_INFO))

    def server_temp_password_add(self, pw, desc, duration, tcid=0, tcpw=""):
        """
        Sets a new temporary server password specified with *pw*. The temporary
        password will be valid for the number of seconds specified with
        duration. The client connecting with this password will automatically
        join the channel specified with *tcid*. If *tcid* is set to 0, the
        client will join the default channel.

        :type pw: str
        :param pw: Password
        :type desc: str
        :param desc: Description
        :type duration: int
        :param duration: Seconds
        :type tcid: int
        :param tcid: Channel ID
        :type tcpw: str
        :param tcpw: Channel password

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_ADD)
                         .add_parameter("pw", pw)
                         .add_parameter("desc", desc)
                         .add_parameter("duration", duration)
                         .add_parameter("tcid", tcid)
                         .add_parameter("tcpw", tcpw))

    def server_temp_password_del(self, pw):
        """
        Deletes the temporary server password specified with *pw*.

        :type pw: str
        :param pw: Password

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_DEL)
                         .add_parameter("pw", pw))

    def server_temp_password_list(self):
        """
        Returns a list of active temporary server passwords. The output
        contains the clear-text password, the nickname and unique identifier of
        the creating client.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_LIST))

    def server_edit(self, **virtualserver_properties):
        """
        Changes the selected virtual servers configuration using given
        properties. Note that this command accepts multiple properties which
        means that you're able to change all settings of the selected virtual
        server at once.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        # TODO: Проверка на существующие свойства
        return self.send(Request(Command.SERVER_EDIT)
                         .add_parameters(**virtualserver_properties))

    def server_group_list(self):
        """
        Displays a list of server groups available. Depending on your
        permissions, the output may also contain global ServerQuery groups and
        template groups.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_LIST))

    def server_group_add(self, name, type=None):
        """
        Creates a new server group using the name specified with *name* and
        displays its ID. The optional *type* parameter can be used to create
        ServerQuery groups and template groups.

        :type name: str
        :param name: Group name
        :type type: int|:class:`tslib.server.PermissionGroupDatabaseTypes`
        :param type: Group DB type

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_ADD)
                         .add_parameter("name", name)
                         .add_parameter("type", type))

    def server_group_del(self, sgid, force=False):
        """
        Deletes the server group specified with *sgid*. If *force* is set to 1,
        the server group will be deleted even if there are clients within.

        :type sgid: int
        :param sgid: Group ID
        :type force: bool
        :param force:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL)
                         .add_parameter("sgid", sgid)
                         .add_parameter("force", force))

    def server_group_copy(self, ssgid, tsgid, name, type):
        """
        Creates a copy of the server group specified with *ssgid*. If *tsgid*
        is set to 0, the server will create a new group.
        To overwrite an existing group, simply set *tsgid* to the ID of a
        designated target group. If a target group is set, the *name* parameter
        will be ignored.

        :type ssgid: int
        :param ssgid: Source group ID
        :type tsgid: int
        :param tsgid: Target group ID
        :type name: str
        :param name: Group name
        :type type: int|:class:`tslib.server.PermissionGroupDatabaseTypes`
        :param type: Group DB type

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_COPY)
                         .add_parameter("ssgid", ssgid)
                         .add_parameter("tsgid", tsgid)
                         .add_parameter("name", name)
                         .add_parameter("type", type))

    def server_group_rename(self, sgid, name):
        """
        Changes the name of the server group specified with *sgid*.

        :type sgid: int
        :param sgid: Group ID
        :type name: str
        :param name: Group name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_RENAME)
                         .add_parameter("sgid", sgid)
                         .add_parameter("name", name))

    def server_group_perm_list(self, sgid, permsid=False):
        """
        Displays a list of permissions assigned to the server group specified
        with *sgid*. If the *–permsid* option is specified, the output will
        contain the permission names instead of the internal IDs.

        :type sgid: int
        :param sgid: Group ID
        :type permsid: bool
        :param permsid:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_PERM_LIST)
                         .add_parameter("sgid", sgid)
                         .add_option("permsid", permsid))

    def server_group_add_perm(self, sgid, permissions_set):
        """
        Adds a set of specified permissions to the server group specified with
        *sgid*. Multiple permissions can be added by providing the four
        parameters of each permission. A permission can be specified by
        *permid* or *permsid*.

        :type sgid: int
        :param sgid: Group ID
        :type permissions_set: dict
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_ADD_PERM)
                         .add_parameter("sgid", sgid)
                         .add_list_of_parameters(permissions_set))

    def server_group_del_perm(self, sgid, permissions_set):
        """
        Removes a set of specified permissions from the server group specified
        with *sgid*. Multiple permissions can be removed at once. A permission
        can be specified by *permid* or *permsid*.

        :type sgid: int
        :param sgid: Group ID
        :type permissions_set: dict
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL_PERM)
                         .add_parameter("sgid", sgid)
                         .add_list_of_parameters(permissions_set))

    def server_group_add_client(self, sgid, cldbid):
        """
        Adds a client to the server group specified with *sgid*. Please note
        that a client cannot be added to default groups or template groups.

        :type sgid: int
        :param sgid: Group ID
        :type cldbid: int
        :param cldbid: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_ADD_CLIENT)
                         .add_parameter("sgid", sgid)
                         .add_parameter("cldbid", cldbid))

    def server_group_del_client(self, sgid, cldbid):
        """
        Removes a client specified with *cldbid* from the server group
        specified with *sgid*.

        :type sgid: int
        :param sgid: Group ID
        :type cldbid: int
        :param cldbid: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL_CLIENT)
                         .add_parameter("sgid", sgid)
                         .add_parameter("cldbid", cldbid))

    def server_group_client_list(self, sgid, names=False):
        """
        Displays the IDs of all clients currently residing in the server group
        specified with *sgid*. If you're using the optional *-names* option, the
        output will also contain the last known nickname and the unique
        identifier of the clients.

        :type sgid: int
        :param sgid: Group ID
        :type names: bool
        :param names:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_CLIENT_LIST)
                         .add_parameter("sgid", sgid)
                         .add_option("names", names))

    def server_groups_by_client_id(self, cldbid):
        """
        Displays all server groups the client specified with *cldbid* is
        currently residing in.

        :type cldbid: int
        :param cldbid: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUPS_BY_CLIENT_ID)
                         .add_parameter("cldbid", cldbid))

    def server_group_auto_add_perm(self, sgtype, permvalue, permnegated=False,
                                   permskip=False, permid=None, permsid=None):
        """
        Adds a set of specified permissions to *ALL* regular server groups on
        all virtual servers. The target groups will be identified by the value
        of their *i_group_auto_update_type* permission specified with *sgtype*.
        Multiple permissions can be added at once. A permission can be
        specified by *permid* or *permsid*. The known values for *sgtype* are:
        10: Channel Guest
        15: Server Guest
        20: Query Guest
        25: Channel Voice
        30: Server Normal
        35: Channel Operator
        40: Channel Admin
        45: Server Admin
        50: Query Admin

        :type sgtype: int|:class:`tslib.server.GroupType`
        :param sgtype: Group type
        :type permid_or_permsid: int|str
        :param permid_or_permsid: Permission ID or name
        :type permid: int
        :param permid: Permission ID
        :type permsid: str
        :param permsid: Permission name
        :type permvalue: str|int|bool
        :param permvalue: Permission value
        :type permnegated: bool
        :param permnegated:
        :type permskip: bool
        :param permskip:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if permid is None and permsid is None:
            return MissedParameterError(
                "*permid* or *permsid* must be specified")

        if permid:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", sgtype)
                             .add_parameter("permid", permid)
                             .add_parameter("permvalue", permvalue)
                             .add_parameter("permnegated", permnegated)
                             .add_parameter("permsip", permskip))
        else:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", sgtype)
                             .add_parameter("permsid", permsid)
                             .add_parameter("permvalue", permvalue)
                             .add_parameter("permnegated", permnegated)
                             .add_parameter("permsip", permskip))

    def server_group_auto_del_perm(self, sgtype, permid=None, permsid=None):
        """
        Removes a set of specified permissions from *ALL* regular server groups
        on all virtual servers. The target groups will be identified by the
        value of their *i_group_auto_update_type permission* specified with
        *sgtype*. Multiple permissions can be removed at once. A permission can
        be specified by *permid* or *permsid*. The known values for *sgtype*
        are:
        10: Channel Guest
        15: Server Guest
        20: Query Guest
        25: Channel Voice
        30: Server Normal
        35: Channel Operator
        40: Channel Admin
        45: Server Admin
        50: Query Admin

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if permid is None and permsid is None:
            return MissedParameterError(
                "*permid* or *permsid* must be specified")

        if permid:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", sgtype)
                             .add_parameter("permid", permid))
        else:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", sgtype)
                             .add_parameter("permsid", permsid))

    def server_snapshot_create(self):
        """
        Displays a snapshot of the selected virtual server containing all
        settings, groups and known client identities.
        The data from a server snapshot can be used to restore a virtual
        servers configuration, channels and permissions using the
        *serversnapshotdeploy* command.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_SNAPSHOT_CREATE))

    # TODO: Check, how it's should work, and then rewrite function
    def server_snapshot_deploy(self, virtualserver_snapshot, mapping=False):
        """
        Restores the selected virtual servers configuration using the data from
        a previously created server snapshot.
        Please note that the TeamSpeak 3 Server does NOT check for necessary
        permissions while deploying a snapshot so the command could be abused
        to gain additional privileges.

        :type virtualserver_snapshot: str
        :param virtualserver_snapshot:
        :type mapping: bol
        :param mapping:
        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_SNAPSHOT_DEPLOY)
                         .add_parameter(None, virtualserver_snapshot)
                         .add_option("mapping", mapping))

    def server_notify_register(self, event, id=None):
        """
        Registers for a specified category of events on a virtual server to
        receive notification messages. Depending on the notifications you've
        registered for, the server will send you a message on every event in
        the view of your ServerQuery client (e.g. clients joining your channel,
        incoming text messages, server configuration changes, etc). The event
        source is declared by the *event* parameter while id can be used to
        limit the notifications to a specific channel.

        :type event: :class:`tslib.server.Server.EventType`
        :param event: Event type
        :type id: int
        :param id: Channel ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if not isinstance(event, EventType):
            raise TypeError(
                "*event* parameter must be EventType object's value")

        q = Request(Command.SERVER_NOTIFY_REGISTER).add_parameter("event",
                                                                  event)

        if event == EventType.CHANNEL or event == EventType.TEXT_CHANNEL:
            if not id:
                raise MissedParameterError
            q.add_parameter("id", id)

        return self.send(q)

    def server_notify_unregister(self):
        """
        Unregisters all events previously registered with servernotifyregister
        so you will no longer receive notification messages.

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_NOTIFY_UNREGISTER))

    def send_text_message(self, target_mode, target, msg):
        """
        Sends a text message to a specified target. If *targetmode* is set to
        1, a message is sent to the client with the ID specified by *target*.
        If *targetmode* is set to 2 or 3, the *target* parameter will be
        ignored and a message is sent to the current channel or server
        respectively.

        :type target_mode: int|:class:`tslib.server.TextMessageTargetMode`
        :param target_mode: Target mode
        :type target: int
        :param target: Client ID
        :type msg: str
        :param msg: Text
        :return:
        """
        return self.send(Request(Command.SEND_TEXT_MESSAGE)
                         .add_parameter("targetmode", target_mode)
                         .add_parameter("target", target)
                         .add_parameter("msg", msg))

    # TODO: Implement functionality
    def log_view(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def log_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def gm(self):
        raise NotImplementedError

    def channel_list(self, topic=False, flags=False, voice=False, limits=False,
                     icon=False):
        """
        Displays a list of channels created on a virtual server including their
        ID, order, name, etc. The output can be modified using several command
        options.

        :type topic: bool
        :param topic:
        :type flags: bool
        :param flags:
        :type voice: bool
        :param voice:
        :type limits: bool
        :param limits:
        :type icon: bool
        :param icon:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_LIST)
                         .add_option("topic", topic)
                         .add_option("flags", flags)
                         .add_option("voice", voice)
                         .add_option("limits", limits)
                         .add_option("icon", icon))

    def channel_info(self, cid):
        """
        Displays detailed configuration information about a channel including
        ID, topic, description, etc

        :type cid: int
        :param cid:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_INFO)
                         .add_parameter("cid", cid))

    # TODO: Implement functionality
    def channel_find(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_move(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_create(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_delete(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_edit(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_del(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_copy(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_rename(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_add_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_perm_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_del_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_group_client_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def set_client_channel_group(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_perm_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_add_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_del_perm(self):
        raise NotImplementedError

    def client_list(self, uid=False, away=False, voice=False, times=False,
                    groups=False, info=False, icon=False, country=False):
        """
        Displays a list of clients online on a virtual server including their
        ID, nickname, status flags, etc. The output can be modified using
        several command options.
        Please note that the output will only contain clients which are
        currently in channels you're able to subscribe to.

        :type uid: bool
        :param uid:
        :type away: bool
        :param away:
        :type voice: bool
        :param voice:
        :type times: bool
        :param times:
        :type groups: bool
        :param groups:
        :type info: bool
        :param info:
        :type icon: bool
        :param icon:
        :type country: bool
        :param country:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_LIST)
                         .add_option("uid", uid)
                         .add_option("away", away)
                         .add_option("voice", voice)
                         .add_option("times", times)
                         .add_option("groups", groups)
                         .add_option("info", info)
                         .add_option("icon", icon)
                         .add_option("country", country))

    def client_info(self, clid):
        """
        Displays detailed configuration information about a client including
        unique ID, nickname, client version, etc

        :type clid: int
        :param clid:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_INFO)
                         .add_parameter("clid", clid))

    # TODO: Implement functionality    # TODO
    def client_find(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_edit(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_db_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_db_info(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_db_find(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_db_edit(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_db_delete(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_get_ids(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_get_db_id_from_uid(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_get_name_from_uid(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_get_name_from_db_id(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_set_server_query_login(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_update(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_move(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_kick(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_poke(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_perm_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_add_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def client_del_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_client_perm_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_client_add_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def channel_client_del_perm(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def permission_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def perm_id_get_by_name(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def perm_overview(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def perm_get(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def perm_find(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def perm_reset(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def privilege_key_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def privilege_key_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def privilege_key_delete(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def privilege_key_use(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def message_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def message_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def message_del(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def message_get(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def message_update_flag(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def complain_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def complain_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def complain_del_all(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def complain_del(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ban_client(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ban_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ban_add(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ban_del(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ban_del_all(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_init_upload(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_init_download(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_get_file_list(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_get_file_info(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_stop(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_delete_file(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_create_dir(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def ft_rename_file(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def custom_search(self):
        raise NotImplementedError

    # TODO: Implement functionality
    def custom_info(self):
        raise NotImplementedError

    def who_am_i(self):
        """
        Displays information about your current ServerQuery connection
        including your loginname, etc

        :rtype: :class:`tslib.response.Response`
        :return: Request object
        """
        return self.send(Request(Command.WHO_AM_I))

    # """
    # Aliases
    # """

    def hostinfo(self):
        return self.host_info()

    def instanceinfo(self):
        return self.instance_info()

    def instanceedit(self, **instance_properties):
        return self.instance_edit(**instance_properties)

    def bindinglist(self):
        return self.binding_list()

    def serverlist(self, uid=False, short=False, all=False, onlyoffline=False):
        return self.server_list(uid, short, all, onlyoffline)

    def serveridgetbyport(self, virtualserver_port):
        return self.server_id_get_by_port(virtualserver_port)

    def serverdelete(self, sid):
        return self.server_delete(sid)

    # def servercreate(virtualserver_name, **virtualserver_properties):
    #     return server_create(virtualserver_name,
    #                          **virtualserver_properties)
    #
    # def serverstart(sid):
    #     return server_start(sid)
    #
    # def serverstop(sid):
    #     return server_stop(sid)
    #
    # def serverprocessstop():
    #     return server_process_stop()
    #
    # def serverinfo():
    #     return server_info()
    #
    # def serverrequestconnectioninfo():
    #     return server_request_connection_info()
    #
    # def serveredit(**virtualserver_properties):
    #     return server_edit(**virtualserver_properties)
    #
    # def servergrouplist():
    #     return server_group_list()
    #
    # def servergroupadd(name, type=None):
    #     return server_group_add(name, type)
    #
    # def servergroupdel(sgid, force=False):
    #     return server_group_del(sgid, force)
    #
    # def servergroupcopy(ssgid, tsgid, name, type):
    #     return server_group_copy(ssgid, tsgid, name, type)
    #
    # def servergrouprename(sgid, name):
    #     return server_group_rename(sgid, name)
    #
    # def servergrouppermlist(sgid, permsid=False):
    #     return server_group_perm_list(sgid, permsid)
    #
    # def servergroupaddclient(sgid, cldbid):
    #     return server_group_add_client(sgid, cldbid)
    #
    # def servergroupdelclient(sgid, cldbid):
    #     return server_group_del_client(sgid, cldbid)
    #
    # def servergroupclientlist(sgid, names=False):
    #     return server_group_client_list(sgid, names)
    #
    # def servergroupsbyclientid(cldbid):
    #     return server_groups_by_client_id(cldbid)
    #
    # def serversnapshotcreate():
    #     return server_snapshot_create()
    #
    # def serversnapshotdeploy(virtualserver_snapshot):
    #     return server_snapshot_deploy(virtualserver_snapshot)
    #
    # def servernotifyregister(event, id=None):
    #     return server_notify_register(event, id)
    #
    # def servernotifyunregister():
    #     return server_notify_unregister()
    #
    # # TODO
    # # sendtextmessage
    # # logview
    # # logadd
    # # gm
    #
    # def channellist(topic=False, flags=False, voice=False, limits=False,
    #                 icon=False):
    #     return channel_list(topic, flags, voice, limits, icon)
    #
    # def channelinfo(cid):
    #     return channel_info(cid)
    #
    # TODO
    # channelfind
    # channelmove
    # channelcreate
    # channeldelete
    # channeledit
    # channelgrouplist
    # channelgroupadd
    # channelgroupdel
    # channelgroupcopy
    # channelgrouprename
    # channelgroupaddperm
    # channelgrouppermlist
    # channelgroupdelperm
    # channelgroupclientlist
    # setclientchannelgroup
    # channelpermlist
    # channeladdperm
    # channeldelperm
    #
    # def clientlist(uid=False, away=False, voice=False, times=False,
    #                groups=False, info=False, icon=False, country=False):
    #     return client_list(uid, away, voice, times, groups, info, icon,
    #                        country)
    #
    # def clientinfo(clid):
    #     return client_info(clid)
    #
    # TODO
    # clientfind
    # clientedit
    # clientdblist
    # clientdbinfo
    # clientdbfind
    # clientdbedit
    # clientdbdelete
    # clientgetids
    # clientgetdbidfromuid
    # clientgetnamefromuid
    # clientgetnamefromdbid
    # clientsetserverquerylogin
    # clientupdate
    # clientmove
    # clientkick
    # clientpoke
    # clientpermlist
    # clientaddperm
    # channeldelperm
    # channelclientpermlist
    # channelclientaddperm
    # channelclientdelperm
    # permissionlist
    # permidgetbyname
    # permoverview
    # permget
    # permfind
    # permreset
    # privilegekeylist
    # privilegekeyadd
    # privilegekeydelete
    # privilegekeyuse
    # messagelist
    # messageadd
    # messagedel
    # messageget
    # messageupdateflag
    # complainlist
    # complainadd
    # complaindelall
    # complaindel
    # banclient
    # banlist
    # banadd
    # bandel
    # bandelall
    # ftinitupload
    # ftinitdownload
    # ftlist
    # ftgetfilelist
    # ftgetfileinfo
    # ftstop
    # ftdeletefile
    # ftcreatedir
    # ftrenamefile
    # customsearch
    # custominfo

    def whoami(self):
        return self.who_am_i()
