from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import View

from xml_score.models import XmlScore
from xml_score.forms import XmlScoreForm

import xml.etree.ElementTree as ET


class XmlScoreCreateView(CreateView):
    """ File upload """
    model = XmlScore
    form_class = XmlScoreForm

    def get_success_url(self):
        return reverse_lazy('detail-view', args=[self.object.id])


class XmlScoreDetailView(DetailView):
    """ File detail """
    model = XmlScore


class XmlScoreView(View):
    """ Calculate attributes """
    def get(self, request, *args, **kwargs):
        xml_id = kwargs['pk']
        xml = get_object_or_404(XmlScore, pk=xml_id)

        # Extract file path
        tree = ET.parse(xml.xml)
        root = tree.getroot()
        count = len(root.attrib)
        
        # Calculate number of attributes
        def count_of_attr(root):
            count = len(root.attrib)
            for child in root:
                count += count_of_attr(child)
            return count

        xml.score = count_of_attr(root)
        xml.save()

        return HttpResponseRedirect(reverse('detail-view', args=[xml_id]))
