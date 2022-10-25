#!/usr/bin/python3

import struct


def main():
    with open("encoded.bin", "wb") as f:
        s = "happy birthday Matt!"
        f.write(s.encode("utf-8"))
        for c in "happy birthday Matt!":
            f.write(struct.pack("B", ord(c) ^ 0x55))
    # with open("encoded.bin", "rb") as f:
    #     for c in f.read():
    #         print(chr(c ^ 0x55), end="")
    #     print()


if __name__ == "__main__":
    main()
