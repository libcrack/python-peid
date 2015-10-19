#!/usr/bin/python2
# coding: utf-8
# vim:ts=4 sts=4 tw=100:

__version__ = "1.5.0"
__author__  = "Borja Ruiz"
__email__   = "borja [at] libcrack [dot] so"
__url__     = "https://www.github.com/borjiviri/peid"

import logging
import peutils
import pefile
import sys
import os

try:
    import argparse
except ImportError as e:
    logger.error('Missing needed module: easy_install argparse')
    halt = True

try:
    import pefile
except ImportError as e:
    logger.error('Missing mandatory module: easy_install pefile')
    halt = True

CWD = os.path.abspath(os.path.dirname(__file__))
USERDB = os.path.join(CWD, os.path.normpath("data/UserDB.TXT"))

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all", dest="show_all", help="show all PE info", default=False, action="store_true")
parser.add_argument("-d", "--database", dest="database", help="signature database file", metavar="DB")
parser.add_argument("-m", "--matches", dest="show_matches", help="show all signature matches", default=False, action="store_true")
parser.add_argument("-v", "--version", dest="version", help="show version number", default=False, action="store_true")
parser.add_argument("-f", "--file", dest="file", help="target PE file", required=True, action="store")
args = parser.parse_args()

logging.basicConfig(level=logging.ERROR)

print("\033[91m")
print(" _____  ______ _ _____  ")
print("|  __ \|  ____(_)  __ \ ")
print("| |__) | |__   _| |  | |")
print("|  ___/|  __| | | |  | |")
print("| |    | |____| | |__| |")
print("|_|    |______|_|_____/ ")
print("\033[0m")
print("User DB: %s" % USERDB)
print("Author:  Borja Ruiz <borja@libcrack.so>")
print("License: GPL3\n")

if args.version:
    print("{0} version {1}",__file__,  __version__)
    sys.exit(0)

if args.database:
    USERDB = args.database

with open(USERDB, 'rt') as f:
    sig_data = f.read()
signatures = peutils.SignatureDatabase(data=sig_data)

try:
    pe = pefile.PE(args.file)
except:
    logging.error("cannot open file %s" % args.file)

if args.show_all|args.show_matches:
    matches = signatures.match_all(pe, ep_only = True)
else:
    matches = signatures.match(pe, ep_only = True)

print(matches)

if args.show_all:
    print(pe.dump_info())

