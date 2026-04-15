from django.forms import ModelForm

from app_main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "image"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update({"class": "form-control"})
