from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import render
from aiarena.core.models import Bot
from aiarena.core.models import Result


class BotUpload(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    redirect_field_name = 'next'
    template_name = 'botupload.html'
    success_message = "Bot was uploaded successfully"

    model = Bot
    fields = ['name', 'bot_zip', 'plays_race', 'type']

    def get_login_url(self):
        return reverse('login')

    def get_success_url(self):
        return reverse('botupload')

    def get_form_kwargs(self):
        # set the bot's user
        kwargs = super(BotUpload, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Bot()
        kwargs['instance'].user = self.request.user
        return kwargs


class Ranking(CreateView):
    def get(self, request):
        bot_ranking = Bot.objects.filter(active=1).order_by('-elo')
        context = {'bot_ranking': bot_ranking}
        return render(request, 'ranking.html', context)


class Results(CreateView):
    def get(self, request):
        results = Result.objects.all().order_by('-match_id')[:100]
        context = {'results': results}
        return render(request, 'results.html', context)
