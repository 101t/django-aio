from django import forms
from django.core.validators import validate_email
from django.contrib.auth import get_user_model


class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "mobile", "address",]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        if validate_email(value=email) and email != self.instance.email:
            self.instance.is_email = False
            self.instance.save()
        return cleaned_data
