from django.shortcuts import render, redirect
from django.http import HttpResponse
import imaplib
from email.header import decode_header
from app.models import User, Email
from app.views import UserView
from app.forms import AddMailForm


class EmailModule:
    def home(self, request):
        user_id = UserView().check_session(request)
        user = User.objects.get(id=user_id)
        email = Email.objects.filter(user=user.id)

        return render(request, 'modules/email/email.html', locals())

    def add_mail(self, request):
        if request.method == 'POST':
            form = AddMailForm(request.POST)
            email = Email()

            email.user = request.POST['user_id']
            email.email = request.POST['email']
            email.password = password = request.POST['password']
            email.frequence = frequence = request.POST['frequence']
            email.memethod = method = request.POST['method']

            value = request.POST['value']

            email.save()
            success_msg = 'Mail Ajouté'
            return redirect('home')
        user_id = request.GET['user_id']
        return render(request, 'forms/add_email.html', locals())

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

    def delete_email_list(self):
        return HttpResponse('you are deleting this')