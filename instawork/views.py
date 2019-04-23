from rest_framework import viewsets

from instawork.models import TeamMember
from instawork.serializers import TeamMemberSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
