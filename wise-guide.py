import sys
sys.path.insert(0, './app')
from controller import Controller
import configparser
import discord
import logging


__author__ = 'dcpulido91@gmail.com'


def ConfigSectionMap(section, Config):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                logging.info('skip: %s' % option)
        except:
            logging.info('exception on %s!' % option)
            dict1[option] = None
    return dict1


def get_general_conf(name):
    Config = configparser.ConfigParser()
    Config.read('./conf/config.conf')
    myprior = {}
    for sec in Config.sections():
        if sec == name:
            myprior = ConfigSectionMap(sec, Config)
    return myprior


generalconf = get_general_conf('General')
tokens = get_general_conf('Tokens')
client = discord.Client()
controller = Controller(generalconf, tokens, client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == "!":
        msg = controller.parse_message(message, client)
        await client.send_message(message.channel, msg)
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == '__main__':
    if generalconf["log"] == "1":
        logging.basicConfig(
            format='%(asctime)s %(levelname)s:%(message)s',
            level=logging.DEBUG)
    client.run(tokens["discord_token"])
