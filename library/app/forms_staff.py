from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BookForm(forms.ModelForm):
    numberOfAvailableCopy = forms.IntegerField(required=False, widget=forms.HiddenInput)
    description = forms.CharField(required=False, label='Mô tả', widget=forms.Textarea)
    class Meta:
        model = Book
        fields = '__all__'

    def clean_numberOfAvailableCopy(self):
        if not self.instance.id:
            return self.cleaned_data['numberOfCopy']

        return self.cleaned_data['numberOfAvailableCopy']