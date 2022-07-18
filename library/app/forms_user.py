from django import forms

class BorrowForm(forms.Form):
    dueDate = forms.DateField(input_formats=['%d/%m/%Y'])