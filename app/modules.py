from django.shortcuts import render
from django.http import HttpResponse
from app.models import User, Email
import imaplib
import email
from email.header import decode_header


class Spam:
    def add_mail(self, request):
        if request == request.POST:
            try:
                email = request.POST.get('email')
                password = request.POST.get('password')
                frequence = request.POST.get('frequence')
                email_password = request.get('email_password')
                add_mail = Email(email=email, password=password, frequence=frequence)
                add_mail.add()
                add_mail.save()
                return HttpResponse('Email added!!')

            except:
                return HttpResponse('ADD ERROR!!')


    def delete_email(self, request, id_user):
        msg = "Views2"
        user = User.objects.get(id=id_user)
        email = user.user_email
        email_password = user.email_password

        try:
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            # authentification
            imap.login(email, email_password)

            # On veut supprimer les spams
            imap.select("SPAM")
            # Obtenir les objet emails
            status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')

            # convertir les messages en listes
            messages = messages[0].split(b' ')
            for mail in messages:
                _, msg = imap.fetch(mail, "(RFC822)")

            for response in msg:

                if isinstance(response, tuple):

                    msg = email.message_from_bytes(response[1])

                    subject = decode_header(msg["Subject"])[0][0]

                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    print("Deleting", subject)

            # mark the mail as deleted
            imap.store(mail, "+FLAGS", "\\Deleted")

            imap.expunge()
            # fermer box email
            imap.close()
            # se deconnecter
            imap.logout()
        except:
            return HttpResponse('ERROR')
