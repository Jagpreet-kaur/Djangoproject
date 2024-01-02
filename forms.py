# dashboard/forms.py
from django import forms
from .models import DashboardItem

class DashboardItemForm(forms.ModelForm):
    class Meta:
        model = DashboardItem
        fields = ['category', 'title', 'image', 'description', 'url']
