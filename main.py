#!/usr/bin/env python3

import sys
import btmvalidation
import btmtransaction


def main():
    path, account_id, password, output_count = btmvalidation.validate_input()
    btmtransaction.handle_input(path, account_id, password, output_count)


if __name__ == "__main__":
    sys.exit(main())
