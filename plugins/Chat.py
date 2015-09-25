"""
    Plugin Name : Chat
    Plugin Version : 1.0

    Description:
        Gives basic commands to the bot

    Contributors:
        - Patrick Hennessy

    License:
        PhilBot is free software: you can redistribute it and/or modify it
        under the terms of the GNU General Public License v3; as published
        by the Free Software Foundation
"""

Metadata = {
    "Name": "Chat",
    "Description": "Basic stuff",
    "Version": 1,
    "Entrypoint": "Chat"
}

from core.Plugin import Plugin
from core.Decorators import command

class Chat(Plugin):

    def activate(self):
        self.ping("i am the message")
        pass

    @command("^.ping$")
    def ping(self, msg):
        pass
