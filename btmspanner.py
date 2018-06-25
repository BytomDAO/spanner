#!/usr/bin/env python3

import sys
from btmsender import btmsender

if __name__ == "__main__":
    if sys.argv[1] == 'btmsender':
        sys.argv.pop(1)
        sys.exit(btmsender.sender())
    elif sys.argv[1] == 'utxocombiner':
        sys.argv.pop(1)
        # TODO
    else:
        print("Input error:\n"
              "btmsender usage: btmspanner.py btmsender [-h] -i I -a A -p P [-c C]"
              "utxocombiner usage: btmspanner.py utxocombiner")
        sys.exit(1)
