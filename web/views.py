# from click import confirm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
# from rest_framework.response import Response
# from .serializer import UserDetailsSerializers
# from rest_framework.viewsets import GenericViewSet
# from rest_framework import mixins
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from web.models import Product, Category, SubCategory


# class UserDetailsSerializers(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,
#                              mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = UserDetailsSerializers
#     queryset = UserDetails.objects.all()

# def list(self, request, *args, **kwargs):
#     serializer = self.get_serializer(self.queryset, many=True)
#     return Response(serializer.data)


# Create your views here.
def IndexView(request):
    queryset = Category.objects.all()

    return render(request, "index.html", {'category': queryset})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        if password != confirm_password:
            messages.info(request, "Password and Conform Password are Not Same")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "User Name Already Exist")
                return redirect('/signup')

        except Exception as e:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email Already Exist")
                return redirect('/signup')

        except Exception as e:
            pass

        my_user = User.objects.create_user(first_name, last_name, password)
        my_user.save()
        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        new_user = authenticate(username=username, password=password)

        if new_user is not None:
            return IndexView(request)

        else:
            messages.error(request, "wrong information")
            return redirect("index")

    return render(request, "signin.html")


def SignOut(request):
    logout(request)
    messages.success(request, "logged Out!")
    return redirect("index")


def all_product(request):
    all_products = Product.objects.all()
    return render(request, "product.html", {'product': all_products})


def category(request, id):
    queryset = SubCategory.objects.filter(category=id)
    return render(request, "subcategory.html", {'subcategory': queryset})


def subcategory(request, id):
    queryset = Product.objects.filter(subcategory=id)
    return render(request, "product.html", {'category': queryset})
