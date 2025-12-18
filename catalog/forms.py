from django.forms import ModelForm
from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError

SPAM_WORDS = ['казино',
              'крипта',
              'биржа',
              'дешево',
              'бесплатно',
              'обман',
              'полиция',
              'радар',
              ]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price',]
        #        fields = "__all__" # для вывода всех полей !!Заметка для себя
        exclude = ("views_counter", "owner")  # для фильтрации отмены вывода поля



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            for word in SPAM_WORDS:
                if word in name.lower():
                    raise forms.ValidationError(f"Название содержит запрещённое слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            for word in SPAM_WORDS:
                if word in description.lower():
                    raise forms.ValidationError(f"Описание содержит запрещённое слово: {word}")
        return description

    def clean_purchase_price(self):
        price = self.cleaned_data.get('purchase_price')
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-check-input'})
