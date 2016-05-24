from django.conf.urls import *

import paypal.standard.ipn.views

urlpatterns = (
    url(r'^$', paypal.standard.ipn.views.ipn, name="paypal-ipn"),
)
