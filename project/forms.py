from django import forms
from .models import ProductModel


class Product(forms.ModelForm):


	class Meta:
		# specify model to be used
		model = ProductModel

		# specify fields to be used
		fields = [
			"name",
            "price",
            "stock",
            "image",
			
		]
