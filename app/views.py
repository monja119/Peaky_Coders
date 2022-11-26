from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.hashers import make_password, check_password
from app.models import *
from app.forms import UserForm


class Tabs:
    def home(self, request):
        msg = "Views1"
        if UserView().check_session is not None:
            session = UserView().check_session(request)
        else:
            session = None

        return render(request, 'tabs/home.html', locals())

    def base(self, request):
        msg = "Views2"
        return render(request, 'tabs/base.html', locals())

    def data(self, request):
        msg = "Views1"
        return render(request, 'tabs/data.html', locals())

    def recyclage(self, request):
        msg = "Views2"
        return render(request, 'tabs/recyclage.html', locals())

    def bin(self, request):
        msg = "Views3"
        return render(request, 'tabs/bin.html', locals())

    def extra(self, request):
        msg = "Views4"  # 591583
        return render(request, 'tabs/extra.html', locals())


class UserView:
    def login(self, request):
        if request.method == 'POST':
            user_email = request.POST['email']
            user_password = request.POST['password']
            user_remember = request.POST.get('remember')
            try:
                user = User.objects.get(email=user_email)
                if check_password(user_password, user.password):
                    user_id = user.id
                    request.session['id'] = user_id
                    session = self.check_session(request)
                    success_msg = 'Vous êtes connecté'
                    return render(request, 'tabs/base.html', locals())
                else:
                    error_msg = 'Mot de passe incorrect'
                    return render(request, 'tabs/base.html', locals())

            except User.DoesNotExist:
                error_msg = 'Identifiant non identifié'
                return render(request, 'tabs/base.html', locals())
        else:
            return render(request, 'forms/login.html', locals())

    def register(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = User()
            msg, error_msg = '', ''
            # auth
            email, password, retype_password = form.cleaned_data['email'], \
                                               form.cleaned_data['password'], \
                                               request.POST['retype_password']

            # verification si les deux mots de passe sont les même
            if password != retype_password:
                error_msg = 'les deux mots de passe ne sont pas les même'
                return render(request, 'forms/register.html', locals())
            else:
                # ajout à la base de données

                try:
                    User.objects.get(email=email)
                    error_msg = 'Email déjà utilisé par un autre utilisateur'
                    return render(request, 'tabs/errors.html', locals())
                except User.DoesNotExist:
                    # about
                    form.save()
                    user.first_name, user.last_name = form.cleaned_data['first_name'], form.cleaned_data['last_name']
                    user.gender = form.cleaned_data['gender']

                    # contact
                    user.address = form.cleaned_data['address']
                    user.tel = form.cleaned_data['tel']
                    user.email = form.cleaned_data['email']

                    user.picture = form.cleaned_data['picture']
                    user.password = make_password(password, None, 'default')

                    user.save()

                    success_msg = 'Création de compte avec succès'
                    return render(request, 'tabs/home.html', locals())
        else:
            return render(request, 'forms/register.html', locals())

    def get_user(self, request, id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None

    def delete(self, request, id):
        return HttpResponse(f'deleted user {id}')

    def set_session(self, id):
        try:
            request.session['id'] = id
            return 0
        except:
            return -1

    def check_session(self, request):
        session = None
        try:
            session = request.session['id']
        except KeyError:
            session = None
        return session

    def logout(self, request):
        try:
            del request.session['id']
        except:
            pass
        success_msg = 'Vous êtes deconnectés'
        return redirect('data')


class Recycle:
    def share(self, request):
        recycle = Recyclage.objects.all()
        return render(request, 'pages/share_recycle.html', locals())

    def view(self, request):
        if request.method == 'GET':
            try:
                id = int(request.GET['id'])
                recycle = Recyclage.objects.get(id=id)
                return render(request, 'pages/view_recycle.html', locals())
            except KeyError:
                return HttpResponse('Recyclage non trouvé')

    def question(self, request):
        question = Question.objects.all()
        return render(request, 'pages/questions_recycle.html', locals())

    def new_question(self, request):
        if request.method == 'POST':
            question = Question()
            question.email = request.POST['email']
            question.objet = request.POST['objet']
            question.question = request.POST['question']

            question.save()
            return redirect('home')
        else:
            return HttpResponse('new question')

    def view_question(self, request):
        try:
            id = int(request.GET['id'])
            question = Question.objects.get(id=id)
            return render(request, 'pages/view_question.html', locals())

        except:
            return HttpResponse('Question non trouvé')

    def answer_question(self, request):
        if request.method == 'POST':
            answer = Answer()
            answer.email = request.POST['email']
            answer.question_id = request.POST['question_id']
            answer.content = request.POST['answer']

            answer.save()

            return HttpResponse('Question répondue')

        else:
            error_msg = 'Une Erreur survenue'
            render(request, 'tabs/errors.html', locals())
    def new_recycle(self, request):
        if request.method == 'POST':
            recycle = Recyclage()
            recycle.email = request.POST['email']
            recycle.title = request.POST['title']
            recycle.content = request.POST['content']

            recycle.save()

            return redirect('home')
        else:
            return render(request, 'forms/new_recycle.html', locals())
