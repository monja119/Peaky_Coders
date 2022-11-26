from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from app.models import User
from app.forms import UserForm


class Tabs:
    def home(self, request):
        msg = "Views1"
        return render(request, 'tabs/home.html', locals())

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
                if user.password == user_password:
                    user_id = User.id
                    self.set_session(user.id)
                    msg = f'this user is {user.first_name} and has {user.id} id'
                else:
                    return HttpResponse('Mot de passe incorrecte')

                return HttpResponse(msg)
            except User.DoesNotExist:
                return HttpResponse("User doesn't match any account")
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
                    return render(request, 'forms/register.html', locals())
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
                    return redirect(Page().home)
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

    def check_session(self, id):
        session = None
        try:
            session = request.session['id']
        except KeyError:
            session = None
        return session

    def logout(self, request, id):
        try:
            del request.session['id']
        except:
            pass
        return HttpResponse(f'logged out {id}')
