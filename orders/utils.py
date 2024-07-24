from uuid import uuid4


length = 128


def order_number_generator():
    return str(uuid4())[20:]