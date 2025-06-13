from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(next_page=reverse_lazy('ctc_home')), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

