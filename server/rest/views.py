from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest.serializers import UserSerializer, GroupSerializer, LeadSerializer
from rest.models import Lead
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get_queryset(self):
        query_params = self.request.GET
        if 'single' in query_params and query_params['single'] in ['true', 'True', 'TRUE']:
            return Lead().get_single_result(query_params)
        return Lead().get_by_components(query_params)

    """
        def retrieve(self, request, pk=None):
        queryset = Owner.objects.all()
        owner = get_object_or_404(queryset, pk=pk)

        if self.request.user in owner.users.all():
            serializer = OwnerSerializer(owner)
            return Response(serializer.data)

        query_params = self.request.GET
        if 'purchase' in query_params and query_params['purchase'] in ['true', 'True', 'TRUE']:
            # TODO: Purchase the Owner data
            pass
        else:
            return Response("Owner data available for purchase.", 402)

        serializer = OwnerSerializer(owner)
        return Response(serializer.data)
    """
