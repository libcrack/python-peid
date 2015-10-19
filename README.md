# Python PEiD


### Description

Python wrapper over [pefile](https://github.com/erocarrera/pefile) implementing
similar functionalities as the ones shipped with PEiD.


### Dependencies

- Python 2.7+: pefile, argparse, logging


### Usage

```text
usage: peid.py [-h] [-a] [-d DB] [-m] [-v] -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             show all PE info
  -d DB, --database DB  signature database file
  -m, --matches         show all signature matches
  -v, --version         show version number
  -f FILE, --file FILE  target PE file
```

