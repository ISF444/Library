from django.contrib.auth import views
from django.urls import path

from .views import book_regis_get, readers_regis_get

urlpatterns = [
    path('', book_regis_get),
    path('new_readers/',  readers_regis_get),
#    path('login/', views.LoginVies.as_viev(), name='login'),
#    path('logout/', views.LogoutVies.as_viev(), name='logout'),
#    path('password-change/', views.PasswordChangeView(), name='password_change'),
#    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#    path('password-reset/', views.PasswordResetViev.as_view(), name='password_reset'),
#    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
