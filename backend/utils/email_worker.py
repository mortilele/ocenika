import threading

from django.conf import settings
from django.core.mail import send_mail

from utils import constants


class EmailThread(threading.Thread):
    def __init__(self, subject, email, html_message, kwargs):
        threading.Thread.__init__(self)
        self.subject = subject
        self.email = email
        self.html_message = html_message
        self.kwargs = kwargs

    def run(self):
        send_mail(subject=self.subject,
                  message=constants.OCENIKA,
                  from_email=settings.FROM_EMAIL,
                  recipient_list=[self.email],
                  html_message=self.html_message,
                  **self.kwargs)
