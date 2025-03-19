from django import forms


class valideForm(forms.Form):

    choise_value = forms.ChoiceField(choices=((1, "Внести"), (2, "Снять")),
                                     label='',
                                     error_messages={
                                         'required': 'Заполните поле'},
                                     widget=forms.Select(attrs={'class': 'choise_vidget'}, ))

    value = forms.IntegerField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Введите сумму'}),
                               error_messages={
                                   'required': 'Заполните поле'})
