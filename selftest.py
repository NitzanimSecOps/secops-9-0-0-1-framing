"""Local tester for protocol.py and server.py - not the hidden grader.

    python3 selftest.py

Starts your server.py in the background and talks to it: a short message, a message sent one byte
at a time, two messages in one send, and a large message. Change the examples and try your own.
"""
import os
import socket
import struct
import subprocess
import sys
import time

HOST = "127.0.0.1"
PORT = 2405


def frame(data):
    return struct.pack("!I", len(data)) + data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        sys.path.insert(0, here)
        from protocol import recv_msg, send_msg

        with socket.create_connection((HOST, PORT)) as s:
            s.settimeout(5)
            send_msg(s, b"hello")
            print("short message:", recv_msg(s))

            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            for i, byte in enumerate(frame(b"one byte at a time")):
                s.sendall(bytes([byte]))
                time.sleep(0.01)
            print("split message:", recv_msg(s))

            s.sendall(frame(b"first") + frame(b"second"))
            print("two together:", recv_msg(s), recv_msg(s))

            big = bytes(range(256)) * 20000
            send_msg(s, big)
            print("large message identical:", recv_msg(s) == big)
    finally:
        server.kill()


if __name__ == "__main__":
    main()
