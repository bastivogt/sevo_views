from django import forms

from . import models


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = "__all__"