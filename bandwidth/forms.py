from django import forms
from .models import article,upgrade,author


class downgradeForm(forms.ModelForm):
    class Meta:
        model = article
        fields = [
            
            'pop_name',
            'category',
            'data_show',
            'Existing_Internet',
            'Existing_Facebook',
            'Existing_YouTube',
            'Existing_BDInternet',
            'Upgrade_Internet',
            'Upgrade_Facebook',
            'Upgrade_YouTube',
            'Upgrade_BDInternet',
        ]



class UpdateForm(forms.ModelForm):
    class Meta:
        model = upgrade
        fields = [
            'upgrade_author',
            'AfterUpgrade_Internet',
            'AfterUpgrade_Facebook',
            'AfterUpgrade_YouTube',
            'AfterUpgrade_BDInternet',
        ]

class createAuthor(forms.ModelForm):
    class Meta:
        model = author
        fields = [
            'profile_pic',
            'details',
            'email'
        ]