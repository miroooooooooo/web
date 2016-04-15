# coding=utf-8
from __future__ import unicode_literals

from django import forms

from .tester import POCET_PRVKOV

class SubmitForm(forms.Form):
    selection = forms.IntegerField(min_value=1, max_value=POCET_PRVKOV, label='Druhá najlepšia zlúčenina')
