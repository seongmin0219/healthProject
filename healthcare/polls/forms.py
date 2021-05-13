from django import forms

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

class healthCareForm(forms.Form):

    today_health_history = forms.charField(label = 'Your name name' , max_length = 7)

