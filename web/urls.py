from rest_framework import routers
from django.urls import path

from web import views


router = routers.SimpleRouter()


urlpatterns = [
    path("", views.IndexView, name='index'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("signout", views.SignOut, name='signout'),
    path("all-product", views.all_product, name="all-product"),
    path('category/<int:id>/', views.category, name='category'),
    path('subcategory/<int:id>/', views.subcategory, name='subcategory'),


]+router.urls



