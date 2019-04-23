from rest_framework import serializers

from instawork.models import TeamMember


class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'role')
