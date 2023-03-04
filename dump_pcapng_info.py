#!/usr/bin/env python

from __future__ import print_function

import sys

import pcapng


def dump_information(scanner):
    # for block in scanner:
    #     print(block)
    print(scanner(0))

if __name__ == "__main__":
    # if len(sys.argv) > 1:
    #     with open(sys.argv[1], "rb") as fp:
    #         scanner = pcapng.FileScanner(fp)
    #         dump_information(scanner)
    with open(r'C:\Users\jorin\PycharmProjects\Wireshark\test1_00001_20230220144445.pcapng', "rb") as fp:
        scanner = pcapng.FileScanner(fp)
        dump_information(scanner)
    #
    # else:
    #     scanner = pcapng.FileScanner(sys.stdin)
    #     dump_information(scanner)
