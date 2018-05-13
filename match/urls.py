from django.urls import path, re_path

from .views import IndexView, SearchResultsView

urlpatterns = [
    path('', IndexView.as_view()),
    re_path(r'^results/(?P<q_id>\d+)/$', SearchResultsView.as_view())
]
