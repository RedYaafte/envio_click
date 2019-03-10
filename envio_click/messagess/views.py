from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.views.generic.detail import DetailView
from django.views.generic import View

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from messagess.models import Message
from messagess.serializers import MessageSerializer


from django.core import signing


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailView(DetailView):
    model = Message
    template_name = 'messagess/message_detail.html'


class MessageDecipherView(View):
    def get(self, request, *args, **kwargs):
        message_id = kwargs['pk']
        message = get_object_or_404(Message, pk=message_id)

        if ":" not in message.content:
            print('no contiene :')
            return HttpResponseRedirect(reverse('message-detail', args=[message.id]))
        else:
            message.content = signing.loads(message.content)
            message.save()

        return HttpResponseRedirect(reverse('message-detail', args=[message.id]))

        """ Se tiene que publicar como un twitter """
