from clientes.models import Cliente
from clientes.validator import *
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O Nome não pode ter números"})
        
        return data
