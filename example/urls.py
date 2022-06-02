from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.utils.translation import gettext as _

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils import timezone
from django.shortcuts import redirect

import pytz  # импортируем стандартный модуль для работы с часовыми поясами

class Index(View):
    def get(self, request):
        curent_time = timezone.now()
        string = _('Hello world')
        # return HttpResponse(string)
        context = {
            'string': string,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }
        return HttpResponse(render(request, 'index.html', context))

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', Index.as_view()),]
