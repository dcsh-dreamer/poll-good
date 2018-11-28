from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import *

## Create your views here.
## 投票主題列表
class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        context['options'] = options
        return context

class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id=self.kwargs['pk'])
        option.count += 1
        option.save()
        return '/poll/' + str(option.poll_id) + '/'

class PollCreate(CreateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    template_name = 'form.html'

class PollUpdate(UpdateView):
    model = Poll
    fields = ['subject']
    success_url = '/poll/'
    template_name = 'form.html'

class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    template_name = 'form.html'

    def get_success_url(self):
        return '/poll/'+str(self.kwargs['pid'])+'/'

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)

class OptionUpdate(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'form.html'

    def get_success_url(self):
        return '/poll/'+str(self.object.poll_id)+'/'

class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'
    template_name = 'confirm_delete.html'

class OptionDelete(DeleteView):
    model = Option
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll_id})
        # return '/poll/' + str(self.object.poll_id) + '/'

