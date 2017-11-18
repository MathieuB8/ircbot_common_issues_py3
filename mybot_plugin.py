# -*- coding: utf-8 -*-
from irc3.plugins.command import command
import irc3
import asyncio


@irc3.plugin
class Plugin:

    def __init__(self, bot):
        self.bot = bot

    """@irc3.event(irc3.rfc.JOIN)
    def say_hi(self, mask, channel, **kw):
        Say hi when someone join a channel
        if mask.nick != self.bot.nick:
            self.bot.privmsg(channel, 'Hi %s!' % mask.nick)
        else:
            self.bot.privmsg(channel, 'Hi!')"""

    @command
    def special(self, mask, target, args):
        """special method okay
            %%special
        """
        try:
            self.bot.privmsg(target,'mmh interesting')
        except:
            pass

    @irc3.event(irc3.rfc.PRIVMSG)
    @asyncio.coroutine
    def on_privmsg(self, *args, **kwargs):
        msg, channel, sender = kwargs['data'], kwargs['target'], kwargs['mask']
        try:
			#flag issue
            if ('flag' in msg and 'issue' in msg) or ('flag' in msg and 'when' in msg) or  ('flag' in msg and 'fix' in msg):
                self.bot.privmsg(channel,'Devs are aware of the flag issue. It may be fixed with the next server update.')
                return

			#error : fa failed to start or file not properly sent by the server.
            if ('fa' in msg and 'failed' in msg and 'start' in msg) or ('fa' in msg and 'start' in msg and 'fail' in msg) or  ('download' in msg and 'file' in msg) or ('file' in msg and 'properly' in msg and 'sent' in msg) or  ('file' in msg and 'properly' in msg and 'sent' in msg) or ('file' in msg and 'not' in msg and 'sent' in msg):
                self.bot.privmsg(channel,'Try these solutions : Go to  option menu >> clear data >> clear game files. Verify your antivirus is not blocking it. Try disabling your antivirus. Verify firewall is not blocking it. Try disabling your firewall')
                self.bot.privmsg(channel,'Otherwise try this : http://forums.faforever.com/viewtopic.php?f=3&t=15287&p=155049#p155049 . If it is still not fixed. Report it on the forum or on discord in technical help to fix this issue.')
                return

			#can't make accounts
            if ('account' in msg and 'registration' in msg and 'error' in msg) or ('account' in msg and 'creation' in msg and 'error' in msg) or  ('make' in msg and 'account' in msg and 'error' in msg) or  ('make' in msg and 'new account' in msg and 'disable' in msg) or ('Error! Invalid registration sign up. Please try again later' in msg) or  ('issue' in msg and 'account' in msg and 'creation' in msg) or ('cant' in msg and 'create' in msg and 'new account' in msg) or ('issue' in msg and 'https://www.faforever.com/account/register' in msg) or ('error' in msg and 'https://www.faforever.com/account/register' in msg):
                self.bot.privmsg(channel,'Currently account registration is temporary disabled but will be enabled later.')
                return

			#can't make accounts
            if ('cant' in msg and 'connect' in msg and 'player' in msg) or ('cant' in msg and 'connect' in msg and 'people' in msg) or ('issue' in msg and 'connect' in msg and 'people' in msg) or ('issue' in msg and 'connect' in msg and 'player' in msg):
				self.bot.privmsg(channel,'Make sure you and the other player have an open port for the game : You gotta access your router and map a port (default is 6112 UDP) to your local ip address and make sure that UPNP is disabled in the client.')
                return
        except:
            pass
