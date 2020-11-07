from rest_framework import serializers
from .models import Key, Session, User


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['license']

class UpdateSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['license', 'remote_session_id']