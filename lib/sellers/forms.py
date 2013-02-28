from django import forms

from solitude.fields import URLField

from .models import Seller, SellerPaypal, SellerProduct


class SellerValidation(forms.ModelForm):

    class Meta:
        model = Seller


class SellerPaypalValidation(forms.ModelForm):

    class Meta:
        model = SellerPaypal
        exclude = ['seller', 'token', 'secret']


class SellerProductValidation(forms.ModelForm):
    seller = URLField(to='lib.sellers.resources.SellerResource')

    class Meta:
        model = SellerProduct
