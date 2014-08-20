from django.forms import ModelForm
from brochure.models import Contact

__author__ = 'roxnairani'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
