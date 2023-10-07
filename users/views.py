import random

from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        current_site = get_current_site(self.request)
        activation_link = reverse_lazy(
            'users:email_verification', kwargs={'uidb64': uid})
        activation_url = f"{current_site}{activation_link}"
        mail_subject = 'Активация аккаунта'
        massage = render_to_string('users/email_verification.html', {
            'activation_url': activation_url
        })
        user.email_user(mail_subject, massage)

        return super().form_valid(form)


def activate_account(request, uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=int(uid))
        user.is_active = True
        user.save()
        return redirect('users:activation_ok')
    except User.DoesNotExist:
        return redirect('users:activation_failed')


class ActivationOk(TemplateView):
    template_name = 'users/email_verification_done.html'


class ActivationFailed(TemplateView):
    template_name = 'users/email_verification_failed.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Новый пароль',
        message=f"Ваш новый пароль: {new_password}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('catalog:home'))
