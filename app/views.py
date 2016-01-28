# -*- coding: utf-8 -*-
import os

from logging import getLogger, StreamHandler, DEBUG

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from simple_salesforce import Salesforce

from .auth import SalesforceOAuth2

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

REDIRECT_URI = 'http://localhost:5000'


def is_setup():
    return (os.environ.get('CONSUMER_KEY') is not None
            and os.environ.get('CONSUMER_SECRET') is not None)


class IndexView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        if not is_setup():
            return redirect(reverse('app:setup'))

        connection = SalesforceOAuth2(
                client_id=os.environ.get('CONSUMER_KEY'),
                client_secret=os.environ.get('CONSUMER_SECRET'),
                redirect_uri=REDIRECT_URI)

        if 'code' in request.GET:
            res = connection.get_token(request.GET['code'])
            for k, v in res.items():
                logger.debug('%s: %r' % (k, v))

            sf = Salesforce(
                    instance_url=res['instance_url'],
                    session_id=res['access_token'])
            res = sf.query('SELECT id, name, type, industry, rating FROM Account')
            records = res['records']
            return render(request, self.template_name, {'records': records})
        else:
            auth_url = connection.authorize_url(scope='full')
            logger.debug('redirect to: {}'.format(auth_url))
            return redirect(auth_url)


class SetupView(View):
    template_name = 'app/setup.html'

    def get(self, request, *args, **kwargs):
        if is_setup():
            return redirect(reverse('app:index'))

        return render(request, self.template_name)
