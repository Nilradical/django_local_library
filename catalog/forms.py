from django import forms
import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks.", initial=datetime.date.today()
                                                                                              + datetime.timedelta(21))
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        #check if a date s not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in the past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
