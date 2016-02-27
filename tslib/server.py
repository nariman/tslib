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


class HostMessageMode(Enum):
    LOG = 1  # 1: display message in chatlog
    MODAL = 2  # 2: display message in modal dialog
    MODAL_QUIT = 3  # 3: display message in modal dialog and close connection


class HostBannerMode(Enum):
    NO_ADJUST = 0  # 0: do not adjust
    IGNORE_ASPECT = 1  # 1: adjust but ignore aspect ratio (like TeamSpeak 2)
    KEEP_ASPECT = 2  # 2: adjust and keep aspect ratio


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
            Command.SERVER_NOTIFY_REGISTER
        ]
        super(Server, self).__init__(host, port, timeout)

    def send(self, request):
        if request.enum_command in self._RECV_DAEMON_START_REQUIRED:
            self.start_recv_thread()
        return super(Server, self).send(request)

    def help(self, command=None):
        """
        Provides information about ServerQuery commands. Used without
        parameters, help lists and briefly describes every command.

        ServerQuery method: help [{command}]

        :type command: str
        :param command: Command

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if command:
            return self.send(Request(Command.HELP)
                             .add_parameter(None, command))
        return self.send(Request(Command.HELP))

    def quit(self):
        """
        Closes the ServerQuery connection to the TeamSpeak 3 Server instance.

        ServerQuery method: quit

        :rtype: None
        :return:
        """
        self.close()

    def login(self, client_login_name, client_login_password):
        """
        Authenticates with the TeamSpeak 3 Server instance using given
        ServerQuery login credentials.

        ServerQuery method: login client_login_name={username}
        client_login_password={password}
        ServerQuery method: login {username} {password}

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

        ServerQuery method: logout

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.LOGOUT))

    def version(self):
        """
        Displays the servers version information including platform and build
        number.

        ServerQuery method: version

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.VERSION))

    def host_info(self):
        """
        Displays detailed connection information about the server instance
        including uptime, number of virtual servers online, traffic information,
        etc.

        ServerQuery method: hostinfo

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.HOST_INFO))

    def instance_info(self):
        """
        Displays the server instance configuration including database revision
        number, the file transfer port, default group IDs, etc.

        ServerQuery method: instanceinfo

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.INSTANCE_INFO))

    def instance_edit(self, **properties):
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

        ServerQuery method: instanceedit [instance_properties…]

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.INSTANCE_EDIT)
                         .add_parameters(**properties))

    def binding_list(self):
        """
        Displays a list of IP addresses used by the server instance on
        multi-homed machines.

        ServerQuery method: bindinglist

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.BINDING_LIST))

    def use(self, id=None, port=None, virtual=False):
        """
        Selects the virtual server specified with *id* or *port* to allow
        further interaction. The ServerQuery client will appear on the virtual
        server and acts like a real TeamSpeak 3 Client, except it's unable to
        send or receive voice data.
        If your database contains multiple virtual servers using the same UDP
        port, use will select a random virtual server using the specified port.

        ServerQuery method: use [sid={serverID}] [port={serverPort}] [-virtual]
        ServerQuery method: use {serverID} [-virtual]

        :type id: int
        :param id: Server ID
        :type port: int
        :param port: Server port
        :type virtual: bool
        :param virtual:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if id:
            return self.send(Request(Command.USE)
                             .add_parameter("sid", id)
                             .add_option("virtual", virtual))
        return self.send(Request(Command.USE)
                         .add_parameter("port", port)
                         .add_option("virtual", virtual))

    def server_list(self, unique_id=False, short=False, all=False,
                    only_offline=False):
        """
        Displays a list of virtual servers including their ID, status, number
        of clients online, etc. If you're using the *-all* option, the server
        will list all virtual servers stored in the database. This can be
        useful when multiple server instances with different machine IDs are
        using the same database. The machine ID is used to identify the server
        instance a virtual server is associated with.
        The status of a virtual server can be either online, offline, deploy
        running, booting up, shutting down and virtual online. While most of
        them are self-explanatory, virtual online is a bit more complicated.
        Please note that whenever you select a virtual server which is
        currently stopped, it will be started in virtual mode which means you
        are able to change its configuration, create channels or change
        permissions, but no regular TeamSpeak 3 Client can connect. As soon as
        the last ServerQuery client deselects the virtual server, its status
        will be changed back to offline.

        ServerQuery method: serverlist [-uid] [-short] [-all] [-onlyoffline]

        :type unique_id: bool
        :param unique_id:
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
                         .add_option("uid", unique_id)
                         .add_option("short", short)
                         .add_option("all", all)
                         .add_option("onlyoffline", only_offline))

    def server_id_get_by_port(self, port):
        """
        Displays the database ID of the virtual server running on the UDP port
        specified by *port*.

        ServerQuery method: serveridgetbyport virtualserver_port={serverPort}

        :type port: int
        :param port: Server port

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_ID_GET_BY_PORT)
                         .add_parameter("virtualserver_port",
                                        port))

    def server_delete(self, id):
        """
        Deletes the virtual server specified with *id*. Please note that only
        virtual servers in stopped state can be deleted.

        ServerQuery method: serverdelete sid={serverID}

        :type id: int
        :param id: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_DELETE)
                         .add_parameter("sid", id))

    def server_create(self, name, **properties):
        """
        Creates a new virtual server using the given properties and displays
        its ID, port and initial administrator privilege key. If
        *virtualserver_port* is not specified, the server will test for the
        first unused UDP port.
        The first virtual server will be running on UDP port 9987 by default.
        Subsequently started virtual servers will be running on increasing UDP
        port numbers.

        ServerQuery method: servercreate virtualserver_name={serverName}
        [virtualserver_properties…]

        :type name: str
        :param name: Server name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_CREATE)
                         .add_parameter("virtualserver_name",
                                        name)
                         .add_parameters(**properties))

    def server_start(self, id):
        """
        Starts the virtual server specified with *id*. Depending on your
        permissions, you're able to start either your own virtual server only
        or all virtual servers in the server instance.

        ServerQuery method: serverstart sid={serverID}

        :type id: int
        :param id: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_START)
                         .add_parameter("sid", id))

    def server_stop(self, id):
        """
        Stops the virtual server specified with *id*. Depending on your
        permissions, you're able to stop either your own virtual server only or
        all virtual servers in the server instance.

        ServerQuery method: serverstop sid={serverID}

        :type id: int
        :param id: Server ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_STOP)
                         .add_parameter("sid", id))

    def server_process_stop(self):
        """
        Stops the entire TeamSpeak 3 Server instance by shutting down the
        process.

        ServerQuery method: serverprocessstop

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_PROCESS_STOP))

    def server_info(self):
        """
        Displays detailed configuration information about the selected virtual
        server including unique ID, number of clients online, configuration,
        etc.

        ServerQuery method: serverinfo

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_INFO))

    def server_request_connection_info(self):
        """
        Displays detailed connection information about the selected virtual
        server including uptime, traffic information, etc.

        ServerQuery method: serverrequestconnectioninfo

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_REQUEST_CONNECTION_INFO))

    def server_temp_password_add(self, password, description, duration,
                                 channel_id=0, channel_password=""):
        """
        Sets a new temporary server password specified with *password*. The
        temporary password will be valid for the number of seconds specified
        with *duration*. The client connecting with this password will
        automatically join the channel specified with *channel_id*. If
        *channel_id* is set to 0, the client will join the default channel.

        ServerQuery method: servertemppasswordadd pw={password}
        desc={description} duration={seconds} tcid={channelID} tcpw={channelPW}

        :type password: str
        :param password: Password
        :type description: str
        :param description: Description
        :type duration: int
        :param duration: Seconds
        :type channel_id: int
        :param channel_id: Channel ID
        :type channel_password: str
        :param channel_password: Channel password

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_ADD)
                         .add_parameter("pw", password)
                         .add_parameter("desc", description)
                         .add_parameter("duration", duration)
                         .add_parameter("tcid", channel_id)
                         .add_parameter("tcpw", channel_password))

    def server_temp_password_del(self, password):
        """
        Deletes the temporary server password specified with *password*.

        ServerQuery method: servertemppassworddel pw={password}

        :type password: str
        :param password: Password

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_DEL)
                         .add_parameter("pw", password))

    def server_temp_password_list(self):
        """
        Returns a list of active temporary server passwords. The output
        contains the clear-text password, the nickname and unique identifier of
        the creating client.

        ServerQuery method: servertemppasswordlist

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_TEMP_PASSWORD_LIST))

    def server_edit(self, **properties):
        """
        Changes the selected virtual servers configuration using given
        properties. Note that this command accepts multiple properties which
        means that you're able to change all settings of the selected virtual
        server at once.

        ServerQuery method: serveredit [virtualserver_properties…]

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        # TODO: Check for the existence of properties
        return self.send(Request(Command.SERVER_EDIT)
                         .add_parameters(**properties))

    def server_group_list(self):
        """
        Displays a list of server groups available. Depending on your
        permissions, the output may also contain global ServerQuery groups and
        template groups.

        ServerQuery method: servergrouplist

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_LIST))

    def server_group_add(self, name, type=None):
        """
        Creates a new server group using the name specified with *name* and
        displays its ID. The optional *type* parameter can be used to create
        ServerQuery groups and template groups.

        ServerQuery method: servergroupadd name={groupName} [type={groupDbType}]

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

    def server_group_del(self, id, force=False):
        """
        Deletes the server group specified with *id*. If *force* is set to 1,
        the server group will be deleted even if there are clients within.

        ServerQuery method: servergroupdel sgid={groupID} force={1|0}

        :type id: int
        :param id: Group ID
        :type force: bool
        :param force:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL)
                         .add_parameter("sgid", id)
                         .add_parameter("force", force))

    def server_group_copy(self, source_id, target_id, name, type):
        """
        Creates a copy of the server group specified with *source_id*. If
        *target_id* is set to 0, the server will create a new group.
        To overwrite an existing group, simply set *target_id* to the ID of a
        designated target group. If a target group is set, the *name* parameter
        will be ignored.

        ServerQuery method: servergroupcopy ssgid={sourceGroupID}
        tsgid={targetGroupID} name={groupName} type={groupDbType}

        :type source_id: int
        :param source_id: Source group ID
        :type target_id: int
        :param target_id: Target group ID
        :type name: str
        :param name: Group name
        :type type: int|:class:`tslib.server.PermissionGroupDatabaseTypes`
        :param type: Group DB type

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_COPY)
                         .add_parameter("ssgid", source_id)
                         .add_parameter("tsgid", target_id)
                         .add_parameter("name", name)
                         .add_parameter("type", type))

    def server_group_rename(self, id, name):
        """
        Changes the name of the server group specified with *id*.

        ServerQuery method: servergrouprename sgid={groupID} name={groupName}

        :type id: int
        :param id: Group ID
        :type name: str
        :param name: Group name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_RENAME)
                         .add_parameter("sgid", id)
                         .add_parameter("name", name))

    def server_group_perm_list(self, id, permission_string_id=False):
        """
        Displays a list of permissions assigned to the server group specified
        with *id*. If the *-permission_string_id* option is specified, the
        output will contain the permission names instead of the internal
        IDs.

        ServerQuery method: servergrouppermlist sgid={groupID} [-permsid]

        :type id: int
        :param id: Group ID
        :type permission_string_id: bool
        :param permission_string_id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_PERM_LIST)
                         .add_parameter("sgid", id)
                         .add_option("permsid", permission_string_id))

    def server_group_add_perm(self, id, permissions_set):
        """
        Adds a set of specified permissions to the server group specified with
        *id*. Multiple permissions can be added by providing the four
        parameters of each permission. A permission can be specified by
        *permid* or *permsid*.

        ServerQuery method: servergroupaddperm sgid={groupID}
        [permid={permID}…] [permsid={permName}…] permvalue={permValue}…
        permnegated={1|0}… permskip={1|0}…

        :type id: int
        :param id: Group ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_ADD_PERM)
                         .add_parameter("sgid", id)
                         .add_list_of_parameters(permissions_set))

    def server_group_del_perm(self, id, permissions_set):
        """
        Removes a set of specified permissions from the server group specified
        with *id*. Multiple permissions can be removed at once. A permission
        can be specified by *permid* or *permsid*.

        ServerQuery method: servergroupdelperm sgid={groupID}
        [permid={permID}…] [permsid={permName}…]

        :type id: int
        :param id: Group ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL_PERM)
                         .add_parameter("sgid", id)
                         .add_list_of_parameters(permissions_set))

    def server_group_add_client(self, id, client_db_id):
        """
        Adds a client to the server group specified with *id*. Please note that
        a client cannot be added to default groups or template groups.

        ServerQuery method: servergroupaddclient sgid={groupID}
        cldbid={clientDBID}

        :type id: int
        :param id: Group ID
        :type client_db_id: int
        :param client_db_id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_ADD_CLIENT)
                         .add_parameter("sgid", id)
                         .add_parameter("cldbid", client_db_id))

    def server_group_del_client(self, id, client_db_id):
        """
        Removes a client specified with *client_db_id* from the server group
        specified with *id*.

        ServerQuery method: servergroupdelclient sgid={groupID}
        cldbid={clientDBID}

        :type id: int
        :param id: Group ID
        :type client_db_id: int
        :param client_db_id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_DEL_CLIENT)
                         .add_parameter("sgid", id)
                         .add_parameter("cldbid", client_db_id))

    def server_group_client_list(self, id, names=False):
        """
        Displays the IDs of all clients currently residing in the server group
        specified with *id*. If you're using the optional *-names* option, the
        output will also contain the last known nickname and the unique
        identifier of the clients.

        ServerQuery method: servergroupclientlist sgid={groupID} [-names]

        :type id: int
        :param id: Group ID
        :type names: bool
        :param names:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUP_CLIENT_LIST)
                         .add_parameter("sgid", id)
                         .add_option("names", names))

    def server_groups_by_client_id(self, client_db_id):
        """
        Displays all server groups the client specified with *client_db_id* is
        currently residing in.

        ServerQuery method: servergroupsbyclientid cldbid={clientDBID}

        :type client_db_id: int
        :param client_db_id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_GROUPS_BY_CLIENT_ID)
                         .add_parameter("cldbid", client_db_id))

    def server_group_auto_add_perm(self, type, permission_value,
                                   permission_negated=False,
                                   permission_skip=False, permission_id=None,
                                   permission_string_id=None):
        """
        Adds a set of specified permissions to *ALL* regular server groups on
        all virtual servers. The target groups will be identified by the value
        of their *i_group_auto_update_type* permission specified with
        *type*. Multiple permissions can be added at once. A permission can be
        specified by *permission_id* or *permission_string_id*. The known
        values for *type* are:
        10: Channel Guest
        15: Server Guest
        20: Query Guest
        25: Channel Voice
        30: Server Normal
        35: Channel Operator
        40: Channel Admin
        45: Server Admin
        50: Query Admin

        ServerQuery method: servergroupautoaddperm sgtype={groupID}
        [permid={permID}…] [permsid={permName}…] permvalue={permValue}…
        permnegated={1|0}… permskip={1|0}…

        :type type: int|:class:`tslib.server.GroupType`
        :param type: Group type
        :type permission_id: int
        :param permission_id: Permission ID
        :type permission_string_id: str
        :param permission_string_id: Permission name
        :type permission_value: str|int|bool
        :param permission_value: Permission value
        :type permission_negated: bool
        :param permission_negated:
        :type permission_skip: bool
        :param permission_skip:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if permission_id is None and permission_string_id is None:
            return MissedParameterError(
                "*permission_id* or *permission_string_id* must be specified")

        if permission_id:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", type)
                             .add_parameter("permid", permission_id)
                             .add_parameter("permvalue", permission_value)
                             .add_parameter("permnegated", permission_negated)
                             .add_parameter("permsip", permission_skip))
        else:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", type)
                             .add_parameter("permsid", permission_string_id)
                             .add_parameter("permvalue", permission_value)
                             .add_parameter("permnegated", permission_negated)
                             .add_parameter("permsip", permission_skip))

    def server_group_auto_del_perm(self, type, permission_id=None,
                                   permission_string_id=None):
        """
        Removes a set of specified permissions from *ALL* regular server groups
        on all virtual servers. The target groups will be identified by the
        value of their *i_group_auto_update_type permission* specified with
        *type*. Multiple permissions can be removed at once. A permission can
        be specified by *permission_id* or *permission_string_id*. The known
        values for *type*
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

        ServerQuery method: servergroupautodelperm sgtype={groupID}
        [permid={permID}…] [permsid={permName}…]

        :type type: int|:class:`tslib.server.GroupType`
        :param type: Group type
        :type permission_id: int
        :param permission_id: Permission ID
        :type permission_string_id: str
        :param permission_string_id: Permission name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        if permission_id is None and permission_string_id is None:
            return MissedParameterError(
                "*permid* or *permsid* must be specified")

        if permission_id:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", type)
                             .add_parameter("permid", permission_id))
        else:
            return self.send(Request(Command.SERVER_GROUP_AUTO_ADD_PERM)
                             .add_parameter("sgtype", type)
                             .add_parameter("permsid", permission_string_id))

    def server_snapshot_create(self):
        """
        Displays a snapshot of the selected virtual server containing all
        settings, groups and known client identities.
        The data from a server snapshot can be used to restore a virtual
        servers configuration, channels and permissions using the
        *server_snapshot_deploy* command.

        ServerQuery method: serversnapshotcreate

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_SNAPSHOT_CREATE))

    # TODO: Check, how it's should work, and then rewrite function
    def server_snapshot_deploy(self, snapshot, mapping=False):
        """
        Restores the selected virtual servers configuration using the data from
        a previously created server snapshot.
        Please note that the TeamSpeak 3 Server does NOT check for necessary
        permissions while deploying a snapshot so the command could be abused
        to gain additional privileges.

        ServerQuery method: serversnapshotdeploy [-mapping]
        virtualserver_snapshot

        :type snapshot: str
        :param snapshot:
        :type mapping: bol
        :param mapping:
        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_SNAPSHOT_DEPLOY)
                         .add_parameter(None, snapshot)
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

        ServerQuery method: servernotifyregister
        event={server|channel|textserver|textchannel|textprivate}
        [id={channelID}]

        :type event: str|:class:`tslib.server.Server.EventType`
        :param event: Event type
        :type id: int
        :param id: Channel ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        q = Request(Command.SERVER_NOTIFY_REGISTER).add_parameter("event",
                                                                  event)

        if event == EventType.CHANNEL \
                or event == EventType.TEXT_CHANNEL \
                or event == EventType.CHANNEL.value \
                or event == EventType.TEXT_CHANNEL.value:
            if not id:
                raise MissedParameterError
            q.add_parameter("id", id)

        return self.send(q)

    def server_notify_unregister(self):
        """
        Unregisters all events previously registered with
        *server_notify_register* so you will no longer receive notification
        messages.

        ServerQuery method: servernotifyunregister

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SERVER_NOTIFY_UNREGISTER))

    def send_text_message(self, target_mode, target, msg):
        """
        Sends a text message to a specified target. If *target_mode* is set to
        1, a message is sent to the client with the ID specified by *target*.
        If *target_mode* is set to 2 or 3, the *target* parameter will be
        ignored and a message is sent to the current channel or server
        respectively.

        ServerQuery method: sendtextmessage targetmode={1-3} target={clientID}
        msg={text}

        :type target_mode: int|:class:`tslib.server.TextMessageTargetMode`
        :param target_mode: Target mode
        :type target: int
        :param target: Client ID
        :type msg: str
        :param msg: Text

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SEND_TEXT_MESSAGE)
                         .add_parameter("targetmode", target_mode)
                         .add_parameter("target", target)
                         .add_parameter("msg", msg))

    def log_view(self, lines=None, reverse=False, instance=False,
                 begin_pos=None):
        """
        Displays a specified number of entries from the servers log. If
        *instance* is set to 1, the server will return lines from the master
        logfile (ts3server_0.log) instead of the selected virtual server
        logfile.

        ServerQuery method: logview [lines={1-100}] [reverse={1|0}]
        [instance={1|0}] [begin_pos={n}]

        :type lines: int
        :param lines: Number of lines
        :type reverse: bool
        :param reverse:
        :type instance: bool
        :param instance:
        :type begin_pos: int
        :param begin_pos: Begin position

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.LOG_VIEW)
                         .add_parameter("lines", lines)
                         .add_parameter("reverse", reverse)
                         .add_parameter("instance", instance)
                         .add_parameter("begin_pos", begin_pos))

    def log_add(self, log_lvl, log_msg):
        """
        Writes a custom entry into the servers log. Depending on your
        permissions, you'll be able to add entries into the server instance log
        and/or your virtual servers log. The *log_lvl* parameter specifies the
        type of the entry.

        ServerQuery method: logadd loglevel={1-4} logmsg={text}

        :type log_lvl: int
        :param log_lvl: int|:class:`tslib.server.LogLevel`
        :type log_msg: str
        :param log_msg: Log message
        """
        return self.send(Request(Command.LOG_ADD)
                         .add_parameter("loglvl", log_lvl)
                         .add_parameter("logmsg", log_msg))

    def gm(self, msg):
        """
        Sends a text message to all clients on all virtual servers in the
        TeamSpeak 3 Server instance.

        ServerQuery method: gm msg={text}

        :type msg: str
        :param msg: Message
        """
        return self.send(Request(Command.GM)
                         .add_parameter("msg", msg))

    def channel_list(self, topic=False, flags=False, voice=False, limits=False,
                     icon=False, seconds_empty=False):
        """
        Displays a list of channels created on a virtual server including their
        ID, order, name, etc. The output can be modified using several command
        options.

        ServerQuery method: channellist [-topic] [-flags] [-voice] [-limits]
        [-icon] [-secondsempty]

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
        :type seconds_empty: bool
        :param seconds_empty:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_LIST)
                         .add_option("topic", topic)
                         .add_option("flags", flags)
                         .add_option("voice", voice)
                         .add_option("limits", limits)
                         .add_option("icon", icon)
                         .add_option("secondsempty", seconds_empty))

    def channel_info(self, id):
        """
        Displays detailed configuration information about a channel including
        ID, topic, description, etc

        ServerQuery method: channelinfo cid={channelID}

        :type id: int
        :param id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_INFO)
                         .add_parameter("cid", id))

    def channel_find(self, pattern):
        """
        Displays a list of channels matching a given name pattern.

        ServerQuery method: channelfind pattern={channelName}

        :type pattern: str
        :param pattern: Channel name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_FIND)
                         .add_parameter("pattern", pattern))

    def channel_move(self, id, parent_id, order):
        """
        Moves a channel to a new parent channel with the ID *parent_id*. If
        *order* is specified, the channel will be sorted right under the
        channel with the specified ID. If *order* is set to 0, the channel will
        be sorted right below the new parent.

        ServerQuery method: channelmove cid={channelID} cpid={channelParentID}
        [order={channelSortOrder}]

        :type id: int
        :param id: Channel ID
        :type parent_id: int
        :param parent_id: Parent channel ID
        :type order: int
        :param order: Channel sort order

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_MOVE)
                         .add_parameter("cid", id)
                         .add_parameter("cpid", parent_id)
                         .add_parameter("order", order))

    def channel_create(self, name, **properties):
        """
        Creates a new channel using the given properties and displays its ID.
        Note that this command accepts multiple properties which means that
        you're able to specify all settings of the new channel at once.

        ServerQuery method: channelcreate channel_name={channelName}
        [channel_properties…]

        :type name: str
        :param name: Channel name
        :type properties: dict
        :param properties: Channel properties

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_CREATE)
                         .add_parameter("channel_name", name)
                         .add_parameters(**properties))

    def channel_delete(self, id, force=False):
        """
        Deletes an existing channel by ID. If *force* is set to 1, the channel
        will be deleted even if there are clients within. The clients will be
        kicked to the default channel with an appropriate reason message.

        ServerQuery method: channeldelete cid={channelID} force={1|0}

        :type id: int
        :param id: Channel ID
        :type force: bool
        :param force:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_DELETE)
                         .add_parameter("cid", id)
                         .add_parameter("force", force))

    def channel_edit(self, id, **properties):
        """
        Changes a channels configuration using given properties. Note that this
        command accepts multiple properties which means that you're able to
        change all settings of the channel specified with cid at once.

        ServerQuery method: channeledit cid={channelID} [channel_properties…]

        :type id: int
        :param id: Channel ID
        :type properties: dict
        :param properties: Channel properties

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_EDIT)
                         .add_parameter("cid", id)
                         .add_parameters(**properties))

    def channel_group_list(self):
        """
        Displays a list of channel groups available on the selected virtual
        server.

        ServerQuery method: channelgrouplist

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_LIST))

    def channel_group_add(self, name, type):
        """
        Creates a new channel group using a given name and displays its ID. The
        optional *type* parameter can be used to create template groups.

        ServerQuery method: channelgroupadd name={groupName}
        [type={groupDbType}]

        :type name: str
        :param name: Group name
        :type type: int|:class:`tslib.server.PermissionGroupDatabaseTypes`
        :param type: Channel group DB type

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_ADD)
                         .add_parameter("name", name)
                         .add_parameter("type", type))

    def channel_group_del(self, id, force=False):
        """
        Deletes a channel group by ID. If *force* is set to 1, the channel
        group will be deleted even if there are clients within.

        ServerQuery method: channelgroupdel cgid={groupID} force={1|0}

        :type id: int
        :param id: Channel group ID
        :type force: bool
        :param force:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_DEL)
                         .add_parameter("cgid", id)
                         .add_parameter("force", force))

    def channel_group_copy(self, source_id, target_id, name, type):
        """
        Creates a copy of the channel group specified with *source_group_id*.
        If *target_group_id* is set to 0, the server will create a new group.
        To overwrite an existing group, simply set *target_group_id* to the ID
        of a designated target group. If a target group is set, the *name*
        parameter will be ignored. The *type* parameter can be used to create
        template groups.

        ServerQuery method: channelgroupcopy scgid={sourceGroupID}
        tcgid={targetGroupID} name={groupName} type={groupDbType}

        :type source_id: int
        :param source_id: Source channel group ID
        :type target_id: int
        :param target_id: Target channel group ID
        :type name: str
        :param name: Channel group name
        :type type: int|:class:`tslib.server.PermissionGroupDatabaseTypes`
        :param type: Channel group DB type

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_COPY)
                         .add_parameter("scgid", source_id)
                         .add_parameter("tcgid", target_id)
                         .add_parameter("name", name)
                         .add_parameter("type", type))

    def channel_group_rename(self, id, name):
        """
        Changes the name of a specified channel group.

        ServerQuery method: channelgrouprename cgid={groupID} name={groupName}

        :type id: int
        :param id: Channel group ID
        :type name: str
        :param name: Channel group name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_RENAME)
                         .add_parameter("cgid", id)
                         .add_parameter("name", name))

    def channel_group_add_perm(self, id, permissions_set):
        """
        Adds a set of specified permissions to a channel group. Multiple
        permissions can be added by providing the two parameters of each
        permission. A permission can be specified by *permid* or *permsid*.

        ServerQuery method: channelgroupaddperm cgid={groupID}
        [permid={permID}…] [permsid={permName}…] permvalue={permValue}…

        :type id: int
        :param id: Channel group ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_ADD_PERM)
                         .add_parameter("cgid", id)
                         .add_list_of_parameters(permissions_set))

    def channel_group_perm_list(self, id, permission_string_id=False):
        """
        Displays a list of permissions assigned to the channel group specified
        with *id*. If the *-permission_string_id* option is specified, the
        output will contain the permission names instead of the internal IDs.

        ServerQuery method: channelgrouppermlist cgid={groupID} [-permsid]

        :type id: int
        :param id: Channel group ID
        :type permission_string_id: bool
        :param permission_string_id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_PERM_LIST)
                         .add_parameter("cgid", id)
                         .add_option("permsid", permission_string_id))

    def channel_group_del_perm(self, id, permissions_set):
        """
        Removes a set of specified permissions from the channel group. Multiple
        permissions can be removed at once. A permission can be specified by
        *permid* or *permsid*.

        ServerQuery method: channelgroupdelperm cgid={groupID}
        [permid={permID}…] [permsid={permName}…]

        :type id: int
        :param id: Channel group ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_GROUP_DEL_PERM)
                         .add_parameter("cgid", id)
                         .add_list_of_parameters(permissions_set))

    # TODO: Implement functionality
    def channel_group_client_list(self):
        raise NotImplementedError

    def set_client_channel_group(self, group_id, channel_id, client_db_id):
        """
        Sets the channel group of a client to the ID specified with *group_id*.

        ServerQuery method: setclientchannelgroup cgid={groupID}
        cid={channelID} cldbid={clientDBID}

        :type group_id: int
        :param group_id: Channel group ID
        :type channel_id: int
        :param channel_id: Channel ID
        :type client_db_id: int
        :param client_db_id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.SET_CLIENT_CHANNEL_GROUP)
                         .add_parameter("cgid", group_id)
                         .add_parameter("cid", channel_id)
                         .add_parameter("cldbid", client_db_id))

    def channel_perm_list(self, id, permission_string_id=False):
        """
        Displays a list of permissions defined for a channel.

        ServerQuery method: channelpermlist cid={channelID} [-permsid]

        :type id: int
        :param id: Channel ID
        :type permission_string_id: bool
        :param permission_string_id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_PERM_LIST)
                         .add_parameter("cid", id)
                         .add_option("permsid", permission_string_id))

    def channel_add_perm(self, id, permissions_set):
        """
        Adds a set of specified permissions to a channel. Multiple permissions
        can be added by providing the two parameters of each permission. A
        permission can be specified by *permid* or *permsid*.

        ServerQuery method: channeladdperm cid={channelID} [permid={permID}…]
        [permsid={permName}…] permvalue={permValue}…

        :type id: int
        :param id: Channel ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_ADD_PERM)
                         .add_parameter("cid", id)
                         .add_list_of_parameters(permissions_set))

    def channel_del_perm(self, id, permissions_set):
        """
        Removes a set of specified permissions from a channel. Multiple
        permissions can be removed at once. A permission can be specified by
        *permid* or *permsid*.

        ServerQuery method: channeldelperm cid=123 [permid={permID}…]
        [permsid={permName}…]

        :type id: int
        :param id: Channel ID
        :type permissions_set: list of dicts
        :param permissions_set:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CHANNEL_DEL_PERM)
                         .add_parameter("cid", id)
                         .add_list_of_parameters(permissions_set))

    def client_list(self, unique_id=False, away=False, voice=False, times=False,
                    groups=False, info=False, icon=False, country=False):
        """
        Displays a list of clients online on a virtual server including their
        ID, nickname, status flags, etc. The output can be modified using
        several command options.
        Please note that the output will only contain clients which are
        currently in channels you're able to subscribe to.

        ServerQuery method: clientlist [-uid] [-away] [-voice] [-times]
        [-groups] [-info] [-country] [-ip] [-badges]

        :type unique_id: bool
        :param unique_id:
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
                         .add_option("uid", unique_id)
                         .add_option("away", away)
                         .add_option("voice", voice)
                         .add_option("times", times)
                         .add_option("groups", groups)
                         .add_option("info", info)
                         .add_option("icon", icon)
                         .add_option("country", country))

    def client_info(self, id):
        """
        Displays detailed configuration information about a client including
        unique ID, nickname, client version, etc

        ServerQuery method: clientinfo clid={clientID}

        :type id: int
        :param id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_INFO)
                         .add_parameter("clid", id))

    def client_find(self, pattern):
        """
        Displays a list of clients matching a given name pattern.

        ServerQuery method: clientfind pattern={clientName}

        :type pattern: str
        :param pattern: Client name

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_FIND)
                         .add_parameter("pattern", pattern))

    def client_edit(self, id, **properties):
        """
        Changes a clients settings using given properties.

        ServerQuery method: clientedit clid={clientID} [client_properties…]

        :type id: int
        :param id: Client ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_EDIT)
                         .add_parameter("clid", id)
                         .add_parameters(**properties))

    def client_db_list(self, start=None, duration=None, count=False):
        """
        Displays a list of client identities known by the server including
        their database ID, last nickname, etc.

        ServerQuery method: clientdblist [start={offset}] [duration={limit}]
        [-count]

        :type start: int
        :param start: Offset
        :type duration: int
        :param duration: Limit
        :type count: bool
        :param count:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_DB_LIST)
                         .add_parameter("start", start)
                         .add_parameter("duration", duration)
                         .add_option("count", count))

    def client_db_info(self, id):
        """
        Displays detailed database information about a client including unique
        ID, creation date, etc.

        ServerQuery method: clientdbinfo cldbid={clientDBID}

        :type id: int
        :param id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_DB_INFO)
                         .add_parameter("cldbid", id))

    def client_db_find(self, pattern, unique_id=False):
        """
        Displays a list of client database IDs matching a given pattern. You
        can either search for a clients last known nickname or his unique
        identity by using the *-unique_id* option. The pattern parameter can
        include regular characters and SQL wildcard characters (e.g. %).

        ServerQuery method: clientdbfind pattern={clientName|clientUID} [-uid]

        :type pattern: str
        :param pattern: Client name | Client Unique ID
        :type unique_id: bool
        :param unique_id:

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_DB_FIND)
                         .add_parameter("pattern", pattern)
                         .add_option("uid", unique_id))

    def client_db_edit(self, id, **properties):
        """
        Changes a clients settings using given properties.

        ServerQuery method: clientdbedit cldbid={clientDBID}
        [client_properties…]

        :type id: int
        :param id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_DB_EDIT)
                         .add_parameter("cldbid", id)
                         .add_parameters(**properties))

    def client_db_delete(self, id):
        """
        Deletes a clients properties from the database.

        ServerQuery method: clientdbdelete cldbid={clientDBID}

        :type id: int
        :param id: Client DB ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_DB_DELETE)
                         .add_parameter("cldbid", id))

    def client_get_ids(self, unique_id):
        """
        Displays all client IDs matching the unique identifier specified by
        *unique_id*.

        ServerQuery method: clientgetids cluid={clientUID}

        :type unique_id: str
        :param unique_id: Client Unique ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_GET_IDS)
                         .add_parameter("cluid", unique_id))

    def client_get_db_id_from_uid(self, unique_id):
        """
        Displays the database ID matching the unique identifier specified by
        *unique_id*.

        ServerQuery method: clientgetdbidfromuid cluid={clientUID}

        :type unique_id: str
        :param unique_id: Client Unique ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_GET_DB_ID_FROM_UID)
                         .add_parameter("cluid", unique_id))

    def client_get_name_from_uid(self, unique_id):
        """
        Displays the database ID and nickname matching the unique identifier
        specified by *unique_id*.

        ServerQuery method: clientgetnamefromuid cluid={clientUID}

        :type unique_id: str
        :param unique_id: Client Unique ID

        :rtype: :class:`tslib.response.Response`
        :return: Response object
        """
        return self.send(Request(Command.CLIENT_GET_NAME_FROM_UID)
                         .add_parameter("cluid", unique_id))

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

        ServerQuery method: whoami

        :rtype: :class:`tslib.response.Response`
        :return: Request object
        """
        return self.send(Request(Command.WHO_AM_I))
