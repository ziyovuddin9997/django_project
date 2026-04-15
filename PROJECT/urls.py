from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home_page, name='index'),
    path("signin/", views.login_page, name='login'),
    path("signup/", views.registration_page, name='registration'),
    path("register-user/", views.register_user, name='register'),
    path("profile/", views.profile_page, name='profile'),
    path("services/", views.services_page, name='services'),
    path("contacts/", views.contacts_page, name='contacts'),

    path("authorize/", views.authorize, name='authorize'),
    path("logout/", views.user_logout, name='logout'),

    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
]


urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
