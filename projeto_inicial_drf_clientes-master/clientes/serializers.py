from clientes.validator import celular_valido, cpf_valido
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O Nome não pode ter números"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve respeitar o seguinte padrão 84 98765-4321"})
        
        return data
