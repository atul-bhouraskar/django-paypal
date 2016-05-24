from django.conf.urls import url

import paypal.standard.pdt.views

urlpatterns = (
    url(r'^$', paypal.standard.pdt.views.pdt, name="paypal-pdt"),
)
