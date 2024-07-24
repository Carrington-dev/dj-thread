from collections.abc import Callable
from threading import Thread
fro

class EmailThread(Thread):
    def __init__(self, subject, sending_email, order):
        self.subject = subject
        self.sending_email = sending_email
        self.order = order

    def run(self):
        super().run()
