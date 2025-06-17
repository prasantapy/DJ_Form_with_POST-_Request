from django import forms

class Show_detelis(forms.Form):
    NAME=forms.CharField(
        label='Enter name ',
    )
    ROLL_number=forms.IntegerField()
    city = forms.CharField(initial='Bhubaneswar')

    password=forms.CharField(
        label='PASSWORD',
        widget=forms.PasswordInput(),
    )
