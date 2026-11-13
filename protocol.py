"""Used by both server.py and client.py: how one message travels over TCP."""
import socket

HEADER_SIZE = 4


def recv_exact(sock: socket.socket, n: int) -> bytes | None:
    # recv in a loop until there are n bytes; None if the connection closed
    pass


def send_msg(sock: socket.socket, data: bytes) -> None:
    # a 4-byte big-endian length, then the data
    pass


def recv_msg(sock: socket.socket) -> bytes | None:
    # read the length, then read that many bytes; None if the connection closed
    pass
