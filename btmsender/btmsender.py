from . import validation
from . import transaction


def sender():
    path, account_id, password, output_count = validation.validate_input()
    transaction.handle_input(path, account_id, password, output_count)
