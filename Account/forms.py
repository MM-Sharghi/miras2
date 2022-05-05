from Users.models import Users
from django import forms


class AccountRegisterForms(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','father_name','id_passport','nationality','gender','role','mobile1','marital_status','cityـcode','phone','mobile2','dateـofـbirth','country','state','city','neighbourhood','address','postalـcode','username','password','national_code']
        extra_kwargs = {
            'dateـofـbirth': {'write_only': True},
        }

