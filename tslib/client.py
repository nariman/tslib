#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamSpeak 3 Python Library
tslib.client.

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

logger = logging.getLogger(__name__)


"""
Enumerations
"""

class Command(Enum):
    BAN_ADD = "banadd"
    BAN_CLIENT = "banclient"
    BAN_DEL = "bandel"
    BAN_DEL_ALL = "bandelall"
    BAN_LIST = "banlist"
    CHANNEL_ADD_PERM = "channeladdperm"
    CHANNEL_CLIENT_ADD_PERM = "channelclientaddperm"
    CHANNEL_CLIENT_DEL_PERM = "channelclientdelperm"
    CHANNEL_CLIENT_LIST = "channelclientlist"
    CHANNEL_CLIENT_PERM_LIST = "channelclientpermlist"
    CHANNEL_CONNECT_INFO = "channelconnectinfo"
    CHANNEL_CREATE = "channelcreate"
    CHANNEL_DELETE = "channeldelete"
    CHANNEL_DELPERM = "channeldelperm"
    CHANNEL_EDIT = "channeledit"
    CHANNEL_GROUP_ADD = "channelgroupadd"
    CHANNEL_GROUP_ADD_PERM = "channelgroupaddperm"
    CHANNEL_GROUP_CLIENT_LIST = "channelgroupclientlist"
    CHANNEL_GROUP_DEL = "channelgroupdel"
    CHANNEL_GROUP_DEL_PERM = "channelgroupdelperm"
    CHANNEL_GROUP_LIST = "channelgrouplist"
    CHANNEL_GROUP_PERM_LIST = "channelgrouppermlist"
    CHANNEL_LIST = "channellist"
    CHANNEL_MOVE = "channelmove"
    CHANNEL_PERM_LIST = "channelpermlist"
    CHANNEL_VARIABLE = "channelvariable"
    CLIENT_ADD_PERM = "clientaddperm"
    CLIENT_DB_DELETE = "clientdbdelete"
    CLIENT_DB_EDIT = "clientdbedit"
    CLIENT_DB_LIST = "clientdblist"
    CLIENT_DEL_PERM = "clientdelperm"
    CLIENT_GET_DB_ID_FROM_UID = "clientgetdbidfromuid"
    CLIENT_GET_IDS = "clientgetids"
    CLIENT_GET_NAME_FROM_DB_ID = "clientgetnamefromdbid"
    CLIENT_GET_NAME_FROM_UID = "clientgetnamefromuid"
    CLIENT_GET_UID_FROM_CL_ID = "clientgetuidfromclid"
    CLIENT_KICK = "clientkick"
    CLIENT_LIST = "clientlist"
    CLIENT_MOVE = "clientmove"
    CLIENT_MUTE = "clientmute"
    CLIENT_NOTIFY_REGISTER = "clientnotifyregister"
    CLIENT_NOTIFY_UNREGISTER = "clientnotifyunregister"
    CLIENT_PERM_LIST = "clientpermlist"
    CLIENT_POKE = "clientpoke"
    CLIENT_UNMUTE = "clientunmute"
    CLIENT_UPDATE = "clientupdate"
    CLIENT_VARIABLE = "clientvariable"
    COMPLAIN_ADD = "complainadd"
    COMPLAIN_DEL = "complaindel"
    COMPLAIN_DEL_ALL = "complaindelall"
    COMPLAIN_LIST = "complainlist"
    CURRENT_SCHANDLER_ID = "currentschandlerid"
    FT_CREATE_DIR = "ftcreatedir"
    FT_DELETE_FILE = "ftdeletefile"
    FT_GET_FILE_INFO = "ftgetfileinfo"
    FT_GET_FILE_LIST = "ftgetfilelist"
    FT_INIT_DOWNLOAD = "ftinitdownload"
    FT_INIT_UPLOAD = "ftinitupload"
    FT_LIST = "ftlist"
    FT_RENAME_FILE = "ftrenamefile"
    FT_STOP = "ftstop"
    HASH_PASSWORD = "hashpassword"
    HELP = "help"
    MESSAGE_ADD = "messageadd"
    MESSAGE_DEL = "messagedel"
    MESSAGE_GET = "messageget"
    MESSAGE_LIST = "messagelist"
    MESSAGE_UPDATE_FLAG = "messageupdateflag"
    PERM_OVERVIEW = "permoverview"
    QUIT = "quit"
    SEND_TEXT_MESSAGE = "sendtextmessage"
    SERVER_CONNECT_INFO = "serverconnectinfo"
    SERVER_CONNECTION_HANDLER_LIST = "serverconnectionhandlerlist"
    SERVER_GROUP_ADD = "servergroupadd"
    SERVER_GROUP_ADD_CLIENT = "servergroupaddclient"
    SERVER_GROUP_ADD_PERM = "servergroupaddperm"
    SERVER_GROUP_CLIENT_LIST = "servergroupclientlist"
    SERVER_GROUP_DEL = "servergroupdel"
    SERVER_GROUP_DEL_CLIENT = "servergroupdelclient"
    SERVER_GROUP_DEL_PERM = "servergroupdelperm"
    SERVER_GROUP_LIST = "servergrouplist"
    SERVER_GROUP_PERM_LIST = "servergrouppermlist"
    SERVER_GROUPS_BY_CLIENT_ID = "servergroupsbyclientid"
    SERVER_VARIABLE = "servervariable"
    SET_CLIENT_CHANNEL_GROUP = "setclientchannelgroup"
    TOKEN_ADD = "tokenadd"
    TOKEN_DELETE = "tokendelete"
    TOKEN_LIST = "tokenlist"
    TOKEN_USE = "tokenuse"
    USE = "use"
    VERIFY_CHANNEL_PASSWORD = "verifychannelpassword"
    VERIFY_SERVER_PASSWORD = "verifyserverpassword"
    WHO_AM_I = "whoami"
    # Aliases
    BANADD = "banadd"
    BANCLIENT = "banclient"
    BANDEL = "bandel"
    BANDELALL = "bandelall"
    BANLIST = "banlist"
    CHANNELADDPERM = "channeladdperm"
    CHANNELCLIENTADDPERM = "channelclientaddperm"
    CHANNELCLIENTDELPERM = "channelclientdelperm"
    CHANNELCLIENTLIST = "channelclientlist"
    CHANNELCLIENTPERMLIST = "channelclientpermlist"
    CHANNELCONNECTINFO = "channelconnectinfo"
    CHANNELCREATE = "channelcreate"
    CHANNELDELETE = "channeldelete"
    CHANNELDELPERM = "channeldelperm"
    CHANNELEDIT = "channeledit"
    CHANNELGROUPADD = "channelgroupadd"
    CHANNELGROUPADDPERM = "channelgroupaddperm"
    CHANNELGROUPCLIENTLIST = "channelgroupclientlist"
    CHANNELGROUPDEL = "channelgroupdel"
    CHANNELGROUPDELPERM = "channelgroupdelperm"
    CHANNELGROUPLIST = "channelgrouplist"
    CHANNELGROUPPERMLIST = "channelgrouppermlist"
    CHANNELLIST = "channellist"
    CHANNELMOVE = "channelmove"
    CHANNELPERMLIST = "channelpermlist"
    CHANNELVARIABLE = "channelvariable"
    CLIENTADDPERM = "clientaddperm"
    CLIENTDBDELETE = "clientdbdelete"
    CLIENTDBEDIT = "clientdbedit"
    CLIENTDBLIST = "clientdblist"
    CLIENTDELPERM = "clientdelperm"
    CLIENTGETDBIDFROMUID = "clientgetdbidfromuid"
    CLIENTGETIDS = "clientgetids"
    CLIENTGETNAMEFROMDBID = "clientgetnamefromdbid"
    CLIENTGETNAMEFROMUID = "clientgetnamefromuid"
    CLIENTGETUIDFROMCLID = "clientgetuidfromclid"
    CLIENTKICK = "clientkick"
    CLIENTLIST = "clientlist"
    CLIENTMOVE = "clientmove"
    CLIENTMUTE = "clientmute"
    CLIENTNOTIFYREGISTER = "clientnotifyregister"
    CLIENTNOTIFYUNREGISTER = "clientnotifyunregister"
    CLIENTPERMLIST = "clientpermlist"
    CLIENTPOKE = "clientpoke"
    CLIENTUNMUTE = "clientunmute"
    CLIENTUPDATE = "clientupdate"
    CLIENTVARIABLE = "clientvariable"
    COMPLAINADD = "complainadd"
    COMPLAINDEL = "complaindel"
    COMPLAINDELALL = "complaindelall"
    COMPLAINLIST = "complainlist"
    CURRENTSCHANDLERID = "currentschandlerid"
    FTCREATEDIR = "ftcreatedir"
    FTDELETEFILE = "ftdeletefile"
    FTGETFILEINFO = "ftgetfileinfo"
    FTGETFILELIST = "ftgetfilelist"
    FTINITDOWNLOAD = "ftinitdownload"
    FTINITUPLOAD = "ftinitupload"
    FTLIST = "ftlist"
    FTRENAMEFILE = "ftrenamefile"
    FTSTOP = "ftstop"
    HASHPASSWORD = "hashpassword"
    # HELP = "help"
    MESSAGEADD = "messageadd"
    MESSAGEDEL = "messagedel"
    MESSAGEGET = "messageget"
    MESSAGELIST = "messagelist"
    MESSAGEUPDATEFLAG = "messageupdateflag"
    PERMOVERVIEW = "permoverview"
    # QUIT = "quit"
    SENDTEXTMESSAGE = "sendtextmessage"
    SERVERCONNECTINFO = "serverconnectinfo"
    SERVERCONNECTIONHANDLERLIST = "serverconnectionhandlerlist"
    SERVERGROUPADD = "servergroupadd"
    SERVERGROUPADDCLIENT = "servergroupaddclient"
    SERVERGROUPADDPERM = "servergroupaddperm"
    SERVERGROUPCLIENTLIST = "servergroupclientlist"
    SERVERGROUPDEL = "servergroupdel"
    SERVERGROUPDELCLIENT = "servergroupdelclient"
    SERVERGROUPDELPERM = "servergroupdelperm"
    SERVERGROUPLIST = "servergrouplist"
    SERVERGROUPPERMLIST = "servergrouppermlist"
    SERVERGROUPSBYCLIENTID = "servergroupsbyclientid"
    SERVERVARIABLE = "servervariable"
    SETCLIENTCHANNELGROUP = "setclientchannelgroup"
    TOKENADD = "tokenadd"
    TOKENDELETE = "tokendelete"
    TOKENLIST = "tokenlist"
    TOKENUSE = "tokenuse"
    # USE = "use"
    VERIFYCHANNELPASSWORD = "verifychannelpassword"
    VERIFYSERVERPASSWORD = "verifyserverpassword"
    WHOAMI = "whoami"


"""
Interface
"""


class Client(Interface):
    """
    TeamSpeak 3 ClientQuery Connection Interface
    """
    _RECV_DAEMON_START_REQUIRED = [Command.SERVER_NOTIFY_REGISTER]

    def send(self, request):
        if request.enum_command in self._RECV_DAEMON_START_REQUIRED:
            self.start_recv_thread()

    def ban_add(self):
        raise NotImplementedError

    def ban_client(self):
        raise NotImplementedError

    def ban_del(self):
        raise NotImplementedError

    def ban_del_all(self):
        raise NotImplementedError

    def ban_list(self):
        raise NotImplementedError

    def channel_add_perm(self):
        raise NotImplementedError

    def channel_client_add_perm(self):
        raise NotImplementedError

    def channel_client_del_perm(self):
        raise NotImplementedError

    def channel_client_list(self):
        raise NotImplementedError

    def channel_client_perm_list(self):
        raise NotImplementedError

    def channel_connect_info(self):
        raise NotImplementedError

    def channel_create(self):
        raise NotImplementedError

    def channel_delete(self):
        raise NotImplementedError

    def channel_delperm(self):
        raise NotImplementedError

    def channel_edit(self):
        raise NotImplementedError

    def channel_group_add(self):
        raise NotImplementedError

    def channel_group_add_perm(self):
        raise NotImplementedError

    def channel_group_client_list(self):
        raise NotImplementedError

    def channel_group_del(self):
        raise NotImplementedError

    def channel_group_del_perm(self):
        raise NotImplementedError

    def channel_group_list(self):
        raise NotImplementedError

    def channel_group_perm_list(self):
        raise NotImplementedError

    def channel_list(self):
        raise NotImplementedError

    def channel_move(self):
        raise NotImplementedError

    def channel_perm_list(self):
        raise NotImplementedError

    def channel_variable(self):
        raise NotImplementedError

    def client_add_perm(self):
        raise NotImplementedError

    def client_db_delete(self):
        raise NotImplementedError

    def client_db_edit(self):
        raise NotImplementedError

    def client_db_list(self):
        raise NotImplementedError

    def client_del_perm(self):
        raise NotImplementedError

    def client_get_db_id_from_uid(self):
        raise NotImplementedError

    def client_get_ids(self):
        raise NotImplementedError

    def client_get_name_from_db_id(self):
        raise NotImplementedError

    def client_get_name_from_uid(self):
        raise NotImplementedError

    def client_get_uid_from_cl_id(self):
        raise NotImplementedError

    def client_kick(self):
        raise NotImplementedError

    def client_list(self):
        raise NotImplementedError

    def client_move(self):
        raise NotImplementedError

    def client_mute(self):
        raise NotImplementedError

    def client_notify_register(self):
        raise NotImplementedError

    def client_notify_unregister(self):
        raise NotImplementedError

    def client_perm_list(self):
        raise NotImplementedError

    def client_poke(self):
        raise NotImplementedError

    def client_unmute(self):
        raise NotImplementedError

    def client_update(self):
        raise NotImplementedError

    def client_variable(self):
        raise NotImplementedError

    def complain_add(self):
        raise NotImplementedError

    def complain_del(self):
        raise NotImplementedError

    def complain_del_all(self):
        raise NotImplementedError

    def complain_list(self):
        raise NotImplementedError

    def current_schandler_id(self):
        raise NotImplementedError

    def ft_create_dir(self):
        raise NotImplementedError

    def ft_delete_file(self):
        raise NotImplementedError

    def ft_get_file_info(self):
        raise NotImplementedError

    def ft_get_file_list(self):
        raise NotImplementedError

    def ft_init_download(self):
        raise NotImplementedError

    def ft_init_upload(self):
        raise NotImplementedError

    def ft_list(self):
        raise NotImplementedError

    def ft_rename_file(self):
        raise NotImplementedError

    def ft_stop(self):
        raise NotImplementedError

    def hash_password(self):
        raise NotImplementedError

    def help(self):
        raise NotImplementedError

    def message_add(self):
        raise NotImplementedError

    def message_del(self):
        raise NotImplementedError

    def message_get(self):
        raise NotImplementedError

    def message_list(self):
        raise NotImplementedError

    def message_update_flag(self):
        raise NotImplementedError

    def perm_overview(self):
        raise NotImplementedError

    def quit(self):
        raise NotImplementedError

    def send_text_message(self):
        raise NotImplementedError

    def server_connect_info(self):
        raise NotImplementedError

    def server_connection_handler_list(self):
        raise NotImplementedError

    def server_group_add(self):
        raise NotImplementedError

    def server_group_add_client(self):
        raise NotImplementedError

    def server_group_add_perm(self):
        raise NotImplementedError

    def server_group_client_list(self):
        raise NotImplementedError

    def server_group_del(self):
        raise NotImplementedError

    def server_group_del_client(self):
        raise NotImplementedError

    def server_group_del_perm(self):
        raise NotImplementedError

    def server_group_list(self):
        raise NotImplementedError

    def server_group_perm_list(self):
        raise NotImplementedError

    def server_groups_by_client_id(self):
        raise NotImplementedError

    def server_variable(self):
        raise NotImplementedError

    def set_client_channel_group(self):
        raise NotImplementedError

    def token_add(self):
        raise NotImplementedError

    def token_delete(self):
        raise NotImplementedError

    def token_list(self):
        raise NotImplementedError

    def token_use(self):
        raise NotImplementedError

    def use(self):
        raise NotImplementedError

    def verify_channel_password(self):
        raise NotImplementedError

    def verify_server_password(self):
        raise NotImplementedError

    def who_am_i(self):
        raise NotImplementedError
