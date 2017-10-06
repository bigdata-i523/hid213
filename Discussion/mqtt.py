from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.mycommand.api.manager import Manager
import OS as os
import paho.mqtt.client as mqtt

class MycommandCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_mycommand(self, args, arguments):
        """
        ::
          Usage:
                mycommand path

          Arguments:
              path   the folder path for all the file we need to upload to the server

        """
        client = mqtt.Client()
        client.reinitialise()

        client.connect("www.youtube.com")

        files = os.listdir(arguments)
        for file in files:
          client.publish('filename'，file)
        
        client.disconnect()





