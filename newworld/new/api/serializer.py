from rest_framework.serializers import ModelSerializer
from new.models import Room


class RoomSeriallizer(ModelSerializer):
    class meta:
        model = Room
        fields = '__all__'
