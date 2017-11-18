import irclib
import ircbot

class MonBot(ircbot.SingleServerIRCBot):
	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [("irc.faforever.com", 6667)],"RandomDudepls", "random bot")

	def on_welcome(self, serv, ev):
		serv.join("#test-ircbot")

	def on_pubmsg(self, serv, ev):
		pass
if __name__ == "__main__":
	MonBot().start()