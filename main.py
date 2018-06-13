#!/usr/bin/env python3

import sys
import btmvalidation
import btmtransaction


def main(argv=None):
    if argv is None:
        argv = sys.argv
    path, account_id, password = btmvalidation.validate_input(argv)
    btmtransaction.handle_input(path, account_id, password)


if __name__ == "__main__":
    sys.exit(main())
