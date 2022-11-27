import gzip
import imaplib
import shutil
import sys
from email.header import decode_header
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect

from app.forms import AddMailForm
from app.models import User, Email, File
from app.views import UserView

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import cv2


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


class CompressorModule:
    def add_file(self, request):

        if request.method == 'POST':
            msg = ''
            file = File()
            file.file = request.FILES['file']
            filename = file.file
            file.save()
            filename = f'app/media/{str(filename)}'

            filename_out = f"{filename}.giz.tar"

            with open(filename, "rb") as fin, gzip.open(filename_out, "wb") as fout:
                shutil.copyfileobj(fin, fout)

            # print(f"Uncompressed size: {os.stat(filename_in).st_size}")
            # print(f"Compressed size: {os.stat(filename_out).st_size}")

            with gzip.open(filename_out, "rb") as fin:
                data = fin.read()
                ##Aficher la taille du fichier Decompresser
                print(f"Decompressed size: {sys.getsizeof(data)}")
            filename = filename_out.split('/')[-1]
            return FileResponse(open(filename_out, 'rb'), as_attachment=True)
        else:
            return render(request, 'modules/compressor/compressor.html', locals())

    def app(self, request):
        filename_in = "teste"
        filename_out = "compressed_data.tar.gz"

        with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
            shutil.copyfileobj(fin, fout)

        # print(f"Uncompressed size: {os.stat(filename_in).st_size}")
        # print(f"Compressed size: {os.stat(filename_out).st_size}")

        with gzip.open(filename_out, "rb") as fin:
            data = fin.read()
            # Aficher la taille du fichier Decompresser
            print(f"Decompressed size: {sys.getsizeof(data)}")


class Scrapping:

    def __init__(self, origine, destination):
        self.origine = origine
        self.destination = destination

        # def isConnected():
        # eturn requests.get(env.get("LINK")).status_code == 200

    def scrap(self):
        browser = webdriver.Firefox()
        browser.get('https://maps.google.com')

        element_input_lieu = browser.find_element(By.ID, "searchboxinput")
        element_input_lieu.send_keys(self.origine)
        element_input_lieu.send_keys(Keys.ENTER)

        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button"
                    )
                )
            )
            itenerary_button = browser.find_element(
                By.XPATH,
                '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button'
            )
            itenerary_button.click()

            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located(
                    (
                        By.XPATH,
                        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"
                    )
                )
            )
            element_input_lieu = browser.find_element(
                By.XPATH,
                "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"
            )
            element_input_lieu.send_keys(self.destination)
            element_input_lieu.send_keys(Keys.ENTER)
            sleep(10)
            from Peaky_Coders.settings import BASE_DIR
            image_name = f'{self.origine}.png'
            browser.save_screenshot(image_name)

            image = cv2.imread(image_name)
            shape = image.shape
            w = image.shape[0]
            h = image.shape[1]
            print(shape)
            cropped_image = image[80:w - 80, int((h / 2)) - 50:int((h) - 50)]
            shape = cropped_image.shape
            print(shape)


            cv2.imwrite(f"app/{self.origine}_cropped.png", cropped_image)
            
            file = f"app/{self.origine}_cropped.png"
            return FileResponse(open(file, 'rb'), as_attachment=True)
        except:
            pass

        browser.close()


class BinModule:
    def bin(self, request):
        if request.method == 'POST':
            origine = request.POST['place']
            destination = "wc public"
            execute = Scrapping(origine, destination)
            execute.scrap()
            name = str(origine + destination)
            from Peaky_Coders.settings import BASE_DIR
            image = '{}.png'.format(origine)

            return render(request, 'pages/bin.html', locals())
        else:
            return HttpResponse('Une Erreur est survenue')
