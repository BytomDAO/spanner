#!/usr/bin/env python3

import sys
from btmsender import btmsender
from utxomerger import merge_utxo

if __name__ == "__main__":
    if sys.argv[1] == 'btmsender':
        sys.argv.pop(1)
        sys.exit(btmsender.sender())
    elif sys.argv[1] == 'utxomerger':
        sys.argv.pop(1)
        sys.exit(merge_utxo.main())
    else:
        print("Input error:\n"
              "btmsender usage: btmspanner.py btmsender [-h] -i I -a A -p P [-c C]"
              "utxomerger usage: btmspanner.py utxomerger [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD] [-x MAX_AMOUNT] [-s MIN_AMOUNT] [-l] [-m MERGE_LIST] [-y]")
        sys.exit(1)
