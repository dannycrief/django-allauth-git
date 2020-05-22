from django.shortcuts import render
from django.views.generic import FormView
from common.forms import ProfileCreationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        try:
            context['github_url'] = SocialAccount.objects.get(
                provider='github',
                user=request.user
            ).extra_data['html_url']
        except:
            context['github_url'] = ''
    return render(request, 'index.html', context)


class CreateUserProfile(FormView):
    form_class = ProfileCreationForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('common:index')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(CreateUserProfile, self).form_valid(form)
