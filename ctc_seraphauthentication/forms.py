from django import forms

class LdapPasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

class LdapSetPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm New password")

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("new_password1") != cleaned_data.get("new_password2"):
            self.add_error('new_password2', "Passwords do not match.")
        return cleaned_data


# class LdapSetPasswordForm(forms.Form):
#     old_password = forms.CharField(widget=forms.PasswordInput, label="Current Password")
#     new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
#     new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm New Password")

#     def clean(self):
#         cleaned_data = super().clean()
#         new_password1 = cleaned_data.get("new_password1")
#         new_password2 = cleaned_data.get("new_password2")

#         if new_password1 != new_password2:
#             raise forms.ValidationError("The new passwords do not match.")
#         return cleaned_data