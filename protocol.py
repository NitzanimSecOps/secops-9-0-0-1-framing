HEADER_SIZE = 4


def recv_exact(sock, n):
    # recv in a loop until there are n bytes; None if the connection closed
    pass


def send_msg(sock, data):
    # a 4-byte big-endian length, then the data
    pass


def recv_msg(sock):
    # read the length, then read that many bytes; None if the connection closed
    pass
