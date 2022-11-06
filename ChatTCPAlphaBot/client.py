#!/usr/bin/env python
import sys
from socket import socket, AF_INET, SOCK_STREAM
from packet import Packet

class ClientOptions:
    def __init__(self, ip, port, *args):

        # TODO: validation
        self.ip = ip
        self.port = int(port)

    def get_socket(self):
        return self.ip, self.port

def ask_command():
    return input("$> ")

def main(args):

    options = ClientOptions(*args[1:]) # cli arguments, less the program name
    go_on = True

    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(options.get_socket())

        while go_on:
            # TODO: to send more complex data types write
            #       his own class with serialization and
            #       deserialization

            cmd = ask_command()

            if cmd == "exit":
                go_on = False
            else:
                cmd.split(";")
                cmd = Packet(cmd)
                cmd = cmd.to_bytes()
                s.send(cmd.encode('utf-8'))

if __name__ == "__main__":
    main(sys.argv)
