from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from django.conf.urls.static import static
from authentication import views as auth_views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", auth_views.register, name="register"),
    path("login/", auth_views.login_view, name="login"),
    path("logout/", auth_views.logout_view, name="logout"),
    path("dashboard/", auth_views.dashboard, name="dashboard"),
    path('', include('ol_app.urls')),
    path("", lambda request: redirect('login'), name="home"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
