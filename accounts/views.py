from django.shortcuts import redirect, HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import SignUpForm
from django.contrib.auth import login


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    redirect_authenticated_user = True      # didin't work
    success_url = reverse_lazy('resident_app:home')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    
    def get(self, *args, **kwargs):     # an already logged in user will be redirected
        if self.request.user.is_authenticated:
            return redirect('resident_app:home')
        return super(RegisterView, self).get(*args, **kwargs)
    

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    fields = '__all__'
    redirect_authenticated_user = True   # an already logged in user will be redirected

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('resident_app:home')


def index(request):
    return HttpResponse('worked!')


@login_required(login_url='accounts_app:login')
def test_restricted_view(request):
    return HttpResponse('this is restricted view')