from django import forms


class TokenForm(forms.Form):
    card_id_input = forms.CharField(label='Card ID', max_length=50)
    amount_input = forms.IntegerField(label='Token amount', min_value=1)
    operation_input = forms.ChoiceField(label='Operation', choices=[
                                        ('+', '+'), ('-', '-')], widget=forms.RadioSelect)

class ResetForm(forms.Form):
    card_id_input = forms.CharField(label='Card ID', max_length=50)
