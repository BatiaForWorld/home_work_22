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
        #        fields = "__all__" # для вывода всех полей !!Заметка для себя
        exclude = ("views_counter",)  # для фильтрации отмены вывода поля

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Добавьте фото товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию товара'
        })

        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость товара'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name:
            name_lower = name.lower()
            for word in SPAM_WORDS:
                if word in name_lower:
                    raise forms.ValidationError(
                        f"Название товара не должно содержать запрещенное слово: '{word}'."
                    )

        if description:
            description_lower = description.lower()
            for word in SPAM_WORDS:
                if word in description_lower:
                    raise forms.ValidationError(
                        f"Описание товара не должно содержать запрещенное слово: '{word}'."
                    )
        return cleaned_data

    def clean_purchase_price(self):
        price = self.cleaned_data.get('purchase_price')

        if price < 0:
            raise forms.ValidationError(
                "Цена продукта не может быть отрицательной. Введите корректное значение."
            )
        return price
