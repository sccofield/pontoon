from __future__ import absolute_import

from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # In-context demo
    url(
        r'^in-context/$',
        views.in_context,
        name='pontoon.in_context',
    ),

    # Legacy: Redirect to /in-context
    url(
        r'^intro/$',
        RedirectView.as_view(pattern_name='pontoon.in_context', permanent=True),
    ),
]
