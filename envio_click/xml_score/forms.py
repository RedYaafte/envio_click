from django import forms

from xml_score.models import XmlScore


class XmlScoreForm(forms.ModelForm):

    class Meta:
        model = XmlScore
        fields = ['xml']