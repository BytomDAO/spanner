#!/usr/bin/env python3

import sys
import validation
import transaction


def main():
    path, account_id, password, output_count = validation.validate_input()
    transaction.handle_input(path, account_id, password, output_count)


if __name__ == "__main__":
    sys.exit(main())
