from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from app_main.models import Product
from app_main.forms import ProductForm


def home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")

    products = Product.objects.all()

    data = {
        "products": products,
    }

    return render(
        request=request,
        template_name="home_page.html",
        context=data
    )


def login_page(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request=request, template_name="login_page.html")


def profile_page(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request=request, template_name="profile_page.html")


def services_page(request):
    return render(request=request, template_name="services_page.html")


def contacts_page(request):
    return render(request=request, template_name="contacts_page.html")


def authorize(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    # Userni aniqlash kerak
    user = authenticate(username=username, password=password)

    if user:  # if user is not None
        # Agar bor bo'lsa, session id hosil qilish va asosiy sahifaga yo'naltirish
        login(request=request, user=user)
        return redirect("index")

    else:
        # Agar yo'q bo'lsa, unda login sahifaga qayta yo'natirish kerak
        return redirect(to="login")


def user_logout(request):
    logout(request=request)
    return redirect("login")


def registration_page(request):
    return render(request, "registration.html")


def register_user(request):

    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")

    if password1 != password2:
        return redirect("registration")

    user_exists = User.objects.filter(username=username).exists()

    if user_exists:  # if user_exists == True
        return redirect("registration")

    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
    )

    user.set_password(raw_password=password2)
    user.save()

    return redirect("login")


def add_product(request):
    if request.method == "POST":
        # Forma yaratish va uni ichini frontend dan kelgan ma'lumotlar bilan to'ldirish
        form = ProductForm(request.POST)

        # Frontenddan kelgan ma'lumotlar model kriteriyalariga mos kelishini tekshirish
        if form.is_valid():
            product = form.save(commit=False) # Formani saqlash, lekin natijada hosil bo'ladigan yangi maxsulot obyektini bazaga yozmaslik
            product.owner = request.user      # Yangi hosil bo'lgan maxsulot obyektiga owner sohasini qo'shib yuborish
            product.save()                    # Maxsulot obyektini saqlash va endi haqiqatdan bazaga saqlash

            # Bosh sahifaga yo'naltirish
            return redirect("index")

        return render(request, "add_product.html", {"form": form})

    # Bo'sh forma hosil qilish (frontend da chizib ko'rsatish uchun)
    form = ProductForm()
    return render(request, "add_product.html", {"form": form})


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user != product.owner:
        return redirect("index")


    if request.method == "POST":
        name = request.POST.get("name")  # { "name": "Macbook Pro M4", "price": 2000 }
        price = request.POST.get("price")
        image = request.POST.get("image")

        product.name = name
        product.price = price

        if image:
            product.image = image

        product.save()
        return redirect("index")

    data = {
        "product": product
    }
    return render(request, "edit_product.html", context=data)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user != product.owner:
        return redirect("index")

    product.delete()
    return redirect('index')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    data = {
        "product": product,
    }

    return render(request, "product_detail.html", context=data)
