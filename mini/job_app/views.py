from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_str, force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage, send_mail
from mini import settings
from .tokens import generate_token
from .models import application
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            return redirect('signup')

        if pass1 != pass2:
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()

        subject = 'Welcome to SRH - JOB Login!!'
        message = 'Hello' + myuser.username + '!! \n' + 'Welcome to SRH!! \n Thank you for visiting our website \n we also send you a conformation email,please conform your email address in order to activate your account. \n\n Thanking you \n Sreehari'
        from_email = settings.EMAIL_HOST_USER
        to_list = {myuser.email}
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ SRH - JOB Login!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('signin')

    return render(request, 'signup.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        return redirect('signin')
    else:
        return render(request, 'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return redirect('apply')

        else:
            return redirect('signin')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')


class joblist(ListView):
    model = application
    context_object_name = 'apply'
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apply'] = context['apply'].filter(user=self.request.user)

        return context


class create(CreateView):
    model = application
    fields = ['profile', 'name', 'email', 'phone', 'address', 'college', 'qualification', 'company', 'skill', 'resume']
    success_url = reverse_lazy('apply')
    template_name = 'profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(create, self).form_valid(form)


class Update(UpdateView):
    model = application
    fields = ['profile', 'name', 'email', 'phone', 'address', 'college', 'qualification', 'company', 'skill', 'resume']
    success_url = reverse_lazy('apply')
    template_name = 'profile.html'


class Delete(DeleteView):
    model = application
    context_object_name = 'apply'
    success_url = reverse_lazy('apply')
    template_name = 'delete.html'


class form(DetailView):
    model = application
    fields = '__all__'
    success_url = reverse_lazy('apply')
    template_name = 'detail.html'
