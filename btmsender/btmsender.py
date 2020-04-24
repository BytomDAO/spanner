from . import validation
from . import transaction


def sender():
    _input = validation.validate_input()
    btmsender = transaction.BTMSender(_input)
    btmsender.handle_input()
