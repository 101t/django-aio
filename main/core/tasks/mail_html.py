from typing import List

from django.conf import settings
from django.utils import translation

from config.celery import app
from main.core.mailer import PyMailMultiPart


@app.task(bind=True, default_retry_delay=3, max_retries=3)
def mail_html_mails(
        self, mails: List[str], subject: str, html_template: str, kwargs: dict, lang: str = settings.LANGUAGE_CODE):
    """
    kwargs = {
        user      : {"username": "joe_user", "email": "joe@gmail.com", "name": "Joe Life"},
        site_name : "Company Name",
        logo_url  : "http://www.example.com/logo.png",
        site_url  : "http://www.example.com",
        logo      : f'<img data-imagetype="External" alt="{logo_url}" src="{logo_url}" height="100">'
    }
    """
    translation.activate(lang)
    mail = PyMailMultiPart(subject=subject, html_template=html_template, )
    mail.send(mails=mails, kwargs=kwargs)


@app.task(bind=True, default_retry_delay=3, max_retries=3)
def mail_html_envelopes(
        self, envelopes: List[str], subject: str, html_template: str, lang: str = settings.LANGUAGE_CODE):
    """
    e.g. envelopes = {"name": "Joe Life", "email": "info@domain.com", "kwargs": "Dictionary of extra"}
    """
    translation.activate(lang)
    mail = PyMailMultiPart(subject=subject, html_template=html_template, )
    mail.send_envelopes(envelopes=envelopes)
