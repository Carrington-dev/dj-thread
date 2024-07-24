from email.message import EmailMessage
from threading import Thread

from django.shortcuts import get_object_or_404
from django import template
from django.http import HttpResponse
from django.core.mail import BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.utils.safestring import mark_safe

from orders.models import Order
from django.core.mail import send_mail

import threading

class EmailThread(threading.Thread):
    def __init__(self, data, sender_email):
        self.sender_email = sender_email
        self.data = data
        threading.Thread.__init__(self)

    def run(self):
        order_started('', data=self.data, sender_email=self.sender_email)


def order_started(url, data, sender_email):
    order = get_object_or_404(Order, id=data['id'])
    subject = f'Stemgon Reg Number: #{order.order_number}'
    link = mark_safe(f'<a href="{url}">click here</a>')
    message = mark_safe(f'Dear { order.first_name } { order.last_name },.\n\nCongratulations on your successful purchase with Stemgon!\n\nIf you have not paid for this order, { link } to pay. If payment is not processed within 4 hour(s), the order will be cancelled automatically.')
    # email = EmailMessage(subject, message, sender_email, [order.email])
    # email.send()

    send_mail(
        subject,
        message,
        sender_email, 
        [order.email],
        fail_silently=False,
    )
    print("Here")
