#!/usr/bin/env python3

import sys
from btmsender import btmsender
from utxomerger import merge_utxo

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'btmsender':
            sys.argv.pop(1)
            sys.exit(btmsender.sender())
        elif sys.argv[1] == 'utxomerger':
            sys.argv.pop(1)
            sys.exit(merge_utxo.main())
    print("Input error:\n"
          "btmsender usage: spanner.py btmsender [-h] -n NODE_ADDRESS -i INPUT_FILE -a ACCOUNT_ID -p PASSWORD [-c OUTPUT_COUNT]\n"
          "utxomerger usage: spanner.py utxomerger [-h] [-o URL] [-a ACCOUNT_ALIAS] [-p PASSWORD] [-x MAX_AMOUNT] [-s MIN_AMOUNT] [-l] [-m MERGE_LIST] [-y]")
    sys.exit(1)
