# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import View


class IndexView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SetupView(View):
    template_name = 'app/setup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
