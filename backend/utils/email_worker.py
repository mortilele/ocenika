import threading

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string


class EmailThread(threading.Thread):
    def __init__(self, subject, email, token, user_id, message, kwargs):
        self.subject = subject
        self.email = email
        self.token = token
        self.user_id = user_id
        self.message = message
        self.kwargs = kwargs
        threading.Thread.__init__(self)

    def run(self):
        send_mail(self.subject,
                  self.message,
                  settings.FROM_EMAIL,
                  [self.email],
                  html_message=render_to_string('emails/send_email.html',
                                                {'base_url': settings.BACKEND_URL,
                                                 'user_id': self.user_id,
                                                 'token': self.token}),
                  **self.kwargs)
