"""
URL configuration for hotelbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("blog/",views.blog,name="blog"),
    path("contact/",views.contact,name="contact"),
    path("gallery/",views.gallery,name="gallery"),
    path("room/",views.room,name="room"),
    path("register/",views.register,name="register"),
    path("accounts/login/",views.login_page,name="login"),
    path("logout/",views.logout,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("edit/",views.edit,name="edit"),
    path("logindata/",views.logindata,name="logindata"),
    path("admindata/",views.admindata,name="admindata"),
    path("profiledata/",views.profiledata,name="profiledata"),
    path("logoutdata/",views.logindata,name="logoutdata"),
    # path("add_admin/",views.add_admin,name="add_admin"),
    path("roomdata/",views.roomdata,name="roomdata"),
    path("user/",views.user,name="user"),
    path("booking/",views.booking,name="booking"),
    path("feedback/",views.feedback,name="feedback"),
    path("roomdetail<int:id>/",views.roomdetail,name="roomdetail"),
    path("peyment/",views.peyment,name="peyment"),
    path("booking_edit/<int:id>/", views.booking_edit, name="booking_edit"),
    path("delete_booking/<int:id>/", views.booking_delete, name="delete_booking"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
