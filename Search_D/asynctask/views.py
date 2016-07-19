from django.shortcuts import render
from django.http import HttpResponse
from asynctask.email_config import *
from django.core.mail import EmailMultiAlternatives
from search.settings import EMAIL_HOST_USER
from threading import Thread
import urllib
import pycurl
try:
    import StringIO
except ImportError:
    from io import StringIO

def async_task_req(request):
    action = request.POST['action'] if 'action' in request.POST else None
    if not action:
        return HttpResponse("")
    print '--------------->', action
    if action == 'send_mail':
        subject = request.POST['subject']
        body = request.POST['body']
        email = request.POST['email']
        print 'Starting email thread'
        t = Thread(target=email_thread, args=(subject, body, email))
        t.start()
        return HttpResponse("")
    elif action == 'send_sms':
        sms_content = request.POST['message']
        phone_no = request.POST['phone_no']
        print 'Starting sms thread'
        t = Thread(target=send_sms, args=(phone_no, sms_content))
        t.start()
        return HttpResponse("")
    elif action == 'leadsquare':
        return HttpResponse("")

class ShootMail():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def shoot_email(self):
        #html_content = EMAIL['header'] + self.kwargs['body'] + EMAIL['footer']
        html_content = self.kwargs['body']
        msg = EmailMultiAlternatives(self.kwargs['subject'], html_content, EMAIL_HOST_USER, \
                [self.kwargs['email']])
        if 'attachment' in self.kwargs:
            msg.attach_file(self.kwargs['attachment'])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

def send_sms(phone_no_customer, text):
    """ Method to send Sms using sms gateway """
    print 'sending sms to ', phone_no_customer
    text = urllib.quote_plus(text)
    sms_url = 'http://23.254.128.22:9080/urldreamclient/dreamurl?userName=sup_tech&password=supTech123&clientid=supTedst29&to=%s&text=%s&Senderid=SUPTRX'%(str(phone_no_customer), str(text))
    buffer = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, sms_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()

def email_thread(subject, body, email):
    print 'Shooting email to: ', email
    ShootMail(**{
            'subject': subject,
            'body': body,
            'email': email,
        }).shoot_email()
