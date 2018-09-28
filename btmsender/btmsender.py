from . import validation
from . import transaction


def sender():
    path, account_id, password, output_count, use_unconfirmed, time_range = validation.validate_input()
    transaction.handle_input(path, account_id, password, output_count, use_unconfirmed, time_range)
