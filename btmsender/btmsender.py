from . import validation
from . import transaction


def sender():
    node_address, file_path, account_id, password, output_count, use_unconfirmed, time_range = validation.validate_input()
    btmsender = \
        transaction.BTMSender(node_address, file_path, account_id, password, output_count, use_unconfirmed, time_range)
    btmsender.handle_input()
