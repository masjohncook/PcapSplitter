#!/bin/python

import sys
# from pexpect import expect
from subprocess import Popen, check_call, DEVNULL, STDOUT
import os
import argparse


# check editcap availability, if no install Tshark

class pcap_splitter:
    msg = ""
    def __init__(self):
        pass

    def check_editcap():
        try:
            cmd1 = check_call(['editcap', '--help'], stdout=DEVNULL, stderr=STDOUT)
            msg = "OK"
            return msg

        except FileNotFoundError:
            cmd2 = 'apt install tshark'
            install = check_call('sudo -S {}'.format(cmd2), shell=True)
            msg = "OK"
            return msg

    def split_pcap():
        try:
            filename = sys.argv[1]
            get_filename = filename.split('/')[-1]
            only_filename = get_filename.split('.')
            new_filename = only_filename[0] + "_split.pcap"
            split = check_call(['editcap', '-i', '180', '-F', 'pcap', filename, new_filename],
                               stdout=DEVNULL,
                               stderr=STDOUT)
        except FileNotFoundError:
            print("File not found")


if __name__ == "__main__":
    try:
        if (pcap_splitter.check_editcap() == 'OK'):
            pcap_splitter.split_pcap()
        else:
            exit()
    except FileNotFoundError:
        print()
