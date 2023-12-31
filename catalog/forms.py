from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название содержит запрешённое слово!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название содержит запрешённое слово!')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
