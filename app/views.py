# -*- coding: utf-8 -*-
import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View


def is_setup():
    return (os.environ.get('CONSUMER_KEY') is not None
            and os.environ.get('CONSUMER_SECRET') is not None)


class IndexView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        if not is_setup():
            return redirect(reverse('app:setup'))

        return render(request, self.template_name)


class SetupView(View):
    template_name = 'app/setup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
